    # use pypng method
    s2 = img2.shape
    tn1 = s2[2];
    tn2 = s2[1];
    tn3 = s2[0];
    pngWriter = png.Writer(tn1, tn2);
    pngImg = [];
    irange = range(tn3);
    jrange = range(tn2);
    for i in irange:
        aa = [ ];
        for j in jrange:
            d1 = img1[i,j];
            aa.extend (d1);
        pngImg.append(aa);
    pngWriter.write(ofname, pngImg);
