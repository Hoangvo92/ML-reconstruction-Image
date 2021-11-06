classdef utils
   methods
      function T1 = calT1(obj, b , alfa, beta)
           T1 = alfa * b^(beta);
      end

      function T2 = calT2(obj, b , alfa, beta)
           T2 = alfa * exp(b*beta);
      end

      function rowE = createParts(i, a, b, x, y, phi, t1, t2, pd)
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
            rowE = [ i a b x y phi t1 t2 pd 0 0 0 0];
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

     end
end