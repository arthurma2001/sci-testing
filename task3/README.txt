This directory contains
  diffpng.py
  test_diffpng.py

The test data directory is ../data. It contains
  test_image_1.png
  test_image_2.png

Output difference to output.txt, the format is
  128, 437   ([111 139  38]) ([0 0 0])
  
  The first two numbers are the location(X,Y) in the pixel.
  The second tuple is image1's rgb
  The third tuple is  image2's rgb
  From the above example, it can be seen that 128,437 is the X, Y location in the pixel
  ([111, 139, 38]) is image1's rgb
  ([0,0,0]) is image2's rgb
