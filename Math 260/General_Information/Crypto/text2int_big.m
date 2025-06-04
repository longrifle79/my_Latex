% Function to encode text as base-26 integer
function num = text2int_big(text)
    text = lower(text);
    num = sym(0);
    for i = 1:length(text)
        letter_val = double(text(i)) - double('a');
        num = num * 26 + letter_val;
    end
end
