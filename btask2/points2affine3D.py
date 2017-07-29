# input - 
#   Coordinate A - Pi (px,py,pz, 1), i = 0 ... N >= 4
#   Coordinate B - Qi (qx,qy,qz, qw)
# Formula - 
#   [a11  a12 a13 a14 ]
#   [a21  a22 a23 a24 ] * P1 = Q1
#   [a31  a32 a33 a34 ]
#   [a41  a42 a43 a44 ]
# 
#   a11 * px1 + a12 * py1 + a13 * pz1 + a14 = qx1   (1)
#   a21 * px1 + a22 * py1 + a23 * pz1 + a24 = qy1   (2)
#   a31 * px1 + a32 * py1 + a33 * pz1 + a34 = qz1   (3)
#   a41 * px1 + a42 * py1 + a43 * pz1 + a44 = qw1   (4)
#   a11 * px2 + a12 * py2 + a13 * pz2 + a14 = qx2   (5)
#   a21 * px2 + a22 * py2 + a23 * pz2 + a24 = qy2   (6)
#   a31 * px2 + a32 * py2 + a33 * pz2 + a34 = qz2   (7)
#   a41 * px2 + a42 * py2 + a43 * pz2 + a44 = qw2   (8)
#   a11 * px3 + a12 * py3 + a13 * pz3  + a14 = qx3   (9)
#   a21 * px3 + a22 * py3 + a23 * pz3  + a24 = qy3   (10)
#   a31 * px3 + a32 * py3 + a33 * pz3  + a34 = qz3    (11)
#   a41 * px3 + a42 * py3 + a43 * pz3  + a44 = qw3   (12)
#   a11 * px4 + a12 * py4 + a13 * pz4  + a14 = qx4   (13)
#   a21 * px4 + a22 * py4 + a23 * pz4  + a24 = qy4   (14)
#   a31 * px4 + a32 * py4 + a33 * pz4  + a34 = qz4    (15)
#   a41 * px4 + a42 * py4 + a43 * pz4  + a44 = qw4   (16)
#   ....

# Check if it four point is in the same plane
#   D1 = P2-P1
#   D2 = P3-P1
#   D3 = P4-P1
#   v = (D1 x D2) dot D3
#   if (v near 0) it's in the same plane
#   repeat until all points checked.

# Solver
#   NumPy linalg.lstsq (a, b)
#   a = [ [a11, a12, a13, a14
#             a21, a22, a23, a24
#             a31, a32, a33, a34,
#             a41, a42, a43, a44]
#             .... repeat above
#   b = [qx1, qy1, qz1, qw1,
#          qx2, qy2, qz2, qw2,
#          qx3, qy3, qz3, qw3,
#          qx4, qy4, qz4, qw4,
#          .... ]

from math import sqrt, fabs
import numpy as np;
import sys;

def dot (v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2];

def cross (v1, v2):
    return np.cross (v1, v2)

def normal (v):
    n = sqrt(v[0]*v[0] + v[1]*v[1] + v[2] * v[2]);
    return (v[0]/n, v[1]/n, v[2]/n);

def validInputPoints (plst):
    p1 = plst[0];
    p2 = plst[1];
    p3 = plst[2];
    D1 = (p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2])
    D2 = (p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2])
    N = cross (D1, D2);
    
    bad_point_cnt = 0;
    for p in plst[3:]:
        D3 = (p[0]-p1[0], p[1]-p1[1], p[2]-p1[2])
        v = dot (N, D3);
        # print "v = %f" % v
        f = fabs(v)
        eps = 0.001;
        if f < eps:
            bad_point_cnt = bad_point_cnt + 1;
    if bad_point_cnt == len(plst) - 3:
        return False;
    return True;

def buildMatrix (plst, qlst):
    a = None;
    b = None;
    n = len(plst)
    for i in range(n):
        p = plst[i];
        a1 = np.array ([p[0], p[1], p[2], 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
        a2 = np.array ([0, 0, 0, 0, p[0], p[1], p[2], 1, 0, 0, 0, 0, 0, 0, 0, 0]);
        a3 = np.array ([0, 0, 0, 0, 0, 0, 0, 0, p[0], p[1], p[2], 1, 0, 0, 0, 0]);
        a4 = np.array ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, p[0], p[1], p[2], 1]);
        if a == None:
            a = a1;
        else:
            a = np.vstack ((a, a1));
        a = np.vstack((a,a2));
        a = np.vstack((a,a3));
        a = np.vstack((a,a4));
        
        q = qlst[i];
        b1 = np.array ([q[0]]);
        b2 = np.array ([q[1]]);
        b3 = np.array ([q[2]]);
        b4 = np.array ([q[3]]);
        if b == None:
            b = b1;
        else:
            b = np.hstack ((b, b1));
        b = np.hstack ((b, b2));
        b = np.hstack ((b, b3));
        b = np.hstack ((b, b4));
            
    return (a, b);

def dumpList (msg, plst):
    print "%s=%s" % ( msg,  "[" + ", ".join( str(x) for x in plst) + "]")
    
def test001 ():
    v1 = [0.5, 1.0, 0];
    v2 = [1.0, 0, 0];
    x = dot (v1, v2);
    x = normal (v1);
    print "points2affine3D testing - ";
    # print "x = (%f,%f,%f)" % x
    
    p1 = (1.0, 0.0, 0, 1.0);
    p2 = (0.0, 0.0, 0.0, 1.0);
    p3 = (0.0, 1.0, 0.0, 1.0);
    p4 = (0.0, 0.0, 1.0, 1.0);
    q1 = (0.0, -1.0, -1.0, 1.0);
    q2 = (-1.0, -1.0, -1.0, 1.0);
    q3 = (-1.0, 0.0, -1.0, 1.0)
    q4 = (-1.0, -1.0, 0.0, 1.0)
    e = validInputPoints ((p1, p2, p3, p4));
    if not e:
        print "points are in the same plane";
        sys.exit(-1);
    
    plst = [p1, p2, p3, p4];
    qlst = [q1, q2, q3, q4];
    dumpList ("  plst", plst);
    dumpList ("  qlst", qlst);
    (a, b) = buildMatrix (plst, qlst)
    x = np.linalg.lstsq (a, b);
    m4 = x[0].reshape(4,4);
    print "  output=%s" % m4
    
if __name__ == "__main__":
    test001 ();
    
