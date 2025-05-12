function y = allshift(x);
% This function displays all of the shifts of the message x

for j=0:25,
   z=shift(x,j);
   disp(z);
end;
