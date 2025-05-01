function x = crt(a,m);
% This function solves the Chinese Remainder Theorem problem:
%   x= a(1) mod m(1)
%   x= a(2) mod m(2)
%   ...
%   x= a(r) mod m(r)
% The values for a and m should be a vector of the same dimension

if any(size(a) ~= size(m)),
   error('The vectors a and m should be the same size');
end;

r=length(a);

M=prod(m);  % calculate the total modulus

x=0;

for j=1:r,
   x=x+ a(j)*(M/m(j))*invmodn(M/m(j),m(j));
   x=mod(x,M);
end;   

   