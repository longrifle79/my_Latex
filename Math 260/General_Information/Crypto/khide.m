function k = khide(p);
% This function generates a random integer k that is between
% 1 and p-2 and is relatively prime to p-1.

flag=1;
while flag,
   k=1+ floor(rand(1,1)*(p-2));
   if gcd(k,p-1)==1,
      flag=0;
   end;
end;



