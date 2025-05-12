function X=convm(x,p);
N = length(x)+2*p-2;
x=x(:);
xpad=[zeros(p-1,1);x;zeros(p-1,1)];
for k=1:p,
   X(:,k)=xpad(p-k+1:N-k+1);
end
