
s = 3000;

fa = 1;
flag = 1;
count = 0;
img_index = 1;
for c = 1: s
    alfa = floor(40 * rand + 20);
    TR = floor(20 * rand + 1);
    TE = floor(20 * rand);
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
 
    b = 0.9 * rand();
   % alfa1 = alfa1 + 0.1*fa * b;
 
    beta1 = beta1 + 0.001*fa * b;
    cenx1 = cenx1 * (1.01 + b);
    if abs(cenx1) > 0.5
        ceny1 = 0;
    end
    ceny1 = ceny1 + 0.01*fa;

    if abs(ceny1) > 0.5
        ceny1 = 0;
    end
    phi1 = floor(phi1 + 100*rand);

    E1(k, [2 3 4 5 6]) = [alfa1 beta1 cenx1 ceny1 phi1];
    E = E1(k, :);
    T1 = E(7);
    T2 = E(8);
    T2dot = E(10);
    if k > 6
        E2 = E1(k, :);
        E2(5) = E2(5) - 0.3;
        E2(4) = E2(4) + 0.3;
        E3 = E1(k, :);
        E3(5)= E3(5)+ 0.3;
        E3(4) = E3(4) -0.3;


        E = [E; E2; E3];
    end

    createP = mriphantom(E, 128);
    theSum = sum(sum(createP));
    if theSum > 1.5
      baseFileName = sprintf('%d.png', img_index);
      fullFileName = fullfile('val/images', baseFileName);
      imwrite(createP, fullFileName);

      % Create a table with the data and variable names
  %  T = table(TR, TE, alfa, 'VariableNames', { 'TR', 'TE', 'alfa'} );
      T1 = E(7);
      T2 = E(8);
      T2dot = E(10);
      T = table(T1, T2, T2dot, TR, TE, alfa) ;  
      % Write data to text file
      baseTextName = sprintf('%d.txt', img_index);
      fullTextName = fullfile('val/texts', baseTextName);
      writetable(T, fullTextName);
      img_index = img_index + 1;
    else
        count = count + 1;
    end
end
disp(count);
disp(img_index);