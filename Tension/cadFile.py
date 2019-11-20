"""
Initialized on 23-04-2019
Commenced on 18-11-2019
@author: Anand Swaroop
"""""

import numpy
import copy
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse


class CAD(object):
    def __init__(self, member, plate, weld, input, memb_data ):
        """

        :param member: Angle or Channel
        :param plate: Plate
        :param weld: weld
        :param input: input parameters
        :param memb_data: data of the members
        """


        self.member = member
        self.plate = plate
        self.weld1 = weld
        self.weld2 = copy.deepcopy(weld)
        self.weld3 = copy.deepcopy(weld)
        self.input = input
        self.memb_data = memb_data




    def create_3DModel(self):
        pass

        # self.createPlateGeometry()
        # self.createMemberGeometry()
        # self.createweldGeometry()
        #
        # self.plateModel = self.plate.create_model()
        # self.memberModel = self.member.create_model()
        # self.weld1_Model = self.weld1.create_model()
        # self.weld2_Model = self.weld2.create_model()
        # self.weld3_Model = self.weld3.create_model()



    def createPlateGeometry(self):
        """

         :return: Geometric Orientation of this component
        """
        beamOriginL = numpy.array([0.0, 0.0, 0.0])
        beamL_uDir = numpy.array([1.0, 0.0, 0.0])
        beamL_wDir = numpy.array([0.0, 0.0, 1.0])
        self.plate.place(beamOriginL, beamL_uDir, beamL_wDir)


    def createMemberGeometry(self):
        """

         :return: Geometric Orientation of this component
        """
        beamOriginL = numpy.array([0.0, 0.0, 0.0])
        beamL_uDir = numpy.array([1.0, 0.0, 0.0])
        beamL_wDir = numpy.array([0.0, 0.0, 1.0])
        self.member.place(beamOriginL, beamL_uDir, beamL_wDir)



    def createweldGeometry(self):
        pass
        # """
        #
        #  :return: Geometric Orientation of this component
        #  """
        # beamOriginL = numpy.array([0.0, 0.0, 0.0])
        # beamL_uDir = numpy.array([1.0, 0.0, 0.0])
        # beamL_wDir = numpy.array([0.0, 0.0, 1.0])
        # self.weld1.place(beamOriginL, beamL_uDir, beamL_wDir)
        #
        # beamOriginL = numpy.array([0.0, 0.0, 0.0])
        # beamL_uDir = numpy.array([1.0, 0.0, 0.0])
        # beamL_wDir = numpy.array([0.0, 0.0, 1.0])
        # self.weld2.place(beamOriginL, beamL_uDir, beamL_wDir)
        #
        # beamOriginL = numpy.array([0.0, 0.0, 0.0])
        # beamL_uDir = numpy.array([1.0, 0.0, 0.0])
        # beamL_wDir = numpy.array([0.0, 0.0, 1.0])
        # self.weld3.place(beamOriginL, beamL_uDir, beamL_wDir)

    def get_models(self):
        pass
        # components = [self.memberModel, self.plateModel, self.weld1_Model, self.weld2_Model, self.weld3_Model)
        #
        # CAD = components[0]
        # for comp in components[1:]:
        #     plates = BRepAlgoAPI_Fuse(comp, CAD).Shape()
        #
        # return CAD
