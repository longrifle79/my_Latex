function y = text2int1 (x)
% This function takes the letter in the string x and converts 
% it to an integer. 
% The convention for this function is
%  ' ' --> 0
%   a  --> 1
%   b  --> 2
%   and so on...

[s1,s2]=size(x);

yvec=x - 'a'+1;   
inds=find(yvec<1);
yvec(inds)=zeros(size(inds));  % set all the spaces to a value of 0

% Now we must convert to a number

y=zeros(s1,1);
for k=1:s1,
for j=0:s2-1,
   ind=s2-j;
   y(k)=y(k)+yvec(k,ind)*100^(j);   
end;
end;
