function y = multsell(p,M,a,b,n);
% This function prints the first M multiples of p
p=p(:)';

y=zeros(M,2);
y(1,:)=p;
q=p;
for k=2:M,
   z=addell(p,q,a,b,n);
   q=z;
   if (length(z)==0),   % must have returned a factor!
      y(k:M,:)=[];  % null out the rest
      disp('Multsell ended early since it found a factor');
      return;
   end;
   y(k,:)=z;
end;

   