function y = inv_field( a,n);
% This function calculates the inverse of an element a mod n


g0=n;
g1=a;
u0=1; 
v0=0;
u1=0;
v1=1;
i=1;


if (a<0) {
   a=a+n;
   g1=g1+n;
   }
while (g1),
     y=g0 /g1;
printf("y %d \n",y);
     g2=g0-y*g1;
     u2=u0-y*u1;
     v2=v0-y*v1;
     g0=g1;
     g1=g2;
     u0=u1;
     u1=u2;
     v0=v1;
     v1=v2;
end;  %end while   
x=v0;
if (x>=0),
   y=x;
   return ;
else 
   y=x+n;
end;  %end if-else
   