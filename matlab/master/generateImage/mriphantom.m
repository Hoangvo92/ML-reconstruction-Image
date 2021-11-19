function [p,ellipse]=mriphantom(varargin)
%PHANTOM Generate a head phantom image.
%   P = PHANTOM(DEF,N) generates an image of a head phantom that can   
%   be used to test the numerical accuracy of RADON and IRADON or other  
%   2-D reconstruction algorithms.  P is a grayscale intensity image that
%   consists of one large ellipse (representing the brain) containing
%   several smaller ellipses (representing features in the brain).
%
%   DEF is a string that specifies the type of head phantom to generate.
%   Valid values are: 
%         
%      'Shepp-Logan'            A test image used widely by researchers in
%                               tomography
%      'Modified Shepp-Logan'   (default) A variant of the Shepp-Logan phantom
%                               in which the contrast is improved for better  
%                               visual perception.
%
%   N is a scalar that specifies the number of rows and columns in P.
%   If you omit the argument, N defaults to 256.
% 
%   P = PHANTOM(E,N) generates a user-defined phantom, where each row
%   of the matrix E specifies an ellipse in the image.  E has six columns,
%   with each column containing a different parameter for the ellipses:
%   
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
%     Column 10: T2*
%     Column 11: TR
%     Column 12: TE
%     Column 13: D4
%
%   For purposes of generating the phantom, the domains for the x- and 
%   y-axes span [-1,1].  Columns 2 through 5 must be specified in terms
%   of this range.
%
%   [P,E] = PHANTOM(...) returns the matrix E used to generate the phantom.
%
%   Class Support
%   -------------
%   All inputs must be of class double.  All outputs are of class double.
%
%   Remarks
%   -------
%   For any given pixel in the output image, the pixel's value is equal to the
%   sum of the additive intensity values of all ellipses that the pixel is a 
%   part of.  If a pixel is not part of any ellipse, its value is 0.  
%
%   The additive intensity value A for an ellipse can be positive or negative;
%   if it is negative, the ellipse will be darker than the surrounding pixels.
%   Note that, depending on the values of A, some pixels may have values outside
%   the range [0,1].
%    
%   See also RADON, IRADON.

%   Copyright 1993-2003 The MathWorks, Inc.  
%   $Revision: 1.13.4.2 $  $Date: 2003/08/01 18:09:35 $

%   References: 
%      A. K. Jain, "Fundamentals of Digital Image Processing", p. 439.
%      P. A. Toft, "The Radon Transform, Theory and Implementation" (unpublished
%      dissertation), p. 199.

[ellipse,n] = parse_inputs(varargin{:});

p = zeros(n);

xax =  ( (0:n-1)-(n-1)/2 ) / ((n-1)/2); 
xg = repmat(xax, n, 1);   % x coordinates, the y coordinates are rot90(xg)
maximum = 0;

for k = 1:size(ellipse,1)    

   t1 = ellipse(k,7);          % T1
   t2dot = ellipse(k,10);      % T2*
   tr = ellipse(k,11);         % TR
   te = ellipse(k,12);         % TE
   alf = ellipse(k,13)*pi/180;        % flip angle alfa

  
   kh = 1;
   cosa = cos(alf);
   sina = sin(alf);
   ratio1 = -tr / t1;
   ratio2 = -te / t2dot;
   p1 = sina * (1 -  exp(ratio1));
   p2 = 1 - cosa * exp(ratio1);
   p3 = exp(ratio2);
   si = kh * (p1 / p2) * p3;
   if abs(si) > maximum
       maximum = abs(si);
   end
end

for k = 1:size(ellipse,1)    
   asq = ellipse(k,2)^2;       % a^2
   bsq = ellipse(k,3)^2;       % b^2
   phi = ellipse(k,6)*pi/180;  % rotation angle in radians
   x0 = ellipse(k,4);          % x offset
   y0 = ellipse(k,5);          % y offset
   t1 = ellipse(k,7);          % T1
   t2dot = ellipse(k,10);      % T2*
   tr = ellipse(k,11);         % TR
   te = ellipse(k,12);         % TE
   alf = ellipse(k,13)*pi/180;        % flip angle alfa
  % A = calculateSignal(phi, t1, t2dot, tr, te);
   A = ellipse(k,1);           % Amplitude change for this ellipse
   x=xg-x0;                    % Center the ellipse
   y=rot90(xg)-y0;  
   cosp = cos(phi); 
   sinp = sin(phi);

   idx = find(((x.*cosp + y.*sinp).^2)./asq + ((y.*cosp - x.*sinp).^2)./bsq <= 1); 
   kh = 1;
   cosa = cos(alf);
   sina = sin(alf);
   ratio1 = -tr / t1;
   ratio2 = -te / t2dot;
   p1 = sina * (1 -  exp(ratio1));
   p2 = 1 - cosa * exp(ratio1);
   p3 = exp(ratio2);
   si = kh * (p1 / p2) * p3;
 
   p(idx) = p(idx) + si ;
end
   
   
function [e,n] = parse_inputs(varargin)
%  e is the m-by-6 array which defines ellipses
%  n is the size of the phantom brain image

n=256;     % The default size
e = [];
defaults = {'shepp-logan', 'modified shepp-logan'};

for i=1:nargin
   if ischar(varargin{i})         % Look for a default phantom
      def = lower(varargin{i});
      idx = strmatch(def, defaults);
      if isempty(idx)
         eid = sprintf('Images:%s:unknownPhantom',mfilename);
         msg = 'Unknown default phantom selected.';
         error(eid,'%s',msg);
      end
      switch defaults{idx}
      case 'shepp-logan'
         e = shepp_logan;
      case 'modified shepp-logan'
         e = modified_shepp_logan;
      end
   elseif numel(varargin{i})==1 
      n = varargin{i};            % a scalar is the image size
   elseif ndims(varargin{i})==2 && size(varargin{i},2)==13 
      e = varargin{i};            % user specified phantom
   else
      eid = sprintf('Images:%s:invalidInputArgs',mfilename);
      msg = 'Invalid input arguments.';
      error(eid,'%s',msg);
   end
end


%function SI = calculateSignal(alfa, t1, t2dot, tr, te) 
%    kh = 1;
%    cosa = cos(alfa); 
%    sina = sin(alfa);
%    ratio1 = -tr/t1;
%    ratio2 = -te/t2dot;
%    p1 = sina * (1 -  exp(ratio1));
%    p2 = 1 - cosa * exp(ratio1);
%    p3 = exp(ratio2);
%    SI = kh * (p1 / p2) * p3;

%end
if isempty(e)                    % ellipse is not yet defined
   e = modified_shepp_logan;
end

   

      
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Default head phantoms:   
%

function shep=shepp_logan
%
%  This is the default head phantom, taken from AK Jain, 439.
%
%         A    a     b    x0    y0    phi   T1    T2      PD    T2*   TR  TE   d4
%   
%        --------------------------------------------------------------
shep = [  1   .69   .92    0     0     0    .315  0.08   1      .062  5   2   30 
        -.98 .6624 .8740   0  -.0184   0    .47   0.1    1      .0875 5   2   30
        -.02 .1100 .3100  .22    0    -18   4.2   1.99   1     1.99   5   2   30
        -.02 .1600 .4100 -.22    0     18   4.2   1.99   1     1.99   5   2   30
         .01 .2100 .2500   0    .35    0    4.2   1.99   1     1.99   5   2   30
         .01 .0460 .0460   0    .1     0    4.2   1.99   1     1.99   5   2   30
         .01 .0460 .0460   0   -.1     0    .65    .1    1      .1    5   2   30
         .01 .0460 .0230 -.08  -.605   0    4.2   1.99   1     1.990  5   2   30
         .01 .0230 .0230   0   -.606   0    .65    .1    1      .1    5   2   30
         .01 .0230 .0460  .06  -.605   0    .78    .2    1      0     5   2   30];
      
      
function toft=modified_shepp_logan
%
%   This head phantom is the same as the Shepp-Logan except 
%   the intensities are changed to yield higher contrast in
%   the image.  Taken from Toft, 199-200.
%      
%         A    a     b    x0    y0    phi  T1    T2     PD    T2*   TR   TE   d4
%        --------------------------------------------------------------
toft = [  1   .69   .92    0     0     0   .315  0.08    1     .062   300 40    10
        -.8  .6624 .8740   0  -.0184   0  0.47   0.1     1     .0875  300 40    10 
        -.2  .1100 .3100  .22    0    -18 4.2    1.99    1    1.99    300 40    10
        -.2  .1600 .4100 -.22    0     18 4.2    1.99    1    1.99    300 40    10
         .1  .2100 .2500   0    .35    0  4.2    1.99    1    1.99    300 40    10 
         .1  .0460 .0460   0    .1     0  4.2    1.99    1    1.99    300 40    10  
         .1  .0460 .0460   0   -.1     0   .65    .1     1     .1     300 40    10 
         .1  .0460 .0230 -.08  -.605   0  4.2    1.99    1    1.99    300 40    10 
         .1  .0230 .0230   0   -.606   0   .65    .1     1     .1     300 40    10  
         .1  .0230 .0460  .06  -.605   0   .78    .2     1      0     300 40    10];
       

       
            
        
             