import numpy as np;
from scipy import misc
import points2affine2D
from PIL import Image;
import pdb;

def loadPNG (fname):
    image = misc.imread(fname);
    return image;

def calcPoint (mat2, i, j):
    v1 = mat2[0];
    v2 = mat2[1];
    i1 = v1[0] * i + v1[1] * j + v1[2];
    j1 = v2[0] * i + v2[1] * j + v2[2];
    return (int(i1), int(j1))

# img1 p1
#   p2 = mat2 * p1
#   copy p1's rgb to img2's @p2
def addPNG (img1, img2, mat2):
    s1 = img1.shape
    d1 = img1.dtype
    s2 = img2.shape
    d2 = img2.dtype
    if d1 != d2:
        print "data type is diff";
        return;
    out = np.copy (img2);
    print s1;
    print d1;
    sn1 = s1[0];
    sn2 = s1[1];
    sn3 = s1[2];
    tn1 = s2[0];
    tn2 = s2[1];
    tn3 = s2[2];
    irange = range(sn1);
    jrange = range(sn2);
    pdb.set_trace();
    for i in irange:
        for j in jrange:
            d1 = img1[i,j];
            p2 = calcPoint (mat2, i, j);
            i2 = p2[0];
            j2 = p2[1];
            if i2 >= 0 and i2 < tn1 and j2 >= 0 and j2 < tn2:
                out[i2,j2] = d1
    return out;
    
def test001 ():
    dnam = "../data"
    fname1 = dnam + "/test_image_1.png";
    fname2 = dnam + "/test_image_2.png";
    ofname = dnam + "/tmp_output.png";
    img1 = loadPNG (fname1);
    img2 = loadPNG (fname2);
    mat2 = [[0.5, 0], [0, 0.5]];
    
    p1 = (0.0, 1.0, 1.0);
    p2=(0.0, 0.0, 1.0);
    p3=(1.0, 0.0, 1.0);
    q1 = (0.0, 0.5, 1.0);
    q2 = (0.0, 0.0, 1.0);
    q3 = (0.5, 0.0, 1.0)
    plst = [p1, p2, p3];
    qlst = [q1, q2, q3];
    mat2 = points2affine2D.buildMatrix2D (plst, qlst);
#  mat2 = [[0.5, 0, 0],  [0, 0.5, 0], [0, 0, 1] ];

    oimg = addPNG (img1, img2, mat2);
    # misc.imsave (ofname, img2); # crash in centos7.2
    img = Image.fromarray(oimg)
    img.save(ofname)

if __name__ == "__main__":
    test001 ();
    
