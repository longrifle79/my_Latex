function rcards = reveal(shval,k,p)
% This function reveals the cards whose values are passed
% in the vector shval. The hiding operation took place by taking 
% the card values and raising them to the kth power mod p

cln=length(shval);
kinv=powermod(k,-1,p-1);


revvals=zeros(cln,1);

for j=1:cln,
   revvals(j)=powermod(shval(j),kinv,p);
   rcards(j,:)=int2text1(revvals(j));
end;


