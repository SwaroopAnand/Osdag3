"""
Initialized on 23-04-2019
Commenced on 18-11-2019
@author: Anand Swaroop
"""""

import numpy
import copy
# from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse


class CAD(object):
    def __init__(self, member, plate, inline_weld, opline_weld, alist, member_data ):
        """

        :param member: Angle or Channel
        :param plate: Plate
        :param weld: weld
        :param input: input parameters
        :param memb_data: data of the members
        """

        self.member1 = member
        self.member2 = copy.deepcopy(member)
        self.plate1 = plate
        self.plate2 = copy.deepcopy(plate)
        self.inline_weld1 = inline_weld
        self.inline_weld2 = copy.deepcopy(inline_weld)
        self.opline_weld1 = opline_weld

        self.inline_weld11 = copy.deepcopy(inline_weld)
        self.inline_weld22 = copy.deepcopy(inline_weld)
        self.opline_weld11 = copy.deepcopy(opline_weld)

        self.input = alist
        self.memb_data = member_data




    def create_3DModel(self):

        if self.input["Member"]["SectionType"] == "Channels":
            if self.input["Member"]["Location"] == "Web":
                self.createMemberGeometry()
                self.createweldGeometry()
                self.createPlate1Geometry()

                self.member1_Model = self.member1.create_model()
                self.inline_weld1_Model = self.inline_weld1.create_model()
                self.inline_weld2_Model = self.inline_weld2.create_model()
                self.opline_weld1_Model = self.opline_weld1.create_model()
                self.plate1_Model = self.plate1.create_model()

            elif self.input["Member"]["Location"] == "Flange":
                self.createMemberGeometry()
                self.createweldGeometry()
                self.createPlate1Geometry()

                self.member1_Model = self.member1.create_model()
                self.inline_weld1_Model = self.inline_weld1.create_model()
                self.inline_weld2_Model = self.inline_weld2.create_model()
                self.opline_weld1_Model = self.opline_weld1.create_model()
                self.inline_weld11_Model = self.inline_weld11.create_model()
                self.inline_weld22_Model = self.inline_weld22.create_model()
                self.opline_weld11_Model = self.opline_weld11.create_model()
                self.plate1_Model = self.plate1.create_model()
                self.plate2_Model = self.plate2.create_model()

            else:  #"Back to Back Web"
                self.createMemberGeometry()
                self.createweldGeometry()
                self.createPlate1Geometry()

                self.member1_Model = self.member1.create_model()
                self.member2_Model = self.member2.create_model()
                self.inline_weld1_Model = self.inline_weld1.create_model()
                self.inline_weld2_Model = self.inline_weld2.create_model()
                self.opline_weld1_Model = self.opline_weld1.create_model()
                self.inline_weld11_Model = self.inline_weld11.create_model()
                self.inline_weld22_Model = self.inline_weld22.create_model()
                self.opline_weld11_Model = self.opline_weld11.create_model()
                self.plate1_Model = self.plate1.create_model()

        if self.input["Member"]["SectionType"] == "Angles":
            if self.input["Member"]["Location"] == "Leg":
                self.createMemberGeometry()
                self.createweldGeometry()
                self.createPlate1Geometry()

                self.member1_Model = self.member1.create_model()
                self.inline_weld1_Model = self.inline_weld1.create_model()
                self.inline_weld2_Model = self.inline_weld2.create_model()
                self.opline_weld1_Model = self.opline_weld1.create_model()
                self.plate1_Model = self.plate1.create_model()

            elif self.input["Member"]["Location"] == "Back to Back Angles":
                self.createMemberGeometry()
                self.createweldGeometry()
                self.createPlate1Geometry()

                self.member1_Model = self.member1.create_model()
                self.member2_Model = self.member2.create_model()
                self.inline_weld1_Model = self.inline_weld1.create_model()
                self.inline_weld2_Model = self.inline_weld2.create_model()
                self.opline_weld1_Model = self.opline_weld1.create_model()
                self.plate1_Model = self.plate1.create_model()

            else:# self.input["Member"]["Location"] == "Star Angles":
                self.createMemberGeometry()
                self.createweldGeometry()
                self.createPlate1Geometry()

                self.member1_Model = self.member1.create_model()
                self.member2_Model = self.member2.create_model()
                self.inline_weld1_Model = self.inline_weld1.create_model()
                self.inline_weld2_Model = self.inline_weld2.create_model()
                self.opline_weld1_Model = self.opline_weld1.create_model()
                self.plate1_Model = self.plate1.create_model()


    def createPlate1Geometry(self):
        """

         :return: Geometric Orientation of this component
        """
        if self.input["Member"]["SectionType"] == "Channels":
            if self.input["Member"]["Location"] == "Web" or self.input["Member"]["Location"] == "Back to Back Web":
                plate1OriginL = numpy.array([0.0, 0.0, 0.0])
                plate1_uDir = numpy.array([0.0, 1.0, 0.0])
                plate1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.plate1.place(plate1OriginL, plate1_uDir, plate1_wDir)

            # elif self.input["Member"]["Location"] == "Back to Back Web":
            #     plate1OriginL = numpy.array([0.0, 0.0, 0.0])
            #     plate1_uDir = numpy.array([0.0, 1.0, 0.0])
            #     plate1_wDir = numpy.array([1.0, 0.0, 0.0])
            #     self.plate1.place(plate1OriginL, plate1_uDir, plate1_wDir)

            else:  # self.input["Member"]["Location"] == "Flange":
                plate1OriginL = numpy.array([0.0, 0.0, 0.0])
                plate1_uDir = numpy.array([0.0, 1.0, 0.0])
                plate1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.plate1.place(plate1OriginL, plate1_uDir, plate1_wDir)

                plate2OriginL = numpy.array([0.0, -self.plate2.T - self.member1.D , 0.0])
                plate2_uDir = numpy.array([0.0, 1.0, 0.0])
                plate2_wDir = numpy.array([1.0, 0.0, 0.0])
                self.plate2.place(plate2OriginL, plate2_uDir, plate2_wDir)

        if self.input["Member"]["SectionType"] == "Angles":
            plate1OriginL = numpy.array([0.0, 0.0, 0.0])
            plate1_uDir = numpy.array([0.0, 1.0, 0.0])
            plate1_wDir = numpy.array([1.0, 0.0, 0.0])
            self.plate1.place(plate1OriginL, plate1_uDir, plate1_wDir)


    def createMemberGeometry(self):
        """

         :return: Geometric Orientation of this compon\ent
        """
        if self.input["Member"]["SectionType"] == "Channels":
            if self.input["Member"]["Location"] == "Web":
                member1OriginL = numpy.array([self.plate1.W - self.inline_weld1.L, -self.member1.B - self.plate1.T / 2, self.member1.D / 2])
                member1_uDir = numpy.array([0.0, -1.0, 0.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member1.place(member1OriginL, member1_uDir, member1_wDir)

            elif self.input["Member"]["Location"] == "Back to Back Web":
                member1OriginL = numpy.array([self.plate1.W - self.inline_weld1.L, -self.member1.B - self.plate1.T / 2, self.member1.D / 2])
                member1_uDir = numpy.array([0.0, -1.0, 0.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member1.place(member1OriginL, member1_uDir, member1_wDir)

                member2OriginL = numpy.array([self.member1.L + self.inline_weld1.L, self.member1.B + self.plate1.T / 2, self.member1.D / 2])
                member2_uDir = numpy.array([0.0, 1.0, 0.0])
                member2_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.member2.place(member2OriginL, member2_uDir, member2_wDir)

            else: # self.input["Member"]["Location"] == "Flange":
                member1OriginL = numpy.array([self.plate1.W - self.inline_weld1.L, - self.plate1.T / 2, self.member1.B / 2])
                member1_uDir = numpy.array([0.0, 0.0, 1.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member1.place(member1OriginL, member1_uDir, member1_wDir)

        if self.input["Member"]["SectionType"] == "Angles":
            if self.input["Member"]["Location"] == "Leg":
                member1OriginL = numpy.array([self.plate1.W - self.inline_weld1.L, - self.plate1.T / 2, 0.0])
                member1_uDir = numpy.array([0.0, 0.0, 1.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member1.place(member1OriginL, member1_uDir, member1_wDir)

            elif self.input["Member"]["Location"] == "Back to Back Angles":
                member1OriginL = numpy.array([self.plate1.W - self.inline_weld1.L, - self.plate1.T / 2, 0.0])
                member1_uDir = numpy.array([0.0, 0.0, 1.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member1.place(member1OriginL, member1_uDir, member1_wDir)

                member1OriginL = numpy.array([self.plate1.W/2 + self.member2.L,  self.plate1.T / 2, 0.0])
                member1_uDir = numpy.array([0.0, 0.0, 1.0])
                member1_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.member2.place(member1OriginL, member1_uDir, member1_wDir)

            else:  # self.input["Member"]["Location"] == "Star Angles":
                member1OriginL = numpy.array([self.plate1.W - self.inline_weld1.L, - self.plate1.T / 2, 0.0])
                member1_uDir = numpy.array([0.0, 0.0, 1.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member1.place(member1OriginL, member1_uDir, member1_wDir)

                member1OriginL = numpy.array([self.plate1.W/2 + self.member2.L,  self.plate1.T / 2, 0.0])
                member1_uDir = numpy.array([0.0, 0.0, -1.0])
                member1_wDir = numpy.array([1.0, 0.0, 0.0])
                self.member2.place(member1OriginL, member1_uDir, member1_wDir)

    def createweldGeometry(self):
        """

         :return: Geometric Orientation of this component
        """

        if self.input["Member"]["SectionType"] == "Channels":
            if self.input["Member"]["Location"] == "Web":
                member1weldOriginL = numpy.array([self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, 1.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2 , -self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, -1.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld2.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2 , self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, -1.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

            elif self.input["Member"]["Location"] == "Back to Back Web":
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, 1.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2, -self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, -1.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld2.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, -1.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                ###### weld on other side of the plate ########
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, self.plate1.T / 2, self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, 1.0, 0.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld11.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, self.plate1.T / 2, -self.member1.D / 2])
                member1weld_uDir = numpy.array([0.0, 1.0, 0.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld22.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, self.plate1.T / 2, self.member1.D / 2])
                member1weld_uDir = numpy.array([-1.0, 0.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld11.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

            else:  # self.input["Member"]["Location"] == "Flange":
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.B / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, 1.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2, -self.member1.B / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, -1.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld2.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.B / 2])
                member1weld_uDir = numpy.array([0.0, -1.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                ###### weld on other side of the plate ########
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2 -self.member1.D, self.member1.B / 2])
                member1weld_uDir = numpy.array([0.0, 1.0, 0.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld11.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2 -self.member1.D, -self.member1.B / 2])
                member1weld_uDir = numpy.array([0.0, 1.0, 0.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld22.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2 -self.member1.D, self.member1.B / 2])
                member1weld_uDir = numpy.array([-1.0, 0.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld11.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

        if self.input["Member"]["SectionType"] == "Angles":
            if self.input["Member"]["Location"] == "Leg":
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, 1.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2, -self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, -1.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld2.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, -1.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)
            elif self.input["Member"]["Location"] == "Back to Back Angles":
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, 1.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2, -self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, -1.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld2.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, -1.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)
            else:  # self.input["Member"]["Location"] == "Star Angles":
                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, 1.0])
                member1weld_wDir = numpy.array([1.0, 0.0, 0.0])
                self.inline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array([self.plate1.W, -self.plate1.T / 2, -self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, 0.0, -1.0])
                member1weld_wDir = numpy.array([-1.0, 0.0, 0.0])
                self.inline_weld2.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

                member1weldOriginL = numpy.array(
                    [self.plate1.W - self.inline_weld1.L, -self.plate1.T / 2, self.member1.A / 2])
                member1weld_uDir = numpy.array([0.0, -1.0, 0.0])
                member1weld_wDir = numpy.array([0.0, 0.0, -1.0])
                self.opline_weld1.place(member1weldOriginL, member1weld_uDir, member1weld_wDir)

    def get_models(self):

        if self.input["Member"]["SectionType"] == "Channels":
            if self.input["Member"]["Location"] == "Web":
                components = [self.plate1_Model, self.inline_weld1_Model, self.inline_weld2_Model, self.opline_weld1_Model, self.member1_Model]

            elif self.input["Member"]["Location"] == "Flange":
                components = [self.plate1_Model,self.plate2_Model, self.inline_weld1_Model, self.inline_weld2_Model,
                              self.opline_weld1_Model, self.inline_weld11_Model, self.inline_weld22_Model, self.opline_weld11_Model, self.member1_Model]

            else: #"Back to Back Web"
                components = [self.plate1_Model, self.inline_weld1_Model, self.inline_weld2_Model,
                              self.opline_weld1_Model,self.inline_weld11_Model, self.inline_weld22_Model, self.opline_weld11_Model, self.member1_Model, self.member2_Model]

        if self.input["Member"]["SectionType"] == "Angles":
            if self.input["Member"]["Location"] == "Leg":
                components = [self.plate1_Model, self.inline_weld1_Model, self.inline_weld2_Model,
                              self.opline_weld1_Model, self.member1_Model]

            elif self.input["Member"]["Location"] == "Back to Back Angles":
                components = [self.plate1_Model, self.inline_weld1_Model, self.inline_weld2_Model,
                              self.opline_weld1_Model, self.member1_Model, self.member2_Model]

            else:  # self.input["Member"]["Location"] == "Star Angles":
                components = [self.plate1_Model, self.inline_weld1_Model, self.inline_weld2_Model,
                              self.opline_weld1_Model, self.member1_Model, self.member2_Model]

        CAD = components[0]
        for comp in components[1:]:
            CAD = BRepAlgoAPI_Fuse(CAD, comp).Shape()

        return CAD
