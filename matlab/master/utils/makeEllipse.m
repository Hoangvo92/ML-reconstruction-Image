function rowE = makeEllipse( a, b, x0, y0, phi, alfa1, beta1, t1, t2, pd, alfa2, beta2, t2dot, tr, te, alfa)
%     input: parameters to form an Ellipse
%            alfa1 and beta1 help calculate t1, calling calT1.m
%            alfa2 and beta2 help calculate t2dot, calling calT2dot.m
%     output: a list of 13 elements
%     Column 1:  i    the additive intensity value of the ellipse
%     Column 2:  a    the length of the horizontal semi-axis of the ellipse 
%     Column 3:  b    the length of the vertical semi-axis of the ellipse
%     Column 4:  x0   the x-coordinate of the center of the ellipse
%     Column 5:  y0   the y-coordinate of the center of the ellipse
%     Column 6:  phi  the angle (in degrees) between the horizontal semi-axis 
%                     of the ellipse and the x-axis of the image 
%    
%     Column 7:  T1
%     Column 8:  T2
%     Column 9:  PD
%     Column 10: T2*
%     Column 11: TR
%     Column 12: TE
%     Column 13: alfa
      i = 1; % A: intensity, default 1
      if t1 == -1.0
          t1 = calT1(alfa1, beta1);
      end

      if t2dot == -1
          t2dot = calT2dot(alfa2, beta2);
      end

      rowE = [ i a b x0 y0 phi t1 t2 pd t2dot tr te alfa];
end

% makeEllipse(1, 1, 0, 0, 70, 1.35, 0.34, -1, 0.2 , 1, 0.2, -0.1, 0, 10, 2, 30);