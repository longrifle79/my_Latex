function y=nextprime(x);
% This program generates the next prime that occurs after x
% Uses Miller-Rabin method to check whether a prime or not

y=x+1;
% Don't consider any evens
if mod(y,2)==0,
   y=y+1;
end;

flag=1;
while flag,
   if (primetest(y)),
      return;
   end;
   y=y+2;
end;
