classdef utils
   methods
      function T1 = calT1(obj, b , alfa, beta)
           T1 = alfa * b^(beta);
      end

      function T2 = calT2(obj, b , alfa, beta)
           T2 = alfa * exp(b*beta);
      end

      function rowE = createParts(i, a, b, x, y, phi, t1, t2, pd, t2dot, tr, te)
%     Column 1:  A    the additive intensity value of the ellipse
%     Column 2:  a    the length of the horizontal semi-axis of the ellipse 
%     Column 3:  b    the length of the vertical semi-axis of the ellipse
%     Column 4:  x0   the x-coordinate of the center of the ellipse
%     Column 5:  y0   the y-coordinate of the center of the ellipse
%     Column 6:  phi  the angle (in degrees) between the horizontal semi-axis 
%                     of the ellipse and the x-axis of the image  
%     Column 7: T1
%     Column 8: T2
%     Column 9: PD
%     Column 10: D1
%     Column 11: D2
%     Column 12: D3
%     Column 13: D4
            rowE = [ i a b x y phi t1 t2 pd t2dot tr te 0];
      end

      function E1 = showT1 (obj, E)
            n_rows = height(E);
            n_columns = width(E);
            for row = 1 : n_rows
                   E(row, 1) = E(row, 7);
            end
            E1 = E;
      end


      function E2 = showT2 (obj, E)
            n_rows = height(E);
            n_columns = width(E);
            for row = 1 : n_rows
               E(row, 1) = E(row, 8);
            end
            E2 = E;
       end


       function Epd = showPD (obj, E)
             n_rows = height(E);
             n_columns = width(E);
             for row = 1 : n_rows
                 E(row, 1) = E(row, 9);
             end
             Epd = E;
       end

       function SI = calculateSignal(obj, alfa, t1, t2dot, tr, te) 
              kh = 1;
              cosa = cos(alfa); 
              sina = sin(alfa);
              ratio1 = -tr/t1;
              ratio2 = -te/t2dot;
              p1 = sina * (1 -  exp(ratio1));
              p2 = 1 - cosa * exp(ratio1);
              p3 = exp(ratio2);
              SI = kh * (p1 / p2) * p3;
        end

     end
end