function y = lfsrlength(v,n);
% This function tests the vector v of bits to see if it is generated
% by a linear feedback recurrence of length at most n

disp('Order   Determinant');
for j=1:n,
   M=circmat(v,j);
   Mdet=mod(det(M),2);
   disp([num2str(j),'        ',num2str(Mdet)]);  
end
