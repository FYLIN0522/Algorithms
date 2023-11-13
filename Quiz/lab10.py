##"""Demo of the generic python code runner pseudo-question"""
##import matplotlib.pyplot as plt
##from graphviz import Graph
##
### First some simple text output.
##vertices = [(0, 0), (100, 0), (1, 50), (100, 100), (0, 100), (0,0)]
##vx, vy = zip(*vertices)  # Unpack them
##points = [(1, 1), (20, 20), (20, 80), (60, 50),
##     (97, 1), (1, 48), (1, 52), (97, 99), (1, 99)]
##px, py = zip(*points) # Unpack
##print("Vertex x values:", vx)
##print("Vertex y values:", vy)
##print("Point x values:", px)
##print("Point y values:", py)
##
### Now a matplotlib graph.
##axes = plt.axes()
##axes.plot(vx, vy, color='blue', marker='o', linestyle='--')
##axes.plot(px, py, color='red', marker='x', linestyle='')
##axes.set_title('The example from the geometry lecture notes')
##
### Lastly a graphviz example
##g = Graph()
##g.node('Root', '23')
##g.node('Leaf1', '13', shape='box')
##g.node('Leaf2', '99', shape='box')
##g.edge('Root', 'Leaf1')
##g.edge('Root', 'Leaf2')
##g.render('graph', format='png', view=False)





class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)



        
        
##def signed_area(a, b, c):
##    """Twice the area of the triangle abc.
##       Positive if abc are in counter clockwise order.
##       Zero if a, b, c are colinear.
##       Otherwise negative.
##    """
##    p = b - a
##    q = c - a
##    return p.x * q.y - q.x * p.y

##def is_on_segment(p, a, b):
####    print(p.lensq(), a.lensq() - b.lensq())
##    area = signed_area(p, a, b)
##    if area == 0:
##        if (a - p).lensq() <= (b - a).lensq() and (b - p).lensq() <= (b - a).lensq():  # ** FIXME **
##            return True
##    return False





def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0

##def classify_points(line_start, line_end, points):
##    left = []
##    right = []
##    for point in points:
##        check = is_ccw(line_start, line_end, point)
##        if check is True:
##            left.append(point)
##        elif check is False:
##            right.append(point)
##
##    return (len(right), len(left))




##def intersecting(a, b, c, d):
##    return is_ccw(a, d, b) != is_ccw(a, c, b) \
##           and is_ccw(c, a, d) != is_ccw(c, b, d)




##def is_strictly_convex(vertices):
####    for vertex in vertices:
##    vertices.append(vertices[0])
##    vertices.append(vertices[1])
##
##    i = 0
##    while i < len(vertices) - 2:
##        if is_ccw(vertices[i], vertices[i+1], vertices[i+2]) is False:
##            return False
##        i += 1
##    return True




def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate is None or is_ccw(hull[-1], p, candidate):  # ** FIXME **
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull


##import matplotlib.pyplot as plt
##def plot_hull(points, hull):
##    """Plot the given set of points and the computed convex hull"""
##    plt.scatter([p.x for p in points], [p.y for p in points])
##    plt.plot([v.x for v in hull + [hull[0]]], [v.y for v in hull + [hull[0]]])
##    plt.show()




class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0



##import matplotlib.pyplot as plt
##def plot_poly(points):
##    """Plot the given set of points as a closed polygon"""
##    plt.plot([v.x for v in points + [points[0]]], [v.y for v in points + [points[0]]])
##    plt.show()



def simple_polygon(points):
    bottommost = min(points, key=lambda p: (p.y, p.x))
    simply_poly = sorted(points, key=lambda p: PointSortKey(p, bottommost))
    return simply_poly



def graham_scan(points):
    points = simple_polygon(points)
    
    stack = points[:3]
    for i in range(3, len(points)):
        while not is_ccw(stack[-2], stack[-1], points[i]):
            stack.pop()
        stack.append(points[i])
        
    return stack


points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = graham_scan(points)
for v in verts:
    print(v)

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]
verts = graham_scan(points)
for v in verts:
    print(v)



    
##Q14
##points = [
##    Vec(40, 130),
##    Vec(60, 30),
##    Vec(50, 10),
##    Vec(70, 120),
##    Vec(15, 20),
##    Vec(80, 120),
##    Vec(52, 30),
##    Vec(30, 30),
##    Vec(25, 140)]
##verts = simple_polygon(points)
##for v in verts:
##    print(v)
##plot_poly(points)
##    
##points = [
##    Vec(100, 100),
##    Vec(0, 100),
##    Vec(50, 0)]
##verts = simple_polygon(points)
##for v in verts:
##    print(v)
##
##points = [
##    Vec(100, 100),
##    Vec(0, 100),
##    Vec(100, 0),
##    Vec(0, 0),
##    Vec(49, 50)]
##verts = simple_polygon(points)
##for v in verts:
##    print(v)




##q10
##points = [
##    Vec(1, 99),
##    Vec(0, 100),
##    Vec(50, 0),
##    Vec(50, 1),
##    Vec(50, 99),
##    Vec(50, 50),
##    Vec(100, 100),
##   Vec(99, 99)]
##verts = gift_wrap(points)
##for v in verts:
##    print(v)
####plot_hull(points, verts)
##
##points = [
##    Vec(1, 1),
##    Vec(99, 1),
##    Vec(100, 100),
##    Vec(99, 99),
##    Vec(0, 100),
##    Vec(100, 0),
##    Vec(1, 99),
##    Vec(0, 0),
##    Vec(50, 50)]
##verts = gift_wrap(points)
##for v in verts:
##    print(v)



    
##plot_hull(points, verts)
##Q8
##verts = [
##    (0, 0),
##    (100, 0),
##    (100, 100),
##    (0, 100)]
##points = [Vec(v[0], v[1]) for v in verts]
##print(is_strictly_convex(points))
##
##verts = [
##    (0, 0),
##    (0, 100),
##    (100, 100),
##    (100, 0)]
##points = [Vec(v[0], v[1]) for v in verts]
##print(is_strictly_convex(points))
##
##verts = [
##    (60, 60),
##    (100, 0),
##    (100, 100),
##    (0, 100)]
##points = [Vec(v[0], v[1]) for v in verts]
##print(is_strictly_convex(points))



##Q7
##a = Vec(0, 0)
##b = Vec(100, 0)
##c = Vec(101, 1)
##d = Vec(101, -1)
##print(intersecting(a, b, c, d))
##
##a = Vec(0, 0)
##b = Vec(100, 0)
##c = Vec(99, 1)
##d = Vec(99, -1)
##print(intersecting(a, b, c, d))
    




##Q6
##points = [
##    Vec(1, 99),
##    Vec(0, 100),
##    Vec(50, 0),
##    Vec(50, 1),
##    Vec(50, 99),
##    Vec(50, 50),
##    Vec(100, 100),
##   Vec(99, 99)]
##
##print(classify_points(Vec(0, 49), Vec(100, 49), points))






##Q5
##a = Vec(1000, 2000)
##b = Vec(0, 0)
##p = Vec(500, 1000)
##print(is_on_segment(p, a, b))
##
##a = Vec(0, 0)
##b = Vec(1000, 2000)
####point_tuples = [(-1, -1),
####    (-1, -2),]
##point_tuples = [
##    (-1, -1),
##    (-1, -2),
##    (-1000, -2000),
##    (0, 0),
##    (1, 2),
##    (500, 1000),
##    (500, 1001),
##    (500, 999),
##    (1000, 2000),
##    (1001, 2001),
##    (1001, 2002),
##    (2000, 4000)]
##points = [Vec(p[0], p[1]) for p in point_tuples]
##for p in points:
##    print(p, is_on_segment(p, a, b))


####Q4 
####fredsville = Vec(10, 20)
####maryton = Vec(100, 200)
####pounamu = Vec(70, 50)
####fredsville = Vec(-11, 23)
####maryton = Vec(-15, -10)
####pounamu = Vec(70, 50)
####p = (maryton - fredsville) + pounamu
####print(p)
