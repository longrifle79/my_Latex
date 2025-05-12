function yct = frequency(txt);
% This function tabulates the amount of times each character 'a'-'z' 
% occurs in txt.

ychar=zeros(26,1);
yct=zeros(26,1);

for k=0:25,
   ychar(k+1)=char('a'+k);
   v=(txt==ychar(k+1,1));   %perform check to see 
   yct(k+1)=sum(v);
   ydisp=[ychar(k+1), '  ',num2str(yct(k+1))];
   disp(ydisp)
end;
