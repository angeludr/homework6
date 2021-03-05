import numpy as np

def grav_accel(p1, p2, m):
    """ p1 = point where the mass element is
        p2 = point you are interested in
        m  = mass
        returns a vector of the gravitational accleration"""
    G = 6.6743e-11
    dist = p2 - p1
    r = np.linalg.norm(dist)
    rhat = dist / r
    return -1 * G * m / r**2 * rhat

def point_in_sphere(x, y, z, radius = None):
    if x**2 + y**2 + z**2 < radius**2:
        return True
    else:
        return False

if __name__ == "__main__":
    
    km = 1000 # 1 km = 1000 meters
    rho = 5514 # kg/m^3, density of Earth
    r_earth = 6378*km # Radius of globe Earth
    h = 200.0*km # Relatively coarse step size
    
    # Set grid size same in x, y, z
    dx, dy, dz = h, h, h
    dV = dx * dy * dz
    
    # x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-7000*km, 7000*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = y.copy()
    
    # Define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 0, 6378*km])
    point_equator   = np.array([0, 6378*km, 0])
    point_southpole = np.array([0, 0, -6378*km])
    
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
    ## print("Should be something like [0,0,-9.8] m/s^2")

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
    
    # South Pole calculation
    grav_vec_southpole = 0
    for idx, xx in enumerate(x):
        # Lil trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx, yy, zz, r_earth):
                    m = rho * dV # Mass density
                    point = np.array([xx, yy, zz])
                    grav_vec_southpole += grav_accel(point, point_southpole, m)
    print('The gravity vector at the south pole is', grav_vec_southpole, '\n')
