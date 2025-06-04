function result = powermod_big(a, e, n)
    % Symbolic modular exponentiation (safe for RSA-sized numbers)
    result = sym(1);
    a = mod(a, n);
    while e > 0
        if mod(e, 2) == 1
            result = mod(result * a, n);
        end
        e = floor(e / 2);
        a = mod(a * a, n);
    end
end
