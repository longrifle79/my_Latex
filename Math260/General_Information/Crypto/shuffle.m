function shval = shuffle(cvals,k,p)
% This function hides and shuffles the cards whose values are passed
% in the vector cvals. The hiding operation takes place by taking 
% cvals and raising its elements to the kth power mod p
% Shuffling is a random permutation

cln=length(cvals);

hvals=zeros(cln,1);
for j=1:cln,
   hvals(j)=powermod(cvals(j),k,p);
end;

% now to shuffle the cards
ind=randperm(cln);

shval=hvals(ind);

