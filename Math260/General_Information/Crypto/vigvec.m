function y=vigvec(txt,m,n)
% This function gives the frequencies of the letters a through z that
%  occur in positions congruent to n (mod m) in the text string txt.

x=choose(txt,m,n);
yct=frequency(x);

y=yct/sum(yct);