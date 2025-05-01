% Test program to do some RSA example


maple('p:= nextprime(1897345789)')
maple('q:= nextprime(278478934897)')
maple('n:=p*q');

maple('x:=101');

maple('e:=nextprime(12345678)')

maple('d:=e&^(-1) mod ((p-1)*(q-1))')

maple('y:=x&^(e) mod n')

maple('c:= y&^(d) mod n')
