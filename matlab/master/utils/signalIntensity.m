function SI = signalIntensity(alfa, t1, t2dot, tr, te) 
    kh = 1;
    cosa = cos(alfa); 
    sina = sin(alfa);
    ratio1 = -tr/t1;
    ratio2 = -te/t2dot;
    p1 = sina * (1 -  exp(ratio1));
    p2 = 1 - cosa * exp(ratio1);
    p3 = exp(ratio2);
    SI = kh * (p1 / p2) * p3;

end