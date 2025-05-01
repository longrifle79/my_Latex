function y = affinecrypt(x,a,b);
% This function performs the affine encryption function
%   y = a x + b mod 26
% where (a,26) = 1
% The result is kept in numerical representation

xnum=text2int(x);
ynum = mod( a*xnum + b, 26);
y=int2text(ynum);
