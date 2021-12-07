
function E = makeEllipse(TR, TE, alfa)
    A = 1.0;
    pd = 1.0;
    
    r1 = makeRow0(0.69, 0.92, 0, 0, 0.315, 0.08, 0, .062, TR, TE, pd, A, alfa);
    r2 = makeRow0(0.6624, 0.8740, 0, -.0184, 0.47, 0.1, 0, 0.0875, TR, TE, pd, A, alfa);
    r3 = makeRow0(0.11, 0.31, 0.22, 0, 4.2, 1.99, -18, 1.99, TR, TE, pd, A, alfa);   
    r4 = makeRow0(0.16, 0.41,-0.22, 0, 4.2, 1.99, 18, 1.99, TR, TE, pd, A, alfa);
    r5 = makeRow0(0.21, 0.25, 0, .35, 4.2, 1.99, 0, 1.99, TR, TE, pd, A, alfa);
    r6 = makeRow0(0.046, 0.046, 0, .1, 4.2, 1.99, 0, 1.99, TR, TE, pd, A, alfa);
    r7 = makeRow0(0.046, 0.046, 0, -.1, .65, 0.1, 0, 0.1, TR, TE, pd, A, alfa);
    r8 = makeRow0(0.046, 0.023, -.08, -.605, 4.2, 1.99, 0, 1.99, TR, TE, pd, A, alfa);
    r9 = makeRow0(0.023, 0.023, 0, -.606, .65, 0.1, 0, .1, TR, TE, pd, A, alfa);
    r10 = makeRow0(0.023, 0.046, .06, -.605, .78, 0.2, 0, 0, TR, TE, pd, A, alfa);
    E = [r1; r2; r3; r4; r5; r6; r7; r8; r9; r10];

end

function row0 = makeRow0( a, b, x0, y0, t1, t2, phi, t2dot, TR, TE, pd, A, alfa)
       
       % si = calculateSignal(phi*pi/180, t1, t2, t2dot, TR, TE );
        row0 = [A a b x0 y0 phi t1 t2 pd t2dot TR TE alfa];
end