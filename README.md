# Clock
A graphical clock in Python 3.x using the Pygame library.

I have included the ability to customise the radius of the clock, the centre point, and the size of the surface.

# Maths
I calculate the coordinates of the circumference of the circle using these equations:
- x = cx + r * cos(theta)
- y = cy + r * sin(theta)

where (cx,cy) is the centre point of the circle, r is the radius, and theta is the angle in [radians](https://en.wikipedia.org/wiki/Radian).\
Note that radians=0 begins at the rightmost point on the circle.

Refer to this [wikipedia article](http://en.wikipedia.org/wiki/Circle#Equations) for more information on Parametric equations.

# Requirements
I am using the [Python 3.7](https://www.python.org/downloads/release/python-370/) IDLE.\
Python 3.x and Pygame 1.7.x or above is required.\
You can download pygame either [here](https://www.pygame.org/download.shtml), [here](https://bitbucket.org/pygame/pygame/downloads/) or [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame).
