function y = interppoly(x,f,m)
% This function calculates the interpolating polynomial that goes 
% through the points (x_j,f_j) in the vectors x and f
% The modulus is m
% The method used in this program is the Newton form of the interpolant.

if (length(x) ~=length(f)),
   error('Vectors are not the same length');
end;

n=length(x);

y=f;
temp=0;
for k=1:n-1,
   for j=n:-1:k+1,
      temp=mod(y(j)-y(j-1),m);
      temp1=powermod((x(j)-x(j-k)),-1,m);
      y(j)=mod(temp*temp1,m);
   end;
end;
y(1)=mod(y(1),m);

for k=n-1:-1:1,
   for j=k:n-1,
      temp=mod(y(j+1)*x(k),m);
      y(j)=mod(y(j)-temp,m);
   end;
end;

   
   
   
   