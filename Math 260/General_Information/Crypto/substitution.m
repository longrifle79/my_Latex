function outputtext = substitution(inputtext,key)
%SUBSTITUTION takes an inputtext and scrambles it according to 
%  a substitution cypher with given key.  The inputtext should be a 
%  string containing only the letters a-z (and no spaces).
%  The key should be a permutation of the numbers 0 through 25.
if ( (inputtext < 'a') | (inputtext > 'z') ),
   error('Text character out of range a-z');
end;
if ~isnumeric(key),
   error('Key not numerical');
end;  
if length(key) ~= 26,
    error('Key wrong length');
end;  
temp = text2int(inputtext);
for j = 1:length(temp)
    temp(j)=key(temp(j)+1);
end;
outputtext = int2text(temp);

end

