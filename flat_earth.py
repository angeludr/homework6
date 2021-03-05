import numpy as np

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m = mass
        returns a vector of the gravitational acceleration"""
    G = 6.6742e-11
    dist = p2 - p1
    r = np.linalg.norm(dist)
    rhat = (p2 - p1) / r
    return -1 * G * m / r**2 * rhat

def point_in_sphere(x, y, z, radius = None):
    if x**2 + y**2 + z**2 < radius**2:
        return True
    else:
        return False
        
if __name__ == "__main__":

    km = 1000 # 1 km = 1000 meters
    rho = 5514 # kg/m^3, density of Earth
    r_earth = 20037*km # Radius of flat Earth
    h = 500.0*km # Relatively coarse step size
    
    # Set grid size same in x, y, z
    dx, dy, dz = h, h, h
    dV = dx * dy * dz
    
    # x, y, z define boundaries of grid
    x = np.arange(-20500*km, 20500*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = y.copy()
    
    # Define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 20037*km, 4750*km])
    point_equator   = np.array([0, 10018.5*km, 4750*km])
    point_edge = np.array([0, 10018.5*km, 0])
    
    # North Pole calculation
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        # Lil trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx, yy, zz, r_earth):
                    m = rho * dV # Mass density
                    point = np.array([xx, yy, zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    print('The gravity vector at the north pole is', grav_vec_northpole, '\n')

    # Equator calculation
    grav_vec_equator = 0
    for idx, xx in enumerate(x):
        # Lil trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx, yy, zz, r_earth):
                    m = rho * dV # Mass density
                    point = np.array([xx, yy, zz])
                    grav_vec_equator += grav_accel(point, point_equator, m)
    print('The gravity vector at the equator is', grav_vec_equator, '\n')
    
    # Edge calculation
    grav_vec_edge = 0
    for idx, xx in enumerate(x):
        # Lil trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx, yy, zz, r_earth):
                    m = rho * dV # Mass density
                    point = np.array([xx, yy, zz])
                    grav_vec_edge += grav_accel(point, point_edge, m)
    print('The gravity vector at the edge is', grav_vec_edge, '\n')
