
% https://mriquestions.com/spoiled-gre-parameters.html
function [P, Ellipse] = generateImage( choice, TR, TE, alfa)
    E = makeEllipse(TR, TE, alfa);
    if choice == 0
        [P, Ellipse] = mriphantom(E, 500);
    end
    
    if choice == 1
        [P, Ellipse] = imt1phantom(E, 500);
    end

    if choice == 2
        [P, Ellipse] = imt2phantom(E, 500);
    end
end







