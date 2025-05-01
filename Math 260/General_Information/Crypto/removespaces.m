function outputstring = removespaces(inputstring)
%REMOVESPACES changes capital letters to lower-case
% and removes spaces to make ordinary text into a 
% plaintext suitable for encryption.
temp = lower(inputstring);
temp = strrep(temp,'.','');
temp = strrep(temp,',','');
temp = strrep(temp,';','');
outputstring = strrep(temp,' ','');

end

