import math

L1 = 8.0
L2 = 16.6  # Length of link 2
L3 = 20.8  # Length of link 3

STEPPER_LIMIT = (0, 360)
SERVO1_LIMIT = (0, 180)
SERVO2_LIMIT = (0, 180)

def forward_kinematics(theta1_deg, theta2_deg, theta3_deg):
    theta1 = math.radians(theta1_deg)
    theta2 = math.radians(theta2_deg)
    theta3 = math.radians(theta3_deg)

    z = L1  + L2 * math.sin(theta2) + L3 * math.sin( theta2 + theta3)
    r2 = z-L1
    r3_sq = L2**2 + L3**2 + 2*L2*L3*math.cos(theta3)
    x = math.sqrt(r3_sq-r2**2)*math.cos(theta1)
    y = x*math.tan(theta1)
    
    x=round(x,1)
    y=round(y,1)
    z=round(z,1)

    return x, y, z


def inverse_kinematics(x, y, z):
    r1 = math.sqrt(x ** 2 + y ** 2)
    r2 = z - L1
    r3 = math.sqrt(r1 ** 2 + r2 ** 2)

    if r1 > L2 + L3:
        print("Target out of reach")
        return None

    theta1 = math.atan2(y, x)

    cos_theta3 = (r3 ** 2 - L2 ** 2 - L3 ** 2) / (2 * L2 * L3)
    theta3 = math.acos(round(cos_theta3, 3))

    gamma = math.atan2(r2, r1)
    beta = math.acos(round((L3 ** 2 - L2 ** 2 - r3 ** 2) / (-2 * L2 * r3), 3))
    theta2 = gamma - beta

    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)
    theta3_deg = math.degrees(theta3)

    return theta1_deg, theta2_deg, theta3_deg


def linear_interpolation(start, end, steps):

    start_x,start_y,start_z = start
    end_x,end_y,end_z = end

    start_angles = inverse_kinematics(start_x, start_y, start_z)
    end_angles = inverse_kinematics(end_x, end_y, end_z)

    delta_path = [(end[i] - start[i]) / steps for i in range(len(start))]

    delta_ang = [(end_angles[i] - start_angles[i]) / steps for i in range(len(start))]

    path = [start]
    ang_list = [start_angles]
    for i in range(1, steps + 1):
        point = [start[j] + delta_path[j] * i for j in range(len(start))]
        path.append(point)

        angle = [start_angles[j] + delta_ang[j] * i for j in range(len(start))]
        ang_list.append(angle)

    return path,ang_list

def main():
    # Example usage
    start_x = float(input("Enter start x-coordinate: "))
    start_y = float(input("Enter start y-coordinate: "))
    start_z = float(input("Enter start z-coordinate: "))
    end_x = float(input("Enter end x-coordinate: "))
    end_y = float(input("Enter end y-coordinate: "))
    end_z = float(input("Enter end z-coordinate: "))

    start = tuple([start_x,start_y,start_z])
    end = tuple([end_x,end_y,end_z])

    steps = int(input("Enter the no. of steps for path gen :"))
    if start and end:
        path,ang_list = linear_interpolation(start,end, steps=steps)
        print("Joint angles for linear path:")
        for i in range(steps+1):
            print(path[i])
            print(ang_list[i])
            
            
            #print(forward_kinematics(point[0],point[1],point[2]))

'''

def main():
    x = float(input("Enter  x-coordinate: "))
    y = float(input("Enter  y-coordinate: "))
    z = float(input("Enter  z-coordinate: "))
    t1,t2,t3 = inverse_kinematics(x,y,z)
    print(t1,t2,t3)

    x1,y1,z1 = forward_kinematics(t1,t2,t3)
    print(x1,y1,z1)

'''
if __name__ == "__main__":
    main()
