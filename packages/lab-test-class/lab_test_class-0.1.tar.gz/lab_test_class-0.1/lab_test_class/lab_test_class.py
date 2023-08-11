import pandas as pd
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import ast
from kneed import KneeLocator
from scipy.integrate import simps


class lab_test(object):
    def __init__(self, name):
        self.name = name

    def calculate_effective_stress(self, stress, pore_pressure):
        eff_sig_33 = stress['sig_33'] - pore_pressure
        eff_sig_22 = stress['sig_22'] - pore_pressure
        eff_sig_11 = stress['sig_11'] - pore_pressure
        sig_12 = stress['sig_12']
        sig_13 = stress['sig_13']
        sig_23 = stress['sig_23']
        eff_stress = {'sig_11': eff_sig_11, 'sig_22': eff_sig_22, 'sig_33': eff_sig_33, 'sig_12': sig_12,
                      'sig_13': sig_13, 'sig_23': sig_23}
        return eff_stress

    def check_triaxial_state(self, Frame, effective_stress, strain):
        sig_33 = effective_stress['sig_33']
        sig_22 = effective_stress['sig_22']
        sig_11 = effective_stress['sig_11']
        eps_33 = strain['eps_33']
        eps_22 = strain['eps_22']
        eps_11 = strain['eps_11']

        tolerance = 1e-2

        if abs((sig_11 - sig_22)) > tolerance:
            raise ValueError('the lateral stresses are diverging too much at Frame %s' % Frame)

        if abs((eps_11 - eps_22)) > tolerance:
            raise ValueError('the lateral stains are diverging too much at Frame %s' % Frame)

    def calculate_deviatoric_stress(self, Frame, effective_stress):
        # the stress state is supposed triaxial (axisymetric)
        sig_33 = effective_stress['sig_33']
        sig_22 = effective_stress['sig_22']
        sig_11 = effective_stress['sig_11']

        q = sig_33 - sig_22
        return q

    def calculate_mean_stress(self, Frame, effective_stress):
        sig_33 = effective_stress['sig_33']
        sig_22 = effective_stress['sig_22']
        sig_11 = effective_stress['sig_11']
        # the stress state is supposed triaxial (axisymetric)
        p = (sig_11 + sig_22 + sig_33) / 3
        return p

    def calculate_volumetric_strain(self, Frame, strain):
        eps_33 = strain['eps_33']
        eps_22 = strain['eps_22']
        eps_11 = strain['eps_11']

        eps_p = eps_11 + eps_22 + eps_33
        return eps_p

    def calculate_deviatoric_strain(self, Frame, strain):
        eps_33 = strain['eps_33']
        eps_22 = strain['eps_22']
        eps_11 = strain['eps_11']

        eps_q = 2 / 3 * (eps_33 - eps_22)

        return eps_q

    def calculate_tau(self, Frame, stress):
        tau_31 = stress['sig_13']
        return tau_31

    def calculate_gamma(self, Frame, strain):
        gamma = strain['eps_13']
        return gamma

    def tg_shear_stiffness_vs_shear_strain(self, eps_q, q):
        pass

    def secant_shear_stiffness_vs_shear_strain(self, eps_q, q):
        G = []
        for index, value in enumerate(eps_q):
            if index == 0:
                pass
            else:
                Gsec = (q[index] - 0) / (eps_q[index] - 0)
                G.append(Gsec / 3)

        return G

    def shear_stiffness_vs_shear_strain(self, eps_q, q):
        dx = np.diff(eps_q)
        dy = np.diff(q)
        slope = dy / dx
        G = slope / 3

        return G

    def calculate_initial_shear_stiffness(self, eps_q, q):
        # the shear stiffness can be calculated from a q_vs_eps_q graph using this formula : dq/deps_q=3G
        # the initial tangent of the plot needs to be evaluated
        # eps_q_list=list(df['deviatoric_strain'][:])
        # q_list=list(df['deviatoric_stress'][:])

        eps_q_list = eps_q
        q_list = q

        fittedcurve = np.polyfit(eps_q_list, q_list, 3)
        xpoint = 0
        deriv = np.polyder(fittedcurve)
        slope_1 = np.polyval(deriv, xpoint)
        G0_1 = slope_1 / 3
        print('the slope using methode 1 is %f' % slope_1)
        print('the shear modulus using method 1 is %f' % G0_1)
        # use the first points to draw a strain line, and take the slope of this line
        line = np.polyfit(eps_q_list[0:10], q_list[0:10], 1)
        slope_2 = line[0]
        G0_2 = slope_2 / 3
        print('the slope using methode 2 is %f' % slope_2)
        print('the shear modulus using method 2 is %f' % G0_2)
        dx = np.diff(eps_q_list)
        dy = np.diff(q_list)
        m = dy / dx
        slope_3 = m[0]
        G0_3 = slope_3 / 3
        print('the slope using methode 3 is %f' % slope_3)
        print('the shear modulus using method 3 is %f' % G0_3)
        return slope_1, slope_2, slope_3, G0_1, G0_2, G0_3

    def q_vs_eps_q_graph(self, df):
        q_list = list(-np.array(df['deviatoric_stress'][:]))
        eps_q_list = list(-np.array(df['deviatoric_strain'][:]))

        # create the figure
        fig, ax = plt.subplots()
        ax.set_xlabel('eps_q')
        ax.set_ylabel('q (kPa)', fontsize=12)
        ax.plot(eps_q_list, q_list, 'ro-')
        return q_list, eps_q_list

    def q_vs_eps_p_graph(self, df):
        q_list = list(df['deviatoric_stress'][:])
        eps_p_list = list(df['volumetric_strain'][:])

        # create the figure
        fig, ax = plt.subplots()
        ax.set_xlabel('eps_p')
        ax.set_ylabel('q (kPa)', fontsize=12)
        ax.plot(eps_p_list, q_list, 'ro-')

    def q_vs_eps_33_graph(self, df):
        q_list = list(-np.array(df['deviatoric_stress'][:]))
        eps_33_list = []
        for i, values in enumerate(df['strain'].values[:]):
            eps_33_list.append(-1 * values['eps_33'])

        fig, ax = plt.subplots()
        ax.set_xlabel('eps_33')
        ax.set_ylabel('q (kPa)', fontsize=12)
        ax.plot(eps_33_list, q_list, 'ro-')
        return q_list, eps_33_list

    def q_vs_p_graph(self, df):
        q_list = list(-np.array(df['deviatoric_stress'][:]))
        p_list = list(-np.array(df['mean_stress'][:]))

        # create the figure
        fig, ax = plt.subplots()
        ax.set_xlabel('p (kPa)')
        ax.set_ylabel('q (kPa)', fontsize=12)
        ax.plot(p_list, q_list, 'ro-')

    def por_vs_eps_33(self, df):
        por = list(-np.array(df['pore_pressure']))
        eps_33_list = []
        for i, values in enumerate(df['strain'].values[:]):
            eps_33_list.append(-1 * values['eps_33'])

        fig, ax = plt.subplots()
        ax.set_xlabel('eps_33')
        ax.set_ylabel('pore_pressure (kPa)', fontsize=12)
        ax.plot(eps_33_list, por, 'ro-')

        return eps_33_list, por

    def Gmax_hypoplastic_sand(self, mR, hs, n, p0, ec0, ei0, ed0, e, beta, phi, alpha):
        phi = np.radians(phi)

        k = 1 - np.sin(phi)

        a = np.sqrt(3) * np.maximum(3 - np.sin(phi), 0) / (2 * np.sqrt(2) * np.sin(phi))

        fk = 0.5 * (np.maximum(0, 1 + 2 * k ** 2) + np.maximum(0, 1 - k) * a ** 2) / (np.maximum(0, 1 + 2 * k ** 2))

        fa = ((ei0 / ec0) ** beta) * ((1 + ei0) / ei0) * (
                    3 + a ** 2 + a * np.sqrt(3) * ((ei0 - ed0) / (ec0 - ed0)) ** alpha) ** (-1)

        G = mR * hs / n * ((3 * p0 / hs) ** (1 - n)) * ((ec0 / e) ** beta) * fa * fk

        return G

    def E_vs_eps_33_hypoplastic(self, q, eps_33):
        dy = np.diff(q)
        dx = np.diff(eps_33)

        E = dy / dx

        return E

    def hs_n_calibration(self, pressure_list, void_list, stress_range_min, stress_range_max):
        # calibrates the hs and n parameters from oedometric test
        # takes two lists (void ratio and pressure)
        # fit the curve with a 3rd degree polynomial
        fittedcurve = np.polyfit(np.log(pressure_list), void_list, 3)
        derriv = np.polyder(fittedcurve)

        # take two points from the curve (pressures) to encompase the stress range of interest

        Cc_1 = -1 * np.polyval(derriv, np.log(stress_range_min))

        void_1 = np.polyval(fittedcurve, np.log(stress_range_min))

        Cc_2 = -1 * np.polyval(derriv, np.log(stress_range_max))

        void_2 = np.polyval(fittedcurve, np.log(stress_range_max))

        # take two points from the curve (pressures) to encompase the stress range of interest

        n = np.log((void_1 * Cc_2) / (void_2 * Cc_1)) / np.log(stress_range_max / stress_range_min)

        # calculate hs
        hs_1 = 3 * stress_range_min * (n * void_1 / Cc_1) ** (1 / n)
        hs_2 = 3 * stress_range_max * (n * void_2 / Cc_2) ** (1 / n)
        hs = (hs_1 + hs_2) / 2
        return n, hs

    def hs_n_calibration_manual(self, pressure_list, void_list, id_1, id_2, id_3, id_4, id_5, id_6):
        # the manual calibration requires 6 points : 2 at the early portion of the curve, 2 at the end and 2 at the middle
        Cc_1 = abs((void_list[id_1] - void_list[id_2]) / (np.log(pressure_list[id_1]) - np.log(pressure_list[id_2])))
        print(Cc_1)
        Cc_2 = abs((void_list[id_3] - void_list[id_4]) / (np.log(pressure_list[id_3]) - np.log(pressure_list[id_4])))
        print(Cc_2)
        Cc_3 = abs((void_list[id_5] - void_list[id_6]) / (np.log(pressure_list[id_5]) - np.log(pressure_list[id_6])))
        print(Cc_3)
        void_1 = (void_list[id_1] + void_list[id_2]) / 2

        void_2 = (void_list[id_3] + void_list[id_4]) / 2

        void_3 = (void_list[id_5] + void_list[id_6]) / 2

        pressure_1 = np.exp((np.log(pressure_list[id_1]) + np.log(pressure_list[id_2])) / 2)

        pressure_2 = np.exp((np.log(pressure_list[id_3]) + np.log(pressure_list[id_4])) / 2)

        pressure_3 = np.exp((np.log(pressure_list[id_5]) + np.log(pressure_list[id_6])) / 2)

        n = np.log((void_1 * Cc_2) / (void_2 * Cc_1)) / np.log(pressure_2 / pressure_1)

        hs = 3 * pressure_3 * (n * void_3 / Cc_3) ** (1 / n)

        return n, hs

    def ec0_ed0_ei0_calibration(self, hs, n, pressure_list, void_list):
        # read the critical void ratio at different corresponding mean pressures
        # the calibration of the critical state void ratios is best done using undrained triaxial tests (Masin)
        # it is done using curve fitting and reading the void ratio at 0 mean pressure

        def func(X, ec0):
            p, hs, n = X
            f = ec0 * np.exp(-(3 * p / hs) ** n)
            return f

        hs_list = list([hs])
        n_list = list([n])
        length = len(pressure_list)
        for i in range(0, length - 1):
            hs_list.append(hs)
            n_list.append(n)
        popt, pcov = curve_fit(func, (np.array(pressure_list), np.array(hs_list), np.array(n_list)),
                               np.array(void_list))
        ec0 = popt
        ed0 = 0.5 * ec0
        ei0 = 1.2 * ec0
        return ec0, ed0, ei0

    def beta_alpha_calibration(self, stress, strain, target_stress, target_strain, strain_limit_alpha,
                               strain_limit_beta):
        # stress vs strain and target_stress vs target_strain must be given in the same space
        # the calibration of the alpha and beta parameters is done using triaxial shear tests in a q vs eps_q space
        # the pisa lab tests are given in an q vs eps_33 space
        # beta controls the initial stiffness and bulk
        # alpha controlls the peak and post peak resistance
        # this function calculate the area below the simulated test(element test or abaqus) versus the given lab test (real lab test result or paper results...)
        # ----------------------------------------#
        # ----------beta calibration------------#
        # since the beta parameter controlls the initial stiffness and bulk, we are going to compare areas for a limited strain level (0.001 for example...)
        # take the stresses and strains that are lower than the strain_limit
        dummy_stress = []
        dummy_strain = []
        dummy_stress_target = []
        dummy_strain_target = []
        for i, value in enumerate(strain):
            if value <= strain_limit_beta:
                dummy_strain.append(value)
                dummy_stress.append(stress[i])
        for i, value in enumerate(target_strain):
            if value <= strain_limit_beta:
                dummy_strain_target.append(value)
                dummy_stress_target.append(target_stress[i])

        area_smalldisplacement_computed = simpson(y=dummy_stress, x=dummy_strain)
        area_smalldisplacement_target = simpson(y=dummy_stress_target, x=dummy_strain_target)
        n_smalldisplacement = abs(
            (area_smalldisplacement_computed - area_smalldisplacement_target) / (area_smalldisplacement_target))

        # ----------alpha_calibration-------------#

        dummy_stress = []
        dummy_strain = []
        dummy_stress_target = []
        dummy_strain_target = []
        for i, value in enumerate(strain):
            if value <= strain_limit_alpha:
                dummy_strain.append(value)
                dummy_stress.append(stress[i])
        for i, value in enumerate(target_strain):
            if value <= strain_limit_alpha:
                dummy_strain_target.append(value)
                dummy_stress_target.append(target_stress[i])
        area_computed = simpson(y=dummy_stress, x=dummy_strain)
        area_target = simpson(y=dummy_stress_target, x=dummy_strain_target)
        n = abs((area_computed - area_target) / area_target)

        return n_smalldisplacement, n

    def mR_calibration(self, stress, G0, target_stress, target_G0, stress_range_min, stress_range_max):
        dummy_stress = []
        dummy_G0 = []
        dummy_stress_target = []
        dummy_G0_target = []
        for i, value in enumerate(stress):
            if value <= stress_range_max and value >= stress_range_min:
                dummy_stress.append(value)
                dummy_G0.append(G0[i])
        for i, value in enumerate(target_stress):
            if value <= stress_range_max and value >= stress_range_min:
                dummy_stress_target.append(value)
                dummy_G0_target.append(target_G0[i])
        area_computed = simpson(y=dummy_G0, x=dummy_stress)
        area_target = simpson(y=dummy_G0_target, x=dummy_stress_target)
        n = abs((area_computed - area_target) / area_target)
        return n

    def R_betaR_chi_calibration(self, G0, eps_q, target_G0, target_eps_q, strain_range_min, strain_range_max):
        dummy_G0 = []
        dummy_eps_q = []
        dummy_G0_target = []
        dummy_eps_q_target = []

        for i, value in enumerate(eps_q):
            if value <= strain_range_max and value >= strain_range_min:
                dummy_eps_q.append(value)
                dummy_G0.append(G0[i])
        for i, value in enumerate(eps_q_target):
            if value <= strain_range_max and value >= strain_range_min:
                dummy_eps_q_target.append(value)
                dummy_G0_target.append(target_G0[i])
        area_computed = simpson(y=dummy_G0, x=dummy_eps_q)
        area_target = simpson(y=dummy_G0_target, x=dummy_eps_q_target)
        n = abs((area_computed - area_target) / area_target)
        return n

    def Lambda_Kappa_N_calibration(self, method, e, sig_33, id_1, id_2, id_3, id_4):
        def unloading(e, sig_33):
            unloading = False
            for index, value in enumerate(sig_33):
                if index == 0:
                    pass
                elif sig_33[index] < sig_33[index - 1]:
                    unloading = True
                    unload_id = index - 1
                    break
            return unloading, unload_id

        if method == 'automatic':

            unld, indx_unload = unloading(e, sig_33)
            max_value = max(sig_33)
            indx = list(sig_33).index(max_value)
            Lambda = (np.log(1 + e[indx - 1]) - np.log(1 + e[indx])) / (np.log(sig_33[indx]) - np.log(sig_33[indx - 1]))
            N = np.log(1 + e[indx]) + Lambda * np.log(sig_33[indx])

            if unld == True:
                # Lambda=(np.log(1+e[indx-1])-np.log(1+e[indx]))/(np.log(sig_33[indx])-np.log(sig_33[indx-1]))

                # use two points to calculate kappa
                Kappa = (np.log(1 + e[indx_unload + 1]) - np.log(1 + e[indx_unload])) / (
                            np.log(sig_33[indx_unload]) - np.log(sig_33[indx_unload + 1]))

                # N=np.log(1+e[indx])+Lambda*np.log(sig_33[indx])
            else:
                # Lambda=(np.log(1+e[-2])-np.log(1+e[-1]))/(np.log(sig_33[-1])-np.log(sig_33[-2]))

                # use two points to calculate kappa
                Kappa = 0

                # N=np.log(1+e[-1])+Lambda*np.log(sig_33[-1])
        else:
            # use two points to calculate lambda
            Lambda = (np.log(1 + e[id_1]) - np.log(1 + e[id_2])) / (np.log(sig_33[id_2]) - np.log(sig_33[id_1]))

            # use two points to calculate kappa
            Kappa = (np.log(1 + e[id_4]) - np.log(1 + e[id_3])) / (np.log(sig_33[id_3]) - np.log(sig_33[id_4]))

            N = np.log(1 + e[id_2]) + Lambda * np.log(sig_33[id_2])

        return Lambda, Kappa, N

    def casagrande_preconsolidation(self, e, sig_33, flex_point_id):
        # function to find the intersectino between two lines given two points from each line

        def findIntersection(x1, y1, x2, y2, x3, y3, x4, y4):
            px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                        (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
            return [px, py]

        # take only the loading part of oedometer test
        for index, value in enumerate(sig_33):

            if index == 0:
                pass
            elif value < sig_33[index - 1]:
                stress = sig_33[0:index]
                void = e[0:index]
                break
            else:
                stress = sig_33[0:index]
                void = e[0:index]

        x = np.log(stress)
        y = void

        # first we must find the point of maximum curvature
        if flex_point_id == 'automatic':
            kneedle = KneeLocator(x, y, S=1.0, curve="concave", direction="decreasing")
            max_rot_sig = kneedle.knee
            max_rot_e = kneedle.knee_y
            x = x.tolist()
            i_d = x.index(max_rot_sig)

        else:
            max_rot_sig = x[flex_point_id]
            max_rot_e = y[flex_point_id]
            x = x.tolist()
            i_d = flex_point_id
        # the equation of the horizontal line at the max flexion point is f(x)=max_rot_e

        # the tangent at point the point of max rotation
        slope = np.diff(y) / np.diff(x)

        tangent = (slope[i_d] + slope[i_d - 1]) / 2

        # find the bisectrice of the horizontal line and the tangent line
        bisectrice = np.arctan(tangent) / 2
        tangent_bisectrice = np.tan(bisectrice)

        # the bisectrice passes by the maximum rotation point, we need to find an other point
        # f(x)=ax+b=>b=f(x)-ax
        b = max_rot_e - tangent_bisectrice * max_rot_sig

        # find the intersection between the bisectrice and the NCL line
        point = findIntersection(x[-1], y[-1], x[-2], y[-2], max_rot_sig, max_rot_e, 0, b)

        point = point[0]
        preconsolidation = np.exp(point)

        return preconsolidation

    def apply_calculate_effective_stress(self, df):
        df['effective_stress'] = df[['stress', 'pore_pressure']].apply(
            lambda row: self.calculate_effective_stress(row['stress'], row['pore_pressure']), axis=1)

    def apply_check_triaxial_state(self, df):
        df[['Frame', 'effective_stress', 'strain']].apply(
            lambda row: self.check_triaxial_state(row['Frame'], row['effective_stress'], row['strain']), axis=1)

    def apply_calculate_deviatoric_stress(self, df):
        df['deviatoric_stress'] = df[['Frame', 'effective_stress']].apply(
            lambda row: self.calculate_deviatoric_stress(row['Frame'], row['effective_stress']), axis=1)

    def apply_calculate_mean_stress(self, df):
        df['mean_stress'] = df[['Frame', 'effective_stress']].apply(
            lambda row: self.calculate_mean_stress(row['Frame'], row['effective_stress']), axis=1)

    def apply_calculate_volumetric_strain(self, df):
        df['volumetric_strain'] = df[['Frame', 'strain']].apply(
            lambda row: self.calculate_volumetric_strain(row['Frame'], row['strain']), axis=1)

    def apply_calculate_deviatoric_strain(self, df):
        df['deviatoric_strain'] = df[['Frame', 'strain']].apply(
            lambda row: self.calculate_deviatoric_strain(row['Frame'], row['strain']), axis=1)

    def apply_calculate_tau(self, df):
        df['tau'] = df[['Frame', 'stress']].apply(lambda row: self.calculate_tau(row['Frame'], row['stress']), axis=1)

    def apply_calculate_gamma(self, df):
        df['gamma'] = df[['Frame', 'strain']].apply(lambda row: self.calculate_gamma(row['Frame'], row['strain']),
                                                    axis=1)

    def apply_post_processing(self, df):
        # this function is kind of a wrapper function, that applies some of the previous functions.
        self.apply_calculate_effective_stress(df)
        self.apply_check_triaxial_state(df)
        self.apply_calculate_deviatoric_stress(df)
        self.apply_calculate_mean_stress(df)
        self.apply_calculate_volumetric_strain(df)
        self.apply_calculate_deviatoric_strain(df)
        self.apply_calculate_tau(df)
        self.apply_calculate_gamma(df)