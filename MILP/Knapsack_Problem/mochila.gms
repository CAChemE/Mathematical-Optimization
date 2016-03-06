# Daniel Domene López

option optcr = 0 ;

Set i objetos /cofre, anillo, collar, espejo, brazaletes, rubi,
                 perfume, diamante, copa, azafran/
;

Parameters
         V(i) volumen de los objetos cm3
         /cofre = 1000,
          anillo = 2,
          collar = 10,
          espejo = 500,
          brazaletes = 15,
          rubi = 3,
          perfume = 100,
          diamante = 5,
          copa = 250,
          azafran = 100
         /
         M(i) masa de los objetos g
         /cofre = 2000,
          anillo = 20,
          collar = 300,
          espejo = 1000,
          brazaletes = 300,
          rubi = 75,
          perfume = 100,
          diamante = 50,
          copa = 500,
          azafran = 100
         /
         C(i) precio de mercado Dinares
         /cofre = 50,
          anillo = 5,
          collar = 3,
          espejo = 20,
          brazaletes = 16,
          rubi = 5,
          perfume = 1,
          diamante = 30,
          copa = 12,
          azafran = 40
         /
         Vmax Volumen maximo de la bolsa cm3 /2000/
         Mmax Masa maxima de la bolsa g /2500/

         L(i) numero de unidades en la cueva
         /cofre = 1,
          anillo = 10,
          collar = 1,
          espejo = 1,
          brazaletes = 15,
          rubi = 1,
          perfume = 1,
          diamante = 1,
          copa = 1,
          azafran = 1
         /
;

Integer variable
         x(i) numero de objetos de cada tipo
;

Variable
         z variable a optimizar

Equations
Objetivo
Volumen
Masa
;

Objetivo.. z =E= sum(i, x(i)*C(i))
;
Volumen..  sum(i, x(i)*V(i)) =L= Vmax
;
Masa..     sum(i, x(i)*M(i)) =L= Mmax
;

x.up(i) = L(i)
;

model mochila /all/
;

solve mochila using MIP maximizing z
;



