function y = randprime(N);
% This function finds a random prime between 1 and N
% The prime is tested using Miller-Rabin

N1=N-1;
flag=1;
while flag,
   y=1+floor((N1)*rand(1,1));
   if primetest(y),
      return;
   end;
end; %end while

