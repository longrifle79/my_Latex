function y = lfsr(c,k,n);
% This function generates a sequence of n bits produced by the linear feedback
% recurrence relation that is governed by the coefficient vector c.
% The initial values of the bits are given by the vector k

y=zeros(1,n);

kln=length(k);
for j=1:n,
   if j<=kln,
      y(j)=k(j);
   else
      reg=y(j-kln:j-1);
      y(j)=mod(reg*c',2);   
   end;   
end
