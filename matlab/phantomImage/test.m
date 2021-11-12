E = makeEllipse(60, 5, 30);
for c= 1: size(E)
    t1 = E(c, 7);
    t2dot = E(c, 10);
    alfa = E(c, 13);
    tr = E(c, 11);
    te = E(c, 12);
    s = signalIntensity(alfa, t1, t2dot, tr, te);
    disp(s);
end