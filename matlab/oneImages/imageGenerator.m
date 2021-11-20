
s = 600;

fa = 1;
flag = 1;
for c = 1: s
    alfa = floor(20 * rand + 20);
    TR = floor(20 * rand + 1);
    TE = floor(10 * rand);
    E1 = makeEllipse(TR, TE, alfa);
    n_ellipse = height(E1);
    k = floor((n_ellipse -1) * rand + 1);
    alfa1 = E1(k,2);
    beta1 = E1(k,3);
    cenx1 = E1(k,4);
    ceny1 = E1(k,5);
    phi1 = E1(k,6);
    if (alfa1 > 0.15 && flag ==1)
        fa = -1;
        flag = 0;
    end
    if (alfa1 < 0.1 && flag == 0)
        fa = 1;
        flag = 1;
    end
 
    b = 0.0015125863 * rand();
    alfa1 = alfa1 + 0.1*fa * b;
 
    beta1 = beta1 + 0.001*fa * b;
    cenx1 = cenx1 * (1.01 + b);
    if abs(cenx1) > 0.5
        ceny1 = 0;
    end
    ceny1 = ceny1 + 0.01*fa;

    if abs(ceny1) > 0.5
        ceny1 = 0;
    end
    phi1 = phi1 + 100*rand;

    E1(k, [2 3 4 5 6]) = [alfa1 beta1 cenx1 ceny1 phi1];
    E = E1(k, :);
    createP = mriphantom(E, 500);

    baseFileName = sprintf('%d.png', c);
    fullFileName = fullfile('images', baseFileName);
    imwrite(createP, fullFileName);

    % Create a table with the data and variable names
  %  T = table(TR, TE, alfa, 'VariableNames', { 'TR', 'TE', 'alfa'} );
    T = table(TR, TE, alfa) ;  
    % Write data to text file
    baseTextName = sprintf('%d.txt', c);
    fullTextName = fullfile('texts', baseTextName);
    writetable(T, fullTextName);
end
