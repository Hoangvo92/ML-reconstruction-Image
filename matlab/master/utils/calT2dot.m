function t2dot = calT2dot(alfa, beta) 
%T1 = alfa*(Bo)^beta
    B0 = 0.2;
    t2dot = alfa * exp(beta * B0);
end