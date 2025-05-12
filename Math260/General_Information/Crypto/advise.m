function aceind=advise(shufvals,p)
% This function advises the player as to which card is the ace
% It uses the fact that we chose a prime p such that the numerical 
% value of ace is a quadratic non-residue, while the numerical values
% of the other cards are quadratic residues

sln=length(shufvals);

for j=1:sln,
   test(j)=powermod(shufvals(j),(p-1)/2,p);
end;

aceind=find(test~=1);
disp(['Ace Index: ', num2str(aceind)]);


