import pdb;
import numpy as np;
from scipy import misc

def loadPNG (fname):
    image = misc.imread(fname);
    return image;

def diffPNG (img1, img2, log_fname):
    s1 = img1.shape
    d1 = img1.dtype
    s2 = img2.shape
    d2 = img2.dtype
    if s1 != s2:
        print "size is diff";
        return;
    if d1 != d2:
        print "data type is diff";
        return;
        
    f = open (log_fname, "wt");
    print s1;
    print d1;
    pdb.set_trace();
    n1 = s1[0];
    n2 = s1[1];
    n3 = s1[2];
    irange = range(n1);
    jrange = range(n2);
    diff_cnt = 0;
    for i in irange:
        for j in jrange:
            d1 = img1[i,j];
            d2 = img2[i,j];
            if not np.array_equal (d1, d2):
                print >> f, "%d, %d (%s) (%s)" % (i, j, d1, d2)
                diff_cnt = diff_cnt + 1;
    f.close();
    return diff_cnt == 0;
    
def test001 ():
    dnam = "../data";
    fname1 = dnam + "/test_image_1.png";
    fname2 = dnam + "/test_image_2.png";
    log_fname = "output.txt";
    img1 = loadPNG (fname1);
    img2 = loadPNG (fname2);
    e = diffPNG (img1, img2, log_fname);
    return e;
    
if __name__ == "__main__":
    test001 ();
    
