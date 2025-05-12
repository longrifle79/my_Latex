function y = int2text1 (x)
% This function takes the number in the variable x and converts 
% it to a character y. 
% The convention for this function is
%   a  <-- 0
%   b  <-- 1
%   and so on...

j=1;
flag=1;
xv=x;
while flag,
   xrem=rem(xv,100);
   xv=floor(xv/100);
   xstore(j)=xrem;
   j=j+1;
   if xv<1,
      flag=0;
   end;
end;

xstore=xstore(:);
yvec=flipud(xstore)';

y=char(yvec+'a'-1);
ind=find(y=='`');
y(ind)=' ';