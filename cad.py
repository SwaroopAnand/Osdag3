import sdxf
import numpy as np

# ================ Connecting Plate ==================

# darshan

"""	
defining co-ordinates of Connecting plate in front view
right of origin is considered as +ve X axis
downward to the origin is considered as +ve Y axis
"""
#
# ptP1x =0
# # ptP1y = ptA1y + self.data_object.column_length_L1 / 2 - self.data_object.beam_depth_D2 / 2 - self.data_object.end_dist - self.data_object.Lv
# ptP1y =0
# P1 = np.array([ptP1x, ptP1y,0])
#
# ptP2x =200
# ptP2y =0
# P2 = np.array([ptP2x, ptP2y,0])
#
# ptP3x = 200
# ptP3y = 400
# P3 = np.array([ptP3x, ptP3y,0])
#
# ptP4x = 0
# ptP4y = 400
# P4 = np.array([ptP4x, ptP4y,0])

d=sdxf.Drawing()

#set the color of the text layer to green
d.layers.append(sdxf.Layer(name="textlayer",color=3))

#add drawing elements
d.append(sdxf.PolyLine(points=[((0,0,0),(0,200,0),(200,200,0),(200,0,0))],layer="drawinglayer"))

d.saveas('hello_world.dxf')