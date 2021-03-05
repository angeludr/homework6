import numpy as np
import time

def ellipseArea(a = None, b = None):
    """Returns area of ellipse"""
    return a * b * np.pi
    
def integralEllipse(x):
    """Returns the integral of ellipse"""
    # Multiply by 4 to get all quadrants of ellipse
    return 4 * (b * ((1 - x**2 / a**2)**(0.5)))

def trapezoidal(f, a = None, b = None, n = None):
    """Returns calculated area of ellipse using trapezoidal sum"""
    
    h = (b - a) / n
    
    s = 0
    
    for n in np.arange(n):
        s += 0.5 * (f(a + n * h) + f(a + (n + 1) * h))

    return s * h

if __name__ == "__main__":
    
    print('\n')

    a = 2.0
    b = 4.0
    
    true = ellipseArea(a, b)
    
    print('True area of ellipse when a =', a,' and b =', b,' is equal to', true)

    trap = trapezoidal(integralEllipse, 0.0, a, 1000) # Step size (n) is large to give an accurate integration
    print('Calculated area using trapezoidal rule:', trap, '\n\n')
    
    h = 0.001
   
    x = np.arange(-2.0, 2.0, h)
    y = np.arange(-4.0, 4.0, h)
    
    xs, ys = np.meshgrid(x, y)

    masked_integral = 0

    mask = 2.0 * (xs**2 + ys**2 <= 4)
    dx = h
    dy = h
    masked_integral = np.sum(mask * dx * dy)
    print('The value of the masked integral is', masked_integral)
    
    t = time.time()
    t1 = time.time()
    total = t1 - t
    print('Time elasped:', total)
