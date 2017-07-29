# Build order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
# EXAMPLE
# Input:
#  projects: a, b, c, d, e, f

# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

# Output:
#   f, e, a, b, d, c
# Use any language you like for this one.

# Algorihm description -
#  use ia as a's index

#0   initial - a, b, c, d, e, f
#1   (a, d) -   a, b, c, d, e, f  (ia < id)
#2   (f, b)  -   a, c, d, e, f, b  (move b after f)
#3   (b, d) -   a, c, e, f, b, d  (move d after b)
#4   (f, a)  -   c, e, f, a, b, d  (move a after f)
#5   (d, c) -    e, f, a, b, d, c (move c after d)
#6   check if all dependencies is fit,  if not, repeat 1 - 6
#     until all dependencies is fit, max loop is length of projects.

import pdb;

def findIdx (plst, a):
    i = 0;
    for x in plst:
        if x == a:
            return i;
        i = i + 1;
    assert (False);
    return None;

def validDepPair (plst, p):
    ia = findIdx(plst, p[0]);
    ib = findIdx(plst, p[1]);
    return (ia < ib, ia, ib)

def addDepPair (plst, p):
    (e, ia, ib) = validDepPair (plst, p);
    if not e:
        x = plst[ib]
        i = ib
        while i < ia:
            plst[i] = plst[i+1]
            i = i + 1
        plst[ia] = x
    return plst

def addAllDepPair (plst, dlst):
    for pr in dlst:
        plst = addDepPair (plst, pr);
    return plst
    
def validAllDepPair (plst, dlst):
    for pr in dlst:
        (e, ia, ib) = validDepPair (plst, pr);
        if not e:
            return False
    return True
    
def process (plst, dlst):
    i = 0;
    n = len(plst);
    success = False;
    while  i < n and not success:
        success = validAllDepPair (plst, dlst);
        if not success:
            plst = addAllDepPair (plst, dlst)
        print "i=%d plst=%s" % (i, plst)
        i = i + 1;
    return success;

def get_nice_string(list_or_iterator):
    return "[" + ", ".join( str(x) for x in list_or_iterator) + "]"
    
def test001 ():
    plst = ['a', 'b', 'c', 'd', 'e', 'f'];
    dlst = (('a','d'), ('f', 'b'), ('b','d'), ('f', 'a'), ('d', 'c'));
    print "projects=%s" % get_nice_string(plst)
    print "dependencies=%s" % get_nice_string(dlst)
    
    ia = findIdx (plst, 'e')
    (e1, ia, ib) = validDepPair (plst, ('f','b'));
    print "e1=%d" % e1
    
    # pdb.set_trace();
    process (plst, dlst);
    olst = plst;
    if olst:
        print "output=%s" % get_nice_string(olst)
    else:
        print "failed"
            
if __name__ == "__main__":
    test001 ();
    

    
    
