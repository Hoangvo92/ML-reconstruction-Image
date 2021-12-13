function t1 = calT1(alfa, beta) 
%T1 = alfa*(Bo)^beta
    B0 = 0.2; %testla
    t1 = alfa * power(B0, beta);
end