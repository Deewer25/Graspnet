from scipy.spatial.transform import Rotation as R
import numpy as np

# SAVE
# env.step([-4.60506905e-01, -2.56650779e-03,  3.00172571e-01, -7.37274265e-01,-6.75593483e-01, -3.12981209e-04,  8.20630291e-05, 0, 0])



#rot0 = R.from_quat([0.743, 0.664, 0.055, 0.060]).as_matrix()

rot0 = R.from_quat([0.761, -0.042, -0.646, -0.037]).as_matrix()
t0 = np.array([-0.588, 0.005, 0.429])

res0 = np.eye(4)



res0[:3, :3] = rot0
res0[:3, -1] = t0

#res0 = np.linalg.inv(res0)

print(res0)


t1 = np.array([-0.04553223,  0.09716797,  0.35888672])
rot1 = np.array(
    [[ 0.07559296, -0.96571505, -0.24835478],
     [ 0.28120205,  0.2596043,  -0.9238674 ],
     [ 0.95666665,  0.       ,   0.29118532]])

res1 = np.eye(4)




res1[:3, :3] = rot1
res1[:3, -1] = t1

#res1 = np.linalg.inv(res1)

print(res1)



rot_x = np.array(
    [[ 0, 0, 0.],
     [ 0,  -1, 0. ],
     [ 0,  0. , -1]])

res_x = np.eye(4)
res_x[:3, :3] = rot_x


RES = np.matmul(res_x,res0)
RES = np.matmul(res1,RES)

Rot = RES[:3,:3]
trans = RES[:3, -1]

quat = R.from_matrix(Rot).as_quat()
#print(np.concatenate([trans, quat]))
print(trans)
print(quat)


