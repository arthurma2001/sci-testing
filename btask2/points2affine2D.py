# input - 
#   Coordinate A - Pi ...  (px,py,1), N >= 3
#   Coordinate B - Qi ... (qx,qy,qw)
# Formula - 
#   [a11  a12 a13]
#   [a21  a22 a23] * Pi = Qi
#   [a31  a32 a33]
# 
#   a11 * px1 + a12 * py1 + a13 = qx1   (1)
#   a21 * px1 + a22 * py1 + a23 = qy1   (2)
#   a31 * px1 + a32 * py1 + a33 = qz1   (3)
#   a11 * px2 + a12 * py2 + a13 = qx2   (4)
#   a21 * px2 + a22 * py2 + a23 = qy2   (5)
#   a31 * px2 + a32 * py2 + a33 = qz2   (6)
#   a11 * px3 + a12 * py3 + a13 = qx3   (7)
#   a21 * px3 + a22 * py3 + a23 = qy3   (8)
#   a31 * px3 + a32 * py3 + a33 = qz3    (9)
#   ....

# Check if it three point is in the same line
#   D1 = P2-P1
#   D2 = P3-P1
#   v = dot (D1,D2)
#   if (v == 1 or v == -1) it's in the same line
#   repeat for all left points

# Solver
#   NumPy linalg.lstsq (a, b)
#   a = [ [a11, a12, a13, a21, a22, a23, a31, a32, a33 ]
#             .... repeast from  above ) ]
#   b = [qx1, qy1, qz1, qx2, qy2, qz2, qx3, qy3, qz3 ... ]

from math import sqrt, fabs
import numpy as np;
import sys;

def dot (v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def normal (v):
    n = sqrt(v[0]*v[0] + v[1]*v[1]);
    return (v[0]/n, v[1]/n);

# check if points are in the same line
def validInputPoints (plst):
    p1 = plst[0];
    p2 = plst[1];
    D1 = (p2[0]-p1[0], p2[1]-p1[1])
    bad_point_cnt = 0;
    for p in plst[2:]:
        D2 = (p[0]-p1[0], p[1]-p1[1])
        d1 = normal (D1);
        d2 = normal (D2);
        v = dot (d1, d2);
    
        # print "v = %f" % v
        f = fabs(1-abs(v))
        eps = 0.001;
        if f < eps: bad_point_cnt = bad_point_cnt + 1;
    if bad_point_cnt == len(plst) - 2:
        return False;
    return True;

def buildMatrix (plst, qlst):
    a = None;
    b = None;
    n = len(plst)
    for i in range(n):
        p = plst[i];
        a1 = np.array ([p[0], p[1], 1, 0, 0, 0, 0, 0, 0]);
        a2 = np.array ([0, 0, 0, p[0], p[1], 1, 0, 0, 0]);
        a3 = np.array ([0, 0, 0, 0, 0, 0, p[0], p[1], 1]);
        if a == None:
            a = a1;
        else:
            a = np.vstack ((a, a1));
        a = np.vstack((a,a2));
        a = np.vstack((a,a3));
        
        q = qlst[i];
        b1 = np.array ([q[0]]);
        b2 = np.array ([q[1]]);
        b3 = np.array ([q[2]]);
        if b == None:
            b = b1;
        else:
            b = np.hstack ((b, b1));
        b = np.hstack ((b, b2));
        b = np.hstack ((b, b3));
            
    return (a, b);

def buildMatrix2D (plst, qlst):
    e = validInputPoints (plst);
    if not e:
        print "three point is in the same line";
        sys.exit(-1);
    
    (a, b) = buildMatrix (plst, qlst)
    x = np.linalg.lstsq (a, b);
    mat4 = x[0];
    return mat4.reshape(3,3)

def dumpList (msg, plst):
    print "%s=%s" % ( msg,  "[" + ", ".join( str(x) for x in plst) + "]")

def test001 ():
    v1 = [0.5, 1.0];
    v2 = [1.0, 0];
    x = dot (v1, v2);
    x = normal (v1);
    print "points2affine2D testing - ";
    # print "x = (%f,%f)" % x
    
    p1 = (0.0, 1.0, 1.0);
    p2=(0.0, 0.0, 1.0);
    p3=(1.0, 0.0, 1.0);
    q1 = (-1.0, 0.0, 1.0);
    q2 = (-1.0, -1.0, 1.0);
    q3 = (0.0, -1.0, 1.0)
    e = validInputPoints ((p1, p2, p3));
    if not e:
        print "three point is in the same line";
        sys.exit(-1);
        
    plst = [p1, p2, p3];
    qlst = [q1, q2, q3];
    dumpList ("  plst", plst);
    dumpList ("  qlst", qlst);
    mat4 = buildMatrix2D (plst, qlst)
    print "  output = %s" % mat4
    
if __name__ == "__main__":
    test001 ();
    
