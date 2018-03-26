import numpy as np
from termcolor import colored
import sys
sys.path.append(r'../build/x64/Release')
import NumC

####################################################################################
def doTest():
    print(colored('Testing Rotations Module', 'magenta'))

    print(colored('Testing Quaternion', 'magenta'))

    print(colored('Testing Default Constructor', 'cyan'))
    NumC.Quaternion()
    print(colored('\tPASS', 'green'))

    print(colored('Testing Value Constructor', 'cyan'))
    quat = np.random.randint(1,10, [4,])
    unitQuat = quat / np.linalg.norm(quat)
    quat = NumC.Quaternion(quat[0].item(), quat[1].item(), quat[2].item(), quat[3].item())
    if (quat.i() == unitQuat[0].item() and
        quat.j() == unitQuat[1].item() and
        quat.k() == unitQuat[2].item() and
        quat.s() == unitQuat[3].item()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Array Constructor', 'cyan'))
    quat = np.random.randint(1,10, [4,])
    unitQuat = quat / np.linalg.norm(quat)
    cArray = NumC.NdArray(1, 4)
    cArray.setArray(quat)
    quat = NumC.Quaternion(cArray)
    if (quat.i() == unitQuat[0].item() and
        quat.j() == unitQuat[1].item() and
        quat.k() == unitQuat[2].item() and
        quat.s() == unitQuat[3].item()):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing angleAxisRotation', 'cyan'))
    axis = np.random.randint(1,10, [3,])
    angle = np.random.rand(1).item() * np.pi
    cAxis = NumC.NdArray(1, 3)
    cAxis.setArray(axis)
    if np.array_equal(np.round(NumC.Quaternion.angleAxisRotation(cAxis, angle).toNdArray().getNumpyArray().flatten(), 10),
                      np.round(quatRotateAngleAxis(axis, angle), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    # print(colored('Testing angularVelocity', 'cyan'))
    # time = np.abs(np.random.randn(1) * 5).item()
    # x1 = np.random.rand(3, 1).flatten()
    # x1 = x1 / np.linalg.norm(x1)
    # x2 = np.random.rand(3, 1).flatten()
    # x2 = x2 / np.linalg.norm(x2)
    #
    # theta0 = np.random.rand(1).item() * 2 * np.pi
    # theta = np.arccos(np.dot(x1, x2))
    # theta1 = theta0 + theta
    # cross = np.cross(x1, x2)
    # cross = cross / np.linalg.norm(cross)
    # cCross = NumC.NdArray(3, 1)
    # cCross.setArray(cross)
    #
    # q0 = np.asarray([cross[0] * np.sin(theta0 / 2), cross[1] * np.sin(theta0 / 2), cross[2] * np.sin(theta0 / 2), np.cos(theta0 / 2)])
    # q1 = np.asarray([cross[0] * np.sin(theta1 / 2), cross[1] * np.sin(theta1 / 2), cross[2] * np.sin(theta1 / 2), np.cos(theta1 / 2)])
    # quat0 = NumC.Quaternion(q0[0], q0[1], q0[2], q0[3])
    # quat1 = NumC.Quaternion(q1[0], q1[1], q1[2], q1[3])
    # crossTo = quat0.rotate(cCross).getNumpyArray().flatten()
    #
    # w = quat0.angularVelocity(quat1, time).getNumpyArray().flatten()
    # angularVelocity = np.linalg.norm(w)
    # axis = w / angularVelocity
    #
    # if (np.round(angularVelocity * time - theta, 1) == 0 and # round to 1 decimal place because C is an approximation on magnitude
    #     np.all(np.round(axis, 10) == np.round(crossTo, 10))):
    #     print(colored('\tPASS', 'green'))
    # else:
    #     print(colored('\tFAIL', 'red'))

    print(colored('Testing conjugate', 'cyan'))
    quat = np.random.randint(1,10, [4,])
    unitQuat = quat / np.linalg.norm(quat)
    cArray = NumC.NdArray(1, 4)
    cArray.setArray(quat)
    quat = NumC.Quaternion(cArray)
    conjQuat = quat.conjugate()
    if (np.round(conjQuat.i(), 10) == np.round(-unitQuat[0].item(), 10) and
        np.round(conjQuat.j(), 10) == np.round(-unitQuat[1].item(), 10) and
        np.round(conjQuat.k(), 10) == np.round(-unitQuat[2].item(), 10) and
        np.round(conjQuat.s(), 10) == np.round(unitQuat[3].item(), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing fromDCM', 'cyan'))
    quat = np.random.randint(1, 5, [4, ])
    cQuat = NumC.Quaternion(quat[0].item(), quat[1].item(), quat[2].item(), quat[3].item())
    dcm = cQuat.toDCM()
    cArray = NumC.NdArray(3)
    cArray.setArray(dcm)
    if np.array_equal(np.round(NumC.Quaternion.fromDCM(cArray).toNdArray().getNumpyArray().flatten(), 10), quat):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing identity', 'cyan'))
    quat = NumC.Quaternion.identity()
    if quat.i() == 0 and quat.j() == 0 and quat.k() == 0 and quat.s() == 1:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing inverse', 'cyan'))
    quat = np.random.randint(1,10, [4,])
    unitQuat = quat / np.linalg.norm(quat)
    cArray = NumC.NdArray(1, 4)
    cArray.setArray(quat)
    quat = NumC.Quaternion(cArray)
    conjQuat = quat.inverse()
    if (np.round(conjQuat.i(), 10) == np.round(-unitQuat[0].item(), 10) and
        np.round(conjQuat.j(), 10) == np.round(-unitQuat[1].item(), 10) and
        np.round(conjQuat.k(), 10) == np.round(-unitQuat[2].item(), 10) and
        np.round(conjQuat.s(), 10) == np.round(unitQuat[3].item(), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing nlerp', 'cyan'))
    myQuat1 = np.random.randint(1, 5, [4, ])
    myQuat2 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(myQuat1[0].item(), myQuat1[1].item(), myQuat1[2].item(), myQuat1[3].item())
    cQuat2 = NumC.Quaternion(myQuat2[0].item(), myQuat2[1].item(), myQuat2[2].item(), myQuat2[3].item())
    t = np.random.rand(1).item()
    interpQuat = cQuat1.nlerp(cQuat2, t).flatten()
    if np.array_equal(np.round(interpQuat, 10), np.round(nlerp(myQuat1, myQuat2, t), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing print', 'cyan'))
    cQuat1.print()
    print(colored('\tPASS', 'green'))

    # print(colored('Testing rotate', 'cyan'))
    # vec = np.random.rand(3, 1) * 10
    # vec = vec.flatten()
    # cVec = NumC.NdArray(1, 3)
    # cVec.setArray(cVec)
    # newVec = myQuat.rotate(vec)
    # newVecPy = np.asarray(np.matrix(myQuat.getDCM()) * np.matrix(vec).T)
    # if np.array_equal(np.round(newVec, 10), np.round(newVecPy, 10)):
    #     print(colored('\tPASS', 'green'))
    # else:
    #     print(colored('\tFAIL', 'red'))

    # print(colored('Testing slerp', 'cyan'))
    # myQuat1 = np.random.randint(1, 5, [4, ])
    # myQuat2 = np.random.randint(1, 5, [4, ])
    # cQuat1 = NumC.Quaternion(myQuat1[0].item(), myQuat1[1].item(), myQuat1[2].item(), myQuat1[3].item())
    # cQuat2 = NumC.Quaternion(myQuat2[0].item(), myQuat2[1].item(), myQuat2[2].item(), myQuat2[3].item())
    # t = np.random.rand(1).item()
    # interpQuat = cQuat1.slerp(cQuat2, t).flatten()
    # if np.array_equal(np.round(interpQuat, 10), np.round(slerp(myQuat1, myQuat2, t), 10)):
    #     print(colored('\tPASS', 'green'))
    # else:
    #     print(colored('\tFAIL', 'red'))

    print(colored('Testing toDCM', 'cyan'))
    quat = np.random.randint(1, 5, [4, ])
    unitQuat = quat / quatNorm(quat)
    cQuat = NumC.Quaternion(quat[0].item(), quat[1].item(), quat[2].item(), quat[3].item())
    dcmPy = quat2dcm(unitQuat)
    dcm = cQuat.toDCM()
    if np.array_equal(np.round(dcm, 10), np.round(dcmPy, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing X Rotation', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    quat = NumC.Quaternion.xRotation(radians.item()).toNdArray().getNumpyArray().flatten()
    if np.array_equal(np.round(quat, 10), np.round(quatRotateX(radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Y Rotation', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    quat = NumC.Quaternion.yRotation(radians.item()).toNdArray().getNumpyArray().flatten()
    if np.array_equal(np.round(quat, 10), np.round(quatRotateY(radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing Z Rotation', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    quat = NumC.Quaternion.zRotation(radians.item()).toNdArray().getNumpyArray().flatten()
    if np.array_equal(np.round(quat, 10), np.round(quatRotateZ(radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing ==', 'cyan'))
    quat1 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    cQuat2 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    if cQuat1 == cQuat2:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing !=', 'cyan'))
    quat1 = np.random.randint(1, 5, [4, ])
    quat2 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    cQuat2 = NumC.Quaternion(quat2[0].item(), quat2[1].item(), quat2[2].item(), quat2[3].item())
    if cQuat1 != cQuat2:
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing addition', 'cyan'))
    quat1 = np.random.randint(1, 5, [4, ])
    quat2 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    cQuat2 = NumC.Quaternion(quat2[0].item(), quat2[1].item(), quat2[2].item(), quat2[3].item())
    resPy = quatAdd(quat1, quat2)
    res = cQuat1 + cQuat2
    if np.array_equal(np.round(res.toNdArray().getNumpyArray().flatten(), 10), np.round(resPy, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing subtraction', 'cyan'))
    quat1 = np.random.randint(1, 5, [4, ])
    quat2 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    cQuat2 = NumC.Quaternion(quat2[0].item(), quat2[1].item(), quat2[2].item(), quat2[3].item())
    resPy = quatSub(quat1, quat2)
    res = cQuat1 - cQuat2
    if np.array_equal(np.round(res.toNdArray().getNumpyArray().flatten(), 10), np.round(resPy, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing muliplication: Scalar', 'cyan'))
    quat = np.random.randint(1, 5, [4, ])
    cQuat = NumC.Quaternion(quat[0].item(), quat[1].item(), quat[2].item(), quat[3].item())
    res = cQuat * -1
    if np.array_equal(np.round(res.flatten(), 10), np.round(-resPy, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing muliplication: Quaternion', 'cyan'))
    quat1 = np.random.randint(1, 5, [4, ])
    quat2 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    cQuat2 = NumC.Quaternion(quat2[0].item(), quat2[1].item(), quat2[2].item(), quat2[3].item())
    resPy = quatMult(quat1, quat2)
    res = cQuat1 * cQuat2
    if np.array_equal(np.round(res.flatten(), 10), np.round(resPy, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    # print(colored('Testing muliplication: Array', 'cyan'))
    # quat = np.random.randint(1, 5, [4, ])
    # cQuat = NumC.Quaternion(quat[0].item(), quat[1].item(), quat[2].item(), quat[3].item())
    # array = np.random.randint(1, 5, [3, ])
    # cArray = NumC.NdArray(3, 1)
    # cArray.setArray(array)
    # res = cQuat * cArray
    # if np.array_equal(np.round(res.flatten(), 10), np.round(-resPy, 10)):
    #     print(colored('\tPASS', 'green'))
    # else:
    #     print(colored('\tFAIL', 'red'))

    print(colored('Testing division', 'cyan'))
    quat1 = np.random.randint(1, 5, [4, ])
    quat2 = np.random.randint(1, 5, [4, ])
    cQuat1 = NumC.Quaternion(quat1[0].item(), quat1[1].item(), quat1[2].item(), quat1[3].item())
    cQuat2 = NumC.Quaternion(quat2[0].item(), quat2[1].item(), quat2[2].item(), quat2[3].item())
    resPy = quatDiv(quat1, quat2)
    res = cQuat1 / cQuat2
    if np.array_equal(np.round(res.toNdArray().getNumpyArray().flatten(), 10), np.round(resPy, 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing DCM', 'magenta'))

    print(colored('Testing angleAxisRotationDCM', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    axis = np.random.rand(3)
    cAxis = NumC.NdArray(1, 3)
    cAxis.setArray(axis)
    rot = NumC.angleAxisRotationDCM(cAxis, radians.item()).getNumpyArray()
    if np.all(np.round(rot, 10) == np.round(angleAxisRotation(axis, radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing isValidDCM', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    rot = NumC.xRotationDCM(radians.item()).getNumpyArray()
    cArray = NumC.NdArray(3)
    cArray.setArray(rot)
    if NumC.isValidDCM(cArray):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing xRotationDCM', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    rot = NumC.xRotationDCM(radians.item()).getNumpyArray()
    if np.all(np.round(rot, 10) == np.round(rotateX(radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing yRotationDCM', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    rot = NumC.yRotationDCM(radians.item()).getNumpyArray()
    if np.all(np.round(rot, 10) == np.round(rotateY(radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

    print(colored('Testing zRotationDCM', 'cyan'))
    radians = np.random.rand(1) * 2 * np.pi
    rot = NumC.zRotationDCM(radians.item()).getNumpyArray()
    if np.all(np.round(rot, 10) == np.round(rotateZ(radians.item()), 10)):
        print(colored('\tPASS', 'green'))
    else:
        print(colored('\tFAIL', 'red'))

########################################################################################################################
def quatNorm(quat):
    return np.linalg.norm(quat)

########################################################################################################################
def dcm2quat(dcm):
    # http://www.vectornav.com/docs/default-source/documentation/vn-100-documentation/AN002.pdf?sfvrsn=19ee6b9_10

    q3 = 0.5 * np.sqrt(dcm[0, 0] + dcm[1, 1] + dcm[2, 2] + 1)
    q0 = (dcm[1, 2] - dcm[2, 1]) / (4 * q3)
    q1 = (dcm[2, 0] - dcm[0, 2]) / (4 * q3)
    q2 = (dcm[0, 1] - dcm[1, 0]) / (4 * q3)

    quat = np.asarray([q0, q1, q2, q3])
    quat = quat / np.linalg.norm(quat)

    return quat

########################################################################################################################
def quat2dcm(quat):
    # http://www.vectornav.com/docs/default-source/documentation/vn-100-documentation/AN002.pdf?sfvrsn=19ee6b9_10

    q0 = quat[0]
    q1 = quat[1]
    q2 = quat[2]
    q3 = quat[3]

    dcm = np.zeros([3, 3])
    dcm[0, 0] = q3**2 + q0**2 - q1**2 - q2**2
    dcm[0, 1] = 2 * (q0 * q1 + q3 * q2)
    dcm[0, 2] = 2 * (q0 * q2 - q3 * q1)
    dcm[1, 0] = 2 * (q0 * q1 - q3 * q2)
    dcm[1, 1] = q3**2 - q0**2 + q1**2 - q2**2
    dcm[1, 2] = 2 * (q1 * q2 + q3 * q0)
    dcm[2, 0] = 2 * (q0 * q2 + q3 * q1)
    dcm[2, 1] = 2 * (q1 * q2 - q3 * q0)
    dcm[2, 2] = q3**2 - q0**2 - q1**2 + q2**2

    return dcm

########################################################################################################################
def quatAdd(quat1, quat2):
    quat = quat1 / quatNorm(quat1) + quat2 / quatNorm(quat2)
    return quat / np.linalg.norm(quat)

########################################################################################################################
def quatSub(quat1, quat2):
    quat = quat1 / quatNorm(quat1) - quat2 / quatNorm(quat2)
    return quat / np.linalg.norm(quat)

########################################################################################################################
def quatMult(quat1, quat2):
    q0 = quat2[3] * quat1[0] + quat2[0] * quat1[3] - quat2[1] * quat1[2] + quat2[2] * quat1[1]
    q1 = quat2[3] * quat1[1] + quat2[0] * quat1[2] + quat2[1] * quat1[3] - quat2[2] * quat1[0]
    q2 = quat2[3] * quat1[2] - quat2[0] * quat1[1] + quat2[1] * quat1[0] + quat2[2] * quat1[3]
    q3 = quat2[3] * quat1[3] - quat2[0] * quat1[0] - quat2[1] * quat1[1] - quat2[2] * quat1[2]

    quat =  np.asarray([q0, q1, q2, q3])
    return quat / quatNorm(quat)

########################################################################################################################
def quatDiv(quat1, quat2):
    q0 = quat2[3] * quat1[0] - quat2[0] * quat1[3] - quat2[1] * quat1[2] + quat2[2] * quat1[1]
    q1 = quat2[3] * quat1[1] + quat2[0] * quat1[2] - quat2[1] * quat1[3] - quat2[2] * quat1[0]
    q2 = quat2[3] * quat1[2] - quat2[0] * quat1[1] + quat2[1] * quat1[0] - quat2[2] * quat1[3]
    q3 = quat2[3] * quat1[3] + quat2[0] * quat1[0] + quat2[1] * quat1[1] + quat2[2] * quat1[2]

    quat = np.asarray([q0, q1, q2, q3])
    return quat / quatNorm(quat)

########################################################################################################################
def nlerp(quat1, quat2, inT):
    quat1 = quat1 / np.linalg.norm(quat1)
    quat2 = quat2 / np.linalg.norm(quat2)

    oneMinusT = 1 - inT

    outQuat = np.zeros([4,])

    outQuat[0] = oneMinusT * quat1[0] + inT * quat2[0]
    outQuat[1] = oneMinusT * quat1[1] + inT * quat2[1]
    outQuat[2] = oneMinusT * quat1[2] + inT * quat2[2]
    outQuat[3] = oneMinusT * quat1[3] + inT * quat2[3]

    outQuat = outQuat / np.linalg.norm(outQuat)

    return outQuat

########################################################################################################################
def quatRotateAngleAxis(axis, radians):
    axis = axis / np.linalg.norm(axis)
    halfRadians = radians / 2
    quat = np.asarray([axis[0] * np.sin(halfRadians), axis[1] * np.sin(halfRadians), axis[2] * np.sin(halfRadians), np.cos(halfRadians)])
    return quat / np.linalg.norm(quat)

########################################################################################################################
def quatRotateX(radians):
    return quatRotateAngleAxis([1,0,0], radians)

########################################################################################################################
def quatRotateY(radians):
    return quatRotateAngleAxis([0,1,0], radians)

########################################################################################################################
def quatRotateZ(radians):
    return quatRotateAngleAxis([0,0,1], radians)

########################################################################################################################
def angleAxisRotation(axis, radians):
    return quat2dcm(quatRotateAngleAxis(axis, radians))

########################################################################################################################
def rotateX(radians):
    return np.matrix([[1, 0, 0],[0, np.cos(radians), np.sin(radians)],[0, -np.sin(radians), np.cos(radians)]])

########################################################################################################################
def rotateY(radians):
    return np.matrix([[np.cos(radians), 0, -np.sin(radians)],[0, 1, 0],[np.sin(radians), 0, np.cos(radians)]])

########################################################################################################################
def rotateZ(radians):
    return np.matrix([[np.cos(radians), np.sin(radians), 0],[-np.sin(radians), np.cos(radians), 0],[0, 0, 1]])

####################################################################################
if __name__ == '__main__':
    doTest()





