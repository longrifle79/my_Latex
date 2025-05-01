function yct = frequency1(txt);
% This function tabulates the amount of times each character 'a'-'z' 
% occurs in txt.
% same as frequency but without printing intermediate output

ychar=zeros(26,1);
yct=zeros(26,1);

for k=0:25,
   ychar(k+1)=char('a'+k);
   v=(txt==ychar(k+1,1));   %perform check to see 
   yct(k+1)=sum(v);
end;
