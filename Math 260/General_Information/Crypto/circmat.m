function X = circmat(v,m);
% This function produces a circulant matrix of the type
% that is used in the function lfsrlength

v=v(:);  % enforce v to be a column vector
X=zeros(m,m);
vln=length(v);
if (vln < 2*m-1),
   error('The vector v needs to be atleast length 2m-1');
end

for j=1:m,
   X(:,j)= v(j:m+j-1); %place data in appropriate columns
end;
