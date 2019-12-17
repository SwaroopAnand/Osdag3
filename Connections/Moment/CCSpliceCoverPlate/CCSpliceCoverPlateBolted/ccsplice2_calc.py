'''
# Created on 30-Oct-2017
# Revised on 5-March-2018
# Revised on 13-April-2018
# Revised on 15-June-2018 (experts suggestions)
# Revised on 18-June-2018 (experts suggestions)
# Revised on 25-June-2018 (After launch)
@author: Kumari Anjali.
'''
'''
ASCII diagram- Column-Column Bolted Splice Connection with Cover Plates
'''

import sys

from Connections.Moment.CCSpliceCoverPlate.CCSpliceCoverPlateBolted.model import *
from utilities.is800_2007 import *
from utilities.other_standards import IS1363_part_1_2002, IS1363_part_3_2002, IS1367_Part3_2002
from Connections.connection_calculations import ConnectionCalculations
import math
import logging
import sys

flag = 1
logger = None


def module_setup():
    global logger
    logger = logging.getLogger("osdag.ccsplice_calc")
    module_setup()
    #######################################################################

    # Start of Main Program


def coverplateboltedconnection(uiObj):
    global logger
    logger = logging.getLogger("osdag.ccsplice_calc")
    global design_status
    design_status = True

    connectivity = uiObj["Member"]["Connectivity"]
    column_section = uiObj["Member"]["ColumnSection"]
    column_fu = float(uiObj["Member"]["fu (MPa)"])
    column_fy = float(uiObj["Member"]["fy (MPa)"])

    axial_force = float(uiObj["Load"]["AxialForce"])
    moment_load = float(uiObj["Load"]["Moment (kNm)"])
    shear_load = float(uiObj["Load"]["ShearForce (kN)"])
    if shear_load == '':
        shear_load = 0
    else:
        shear_load = float(uiObj["Load"]["ShearForce (kN)"])

    bolt_diameter = int(uiObj["Bolt"]["Diameter (mm)"])
    bolt_grade = float(uiObj["Bolt"]["Grade"])
    bolt_type = (uiObj["Bolt"]["Type"])
    flange_plate_preference = uiObj['FlangePlate']['Preferences']
    gap = float(uiObj["detailing"]["gap(mm)"])  # gap between web  plate and column flange

    mu_f = float(uiObj["bolt"]["slip_factor"])
    dp_bolt_hole_type = str(uiObj["bolt"]["bolt_hole_type"])
    #dp_bolt_hole_type = ["standard","over_size", "short_slot","long_slot"]
    #dia_hole = IS800_2007.cl_10_2_1_bolt_hole_size(d =bolt_diameter, bolt_hole_type='standard')

    dia_hole = int(uiObj["bolt"]["bolt_hole_clrnce"]) + bolt_diameter
    bolt_fu = float(uiObj["bolt"]["bolt_fu"])
    # bolt_fy = float(uiObj["bolt"]["bolt_fy"])


    if uiObj["detailing"]["typeof_edge"] == "a - Sheared or hand flame cut":
        type_edge = 'hand_flame_cut'
    else:   # "b - Rolled, machine-flame cut, sawn and planed"
        type_edge = 'machine_flame_cut'
    type_edge = str(uiObj["detailing"]["typeof_edge"])
    flange_plate_t = float(uiObj["FlangePlate"]["Thickness (mm)"])
    flange_plate_w = float(uiObj["FlangePlate"]["Width (mm)"])
    flange_plate_l = str(uiObj["FlangePlate"]["Height (mm)"])
    flange_plate_l = float(flange_plate_l)
    # flange_plate_fu = float(uiObj["Member"]["fu (Mpa)"])
    # flange_plate_fy = float(uiObj["Member"]["fy (MPa)"])
    flange_plate_fu = float(column_fu)
    flange_plate_fy = float(column_fy)
    web_plate_t = float(uiObj['WebPlate']['Thickness (mm)'])
    web_plate_l = str(uiObj["FlangePlate"]["Height (mm)"])
    web_plate_l = float(web_plate_l)
    web_plate_w = str(uiObj["WebPlate"]["Width (mm)"])
    web_plate_w = float(web_plate_w)
    web_plate_l = str(uiObj["FlangePlate"]["Height (mm)"])
    web_plate_l = float(web_plate_l)
    web_plate_fu = float(column_fu)
    web_plate_fy = float(column_fy)

    old_column_section = get_oldcolumncombolist()

    if column_section in old_column_section:
        logger.warning(" : You are using a section (in red color) that is not available in latest version of IS 808")
    if column_fu < 410 or column_fy < 230 or flange_plate_fu or flange_plate_fy or web_plate_fu or web_plate_fy:
        logger.warning(" : You are using a section of grade that is not available in latest version of IS 2062")

    ########################################################################################################################
    # Read input values from Column  database

    dictcolumndata = get_columndata(column_section)

    column_t_w = float(dictcolumndata["tw"])
    column_f_t = float(dictcolumndata["T"])
    column_d = float(dictcolumndata["D"])

    column_r1 = float(dictcolumndata["R1"])
    column_b = float(dictcolumndata["B"])
    column_area = float(dictcolumndata["Area"])
    column_Zz = float(dictcolumndata["Zz"])

    # Minimum Design Action (Cl. 10.7, IS 800:2007)
    # Axial Capacity #kN
    gamma_m0 = 1.1
    Axial_capacity = 0.3 * column_area * column_fy / gamma_m0
    factored_axial_force = max(Axial_capacity, axial_force)

    # Shear Capacity   # kN

    A_v = column_area  #todo
    design_shear_capacity = (A_v * column_fy) / (math.sqrt(3) * gamma_m0 * 1000)  # kN # A_v: Total cross sectional area in shear in mm^2 (float)
    if shear_load >= design_shear_capacity:
        design_status = False
    #######################################################################
    # Calculation of Spacing (Min values rounded to next multiple of 5)

    #  Minimum pitch & gauge distance  of flange and web plate(mm)
    pitch_dist_min_f = IS800_2007.cl_10_2_2_min_spacing(bolt_diameter)
    pitch_dist_min_w = IS800_2007.cl_10_2_2_min_spacing(bolt_diameter)

    platethickness_f = [column_f_t, flange_plate_t]
    platethickness_w = [column_t_w, web_plate_t]

    web_t_thinner = (min(column_t_w, web_plate_t))
    flange_t_thinner = (min(column_f_t, flange_plate_t))

    # Maximum pitch and gauge distance for Flange splice plate
    pitch_dist_max_f = IS800_2007.cl_10_2_3_1_max_spacing(plate_thicknesses =   platethickness_f)

    # Maximim pitch and gauge distance for Web splice plate
    pitch_dist_max_w = IS800_2007.cl_10_2_3_1_max_spacing( plate_thicknesses =  platethickness_w )

    flange_pitch = round(pitch_dist_min_f + 10)
    flange_gauge = flange_pitch
    web_pitch = round(pitch_dist_min_w + 10)
    web_gauge = round(pitch_dist_min_w + 10)
    # min_end_distance & max_end_distance = Minimum and Maximum end distance
    #       [Cl. 10.2.4.2 & Cl. 10.2.4.3, IS 800:2007]

    # min_end_distance and max end distance for flange plate
    corrosive_influences = False
    if uiObj['detailing']['is_env_corrosive'] == "Yes":
        corrosive_influences = True

    [bolt_shank_area, bolt_net_area] = IS1367_Part3_2002.bolt_area(bolt_diameter)

    end_dist_min_f = IS800_2007.cl_10_2_4_2_min_edge_end_dist(
        d=bolt_diameter, bolt_hole_type= dp_bolt_hole_type, edge_type=type_edge)
    end_dist_max_f = IS800_2007.cl_10_2_4_3_max_edge_dist(
        plate_thicknesses=platethickness_f, f_y=column_fy, corrosive_influences=corrosive_influences)

    # min_end_distance and max end distance for web plate
    end_dist_min_w = IS800_2007.cl_10_2_4_2_min_edge_end_dist(
        d=bolt_diameter, bolt_hole_type=dp_bolt_hole_type, edge_type=type_edge)
    end_dist_max_w = IS800_2007.cl_10_2_4_3_max_edge_dist(
        plate_thicknesses = platethickness_w, f_y=column_fy, corrosive_influences=corrosive_influences)

    edge_dist_min_f = end_dist_min_f
    edge_dist_max_f= end_dist_max_w

    end_dist_f = round(end_dist_min_f + 5)
    end_dist_w = round(end_dist_min_w + 5)
    edge_dist_f = end_dist_f
    edge_dist_w = end_dist_w

    #######################################################################
    ###### Calculate bolt capacities ###
    # Calculation of kb for flange
    kbChk1 = end_dist_min_f / float(3 * dia_hole)
    kbChk2 = pitch_dist_min_f / float(3 * dia_hole) - 0.25
    kbChk3 = bolt_fu / float(column_fu)
    kbChk4 = 1
    kb = float(min(kbChk1, kbChk2, kbChk3, kbChk4))
    kb = round(kb, 3)

    # Bolt capacity calculation for flange splice
    if flange_plate_preference == "Outside":
        flange_t_thinner = min(column_f_t, flange_plate_t)
    else:
        flange_t_thinner = min(column_f_t, (2 * flange_plate_t))

    flange_bolt_planes = 1
    number_of_bolts = 1

    if bolt_type == "Bearing Bolt":
        flange_bolt_shear_capacity = round(ConnectionCalculations.bolt_shear(bolt_diameter, flange_bolt_planes, bolt_fu), 2)
        flange_bolt_bearing_capacity = round(ConnectionCalculations.bolt_bearing(bolt_diameter, number_of_bolts, flange_t_thinner,\
                                                                            kb, flange_plate_fu), 2)
        flange_bolt_capacity = min(flange_bolt_shear_capacity,flange_bolt_bearing_capacity)

    elif bolt_type == "Friction Grip Bolt":
        muf = mu_f
        bolt_hole_type = dp_bolt_hole_type  # 1 for standard, 0 for oversize hole
        n_e = 2  # number of effective surfaces offering frictional resistance
        flange_bolt_shear_capacity = round(ConnectionCalculations.bolt_shear_friction_grip_bolt(bolt_diameter, bolt_fu, muf, n_e, bolt_hole_type), 2)
        flange_bolt_bearing_capacity = 'N/A'
        flange_bolt_capacity = flange_bolt_shear_capacity

            #print(flange_bolt_bearing_capacity, flange_bolt_shear_capacity, flange_bolt_capacity)
    else:
        pass

    # Bolt capacity calculation for web splice
    web_bolt_planes = 1
    number_of_bolts = 1

    if bolt_type == "Bearing Bolt":
        web_bolt_shear_capacity = round(
            ConnectionCalculations.bolt_shear(bolt_diameter, web_bolt_planes, bolt_fu), 2)
        web_bolt_bearing_capacity = round(
            ConnectionCalculations.bolt_bearing(bolt_diameter, number_of_bolts, web_t_thinner, \
                                                kb, web_plate_fu), 2)
        web_bolt_capacity = min(web_bolt_shear_capacity, web_bolt_bearing_capacity)

    elif bolt_type == "Friction Grip Bolt":
        muf = mu_f
        bolt_hole_type = dp_bolt_hole_type  # 1 for standard, 0 for oversize hole
        n_e = 2  # number of effective surfaces offering frictional resistance
        flange_bolt_shear_capacity = round(
            ConnectionCalculations.bolt_shear_friction_grip_bolt(bolt_diameter, bolt_fu, muf, n_e, bolt_hole_type), 2)
        flange_bolt_bearing_capacity = 'N/A'
        flange_bolt_capacity = flange_bolt_shear_capacity

        # print(flange_bolt_bearing_capacity, flange_bolt_shear_capacity, flange_bolt_capacity)
    else:
        pass
    number_of_column_flange =2 # todo
    number_of_column_web = 3
    ####check for long joints and large grip length in flange
    lj_flange = (number_of_column_flange - 1) * flange_gauge # lONG jOINT flange
    lj_web = (number_of_column_web  - 1) * web_gauge # long joint web
    if flange_plate_preference == "Outside + Inside": # large grip flange
        lg_flange = column_f_t + 2 * flange_plate_t
    else:
        lg_flange = column_f_t + flange_plate_t
    lg_web = column_t_w + (2* web_plate_t)
    beta_lj_flange = IS800_2007.cl_10_3_3_1_bolt_long_joint(d=bolt_diameter, l_j = lj_flange)
    beta_lg_flange =IS800_2007.cl_10_3_3_2_bolt_large_grip(d= bolt_diameter, l_g = lg_flange, l_j=0)
    beta_lj_web = IS800_2007.cl_10_3_3_1_bolt_long_joint(d=bolt_diameter, l_j = lj_web)
    beta_lg_web = IS800_2007.cl_10_3_3_2_bolt_large_grip(d=bolt_diameter, l_g=lg_web, l_j=0)

    flange_bolt_capacity_red = flange_bolt_capacity *beta_lj_flange *  beta_lg_flange
    web_bolt_capacity_red = web_bolt_capacity * beta_lj_web * lg_web
    #print(flange_bolt_capacity_red, web_bolt_capacity_red)

    # PACKING PLATES #TODO

    def flange_force(column_d, column_f_t, column_b, column_area, axial_force, moment_load):

        """
        Args:
           Column_d: Overall depth of the column section in mm (float)
           Column_b: width of the column section in mm (float)
           Column_f_t: Thickness of flange in mm (float)
           axial_force: Factored axial force in kN (float)
           moment_load: Factored bending moment in kN-m (float)
        Returns:
            Force in flange in kN (float)
        """

        area_f = column_b * column_f_t
        axial_force_f = float(area_f * axial_force / column_area)
        f_f = round((moment_load * 1000) / (column_d - column_f_t), 2) + (axial_force_f)
        return (f_f)

     # Calculation of number of bolts required for web splice plate
    if shear_load != 0:
        web_bolts_required = int(math.ceil(shear_load / web_bolt_capacity_red))
    else:
        web_bolts_required = 2




