import math
import numpy as np

# DH parameters
L1 = 8.0   # Length of link 1
L2 = 16.6  # Length of link 2
L3 = 20.8

def dh_matrix(alpha, a, d, theta):

    ct = np.cos(theta)
    st = np.sin(theta)
    ca = np.cos(alpha)
    sa = np.sin(alpha)
    
    A = np.array([[ct, -st*ca, st*sa, a*ct],
                  [st, ct*ca, -ct*sa, a*st],
                  [0, sa, ca, d],
                  [0, 0, 0, 1]])
    return A

def forward_kinematics(dh_params):
  
    T = np.eye(4)
    for alpha, a, d, theta in dh_params:
        A = dh_matrix(alpha, a, d, theta)
        T = np.dot(T, A)
    return T

def inverse_kinematics(dh_params, target_pose):
    
    joint_angles = []
    for i in range(len(dh_params)):
        alpha, a, d, theta = dh_params[i]
        
        T = np.eye(4)
        for j in range(i):
            alpha_j, a_j, d_j, theta_j = dh_params[j]
            A = dh_matrix(alpha_j, a_j, d_j, theta_j)
            T = np.dot(T, A)
        
        T_inv = np.linalg.inv(T)
        target_pose_joint = np.dot(T_inv, target_pose)
        
        if i == 0:
            theta_i_new = np.arctan2(target_pose_joint[1, 3], target_pose_joint[0, 3])
        elif i == 1:
            r = np.sqrt(target_pose_joint[0, 3]**2 + target_pose_joint[1, 3]**2)
            z = target_pose_joint[2, 3] - dh_params[1][2]
            theta_i_new = np.arctan2(z, r)
        else:
            r = np.sqrt(target_pose_joint[0, 3]**2 + target_pose_joint[1, 3]**2)
            z = target_pose_joint[2, 3] - dh_params[1][2]
            cos_theta = (r**2 + z**2 - dh_params[1][1]**2 - dh_params[2][1]**2) / (2 * dh_params[1][1] * dh_params[2][1])
            theta_i_new = np.arccos(cos_theta)
        
        joint_angles.append(theta_i_new)
    
    return joint_angles


dh_params = [
    (0, 0, 0, 0),          
    (np.pi/2, 0, L1, 0),  
    (0, L2, 0, 0)]      


