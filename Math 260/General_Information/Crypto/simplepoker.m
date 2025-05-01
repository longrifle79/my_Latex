% This program plays a simplified poker game
clear

cards=['ten';'ace';'que';'jac';'kin'];

% Convert the cards to numerical values:
cvals=text2int1(cards)

%
% 
p=300649;

% generate a random exponent k with gcd(k,p-1)=1
k=khide(p);


% Shuffle and hide the cards
shufvals=shuffle(cvals,k,p)


% Now reveal the cards

reveal(shufvals,k,p)





% Now the advise function

advise(shufvals,p)


% To see that the ace was the only quadratic non-residue modulo p
% we do the following test:

powermod(cvals,(p-1)/2,p)
