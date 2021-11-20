for im = 1: 3
    n = randi([300 500]);
    [~, E] = phantom('Shepp-Logan', n);
    for roi = 1: (height(E)-2)
        image = Structure(roi, n, E);
        baseFileName = sprintf('roi_%d_%d_%d.png', im, roi, n);
        fullFileName = fullfile('structures', baseFileName);
        imwrite(image, fullFileName);
    end

end

function image = Structure(j, n, E)
    % [P, E] = phantom('Modified Shepp-Logan', n);
     n_rows = height(E);%% height: Computes number of rows in E, use width for columns
     E(2 + j, 1) = 1;
     %do not include the two ellipses used for the sculp: only the once inside
    % for c = 3 : n_rows
     for c = 1 : n_rows
         if c ~= (2+j)
             E(c, : ) = zeros(1,6);
         end
     end
     image = phantom(E, n);
end


function T1 = calT1(b , alfa, beta)
    T1 = alfa * b^(beta);

end

function T2 = calT2(b , alfa, beta)
    T2 = alfa * exp(b*beta);

end





