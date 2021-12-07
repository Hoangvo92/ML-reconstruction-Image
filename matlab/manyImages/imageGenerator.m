[P, E] = mriphantom('Modified Shepp-Logan', 500);

s = 10000;

fa = 1;
img_idx = 1;
count = 0;
for c = 1: s
    num_ellipse = height(E);
    chosen_num = floor(num_ellipse * rand);
    if chosen_num == 0
        chosen_num = 1;
    end
    ellipse = [];
    idx = floor(chosen_num* rand);
    for k = 1 : chosen_num
        if (k + idx) > num_ellipse
            ellipse = [ellipse; E(k + idx - num_ellipse, :)];
        else
            ellipse =[ellipse; E(k + idx, :)];
        end
    end
    alfa = floor(60 * rand + 20);
    TR = floor(20 * rand + 1);
    TE = floor(20 * rand);
    for r = 1 : height(ellipse)
         alfa1 = ellipse(r,2);
         beta1 = ellipse(r,3);
         cenx1 = ellipse(r,4);
         ceny1 = ellipse(r,5);
         if (alfa1 > 0.15)
             fa = -1;
         else
             fa = 1;
         end
 
         b = 0.9 * rand();
         %alfa1 = alfa1 + 0.1*fa * b;
    
         beta1 = beta1 + 0.001*fa * b;

         cenx1 = cenx1 * (1.01 + b);
         ceny1 = ceny1 + 0.01*fa;
         ellipse(r, [2 3 4 5 11 12 13]) = [ alfa1 beta1 cenx1 ceny1 TR TE alfa];

    end

   
    createP = mriphantom(ellipse, 500);
    theSum = sum(sum(createP));
    if theSum > 0.2

       baseFileName = sprintf('%d.png', img_idx);
       fullFileName = fullfile('val/images', baseFileName);
       imwrite(createP, fullFileName);

        % Create a table with the data and variable names
        %  T = table(TR, TE, alfa, 'VariableNames', { 'TR', 'TE', 'alfa'} );
         T = table(TR, TE, alfa) ;  
        % Write data to text file
        baseTextName = sprintf('%d.txt', img_idx);
        fullTextName = fullfile('val/texts', baseTextName);
        writetable(T, fullTextName);  
        img_idx = img_idx + 1;
    else
        count = count + 1;
    end
end


disp(count);
disp(img_idx);