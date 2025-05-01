function y = lfsrsolve(v,n);
% Given a guess n for the length of the recurrence that generates
% the binary vector v, this function returns the coefficients of the
% recurrence.

v=v(:);

vln=length(v);

if (vln < 2*n),
   error('The vector v needs to be atleast length 2n');
end

M=circmat(v,n);
Mdet=det(M);

x=v(n+1:2*n);

Minv=inv(M);
Minv=mod(round(Minv*Mdet),2);
% A note: Technically, the round() function should never show up, but
% since Matlab does double precision arithmetic to calculate the inverse matrix
% we need to bring the result back to integer values so we can perform a meaningful
% mod operation. As long as this routine is not used on huge examples, it should
% be ok

y=mod(Minv*x,2);
y=y(:)';   % Convert the output to a row vector
