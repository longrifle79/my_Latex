function z=primetest(n);
% This function tests a number n for primeness.
% It uses the Miller-Rabin primality (compositeness) test
% z=1 means prime
% z=0 means composite
T=30;  % hard coded amount of times we test
       % increasing T decreases chance something is prime when it isn't.
       % Probability of error is bounded by (1/4)^T

% First, express n-1 as n-1 = r * 2^s 
if mod(n,2)==0,
   z=0;
   return;
else  
r=n-1;
s=0;
while (mod(r,2)==0),
   s=s+1;
   r=r/2;
end;
for j=1:T,  %test T times 
   a=2+floor(rand(1,1) * (n-4));
   y=powermod(a,r,n);
   if ((y~=1) & (y~=n-1)),
      k=1;
      while ( (k<=s-1) & (y ~= n-1)),
         y=mod(y*y,n);
         if y==1,
            z=0;  % n is composite
            return
         else 
            k=k+1;
         end;  %end if-else
      end; %end while
      if (y ~= n-1),
         z=0;  % n is composite
         return
      end;
   end; %end if
end; %end for

end; %end if

z=1;  %final case is it passed all tests and is prime