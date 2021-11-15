[P, E] = mriphantom('Modified Shepp-Logan', 500);
imshow(P);

%baseFileName = sprintf('Image #%d.png', k);
%fullFileName = fullfile(folder, baseFileName);
%imwrite(yourImage, fullFileName);
s = 500;
alfa1 = E(3,2);
alfa2 = E(4,2);
beta1 = E(3,3);
beta2 = E(4,3);
cenx1 = E(3,4);
cenx2 = E(4,4);
ceny1 = E(3,5);
ceny2 = E(4,5);
phi1 = E(3,6);
phi2 = E(4,6);
fa = 1;
flag = 1;
for c = 1: s
    
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
    alfa2 = alfa2 + 0.1*fa * b;
    beta1 = beta1 + 0.001*fa * b;
    beta2 = beta2 + 0.001*fa * b;
    cenx1 = cenx1 * (1.01 + b);
    cenx2 = cenx2 * (1.01 + b);
    if abs(cenx1) > 0.25
        cenx1 = 0.22;
        cenx2 = -0.22;
    end

    ceny1 = ceny1 + 0.01*fa;
    ceny2 = ceny2 + 0.01*fa;
    if abs(ceny1) > 0.3
        ceny1 = 0;
        ceny2 = 0;
    end

    
    if phi1 > -20
        phi1 = phi1 - 5;
        phi2 = - phi1;
    else
        phi1 = phi1 + 10;
        phi2 = - phi1;
    end

    choice = mod(c,4);
    if choice == 0
        E(3,[2 3]) = [alfa1 beta1];
        E(4,[2 3]) = [alfa2 beta2];
    elseif choice == 1
        E(3,4) = cenx1;
        E(4,4) = cenx2;
    elseif choice == 2
        E(3,5)= ceny1;
        E(4,5)= ceny2;
    else
        E(3,[2 3 4]) = [alfa1 beta1 cenx1];
       
        E(4,[2 3 4]) = [alfa2 beta2 cenx2];
    end
    
    alfa = floor(20 * rand + 20);
    TR = floor(20 * rand + 1);
    TE = floor(10 * rand);
    for r = 1: height(E)
         E(r,13) = alfa;
         E(r,12) = TE;
         E(r,11) = TR;
    end


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
