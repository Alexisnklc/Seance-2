from math import *

class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator=numerator
        self.denominator=denominator
    def __str__(self):
        return f'{self.numerator} / {self.denominator}'
    def numerator(self):
        return self.numerator
    def set_numerator(self, new_numerator):
            if not isinstance(new_numerator, int):
                raise ValueError('Le numérateur doit être un entier')
    def set_denominator(self, new_denominator):
        if new_denominator !=0:
            raise ValueError('Le dénominateur doit être non nul')

    def add(self, other: 'Fraction'):
        '''args : self et other, les deux fractions à additionner
        returns : la somme des deux fractions'''

        return Fraction(self.numerator*other.denominator+self.denominator*other.numerator,self.denominator*other.denominator)

    def mult(self, other:'Fraction'):
        '''args : les deux fractions à multiplier
        returns : le produit des deux fractions'''
        return Fraction(self.numerator*other.numerator,self.denominator*other.denominator)

    def simplify(self):
        '''args : la fraction réductible
        returns : la même fraction mais irréductible'''
        a,b=self.numerator,self.denominator
        while b !=0:
            a,b=b,a%b
        return Fraction(self.numerator//a,self.denominator//a)

    def __eq__(self, other:'Fraction'):
        '''compare deux fractions qui n'ont pas été simplifiées'''
        return self.numerator*other.denominator==self.denominator*other.numerator



if __name__=='__main__':
    assert Fraction(1, 2).add(Fraction(1, 3))==Fraction(5, 6)
    assert Fraction(1, 2).mult(Fraction(1, 3))==Fraction(1, 6)
    assert Fraction(4, 8).simplify()==Fraction(1, 2)


#Exercice 3
    sum=Fraction(0,1)
    for i in range(1,10001):
        sum=sum.add(Fraction(1,i))
    sum=sum.simplify()
    print (somme.x/somme.y)

#Exercice 4

    leibniz=Fraction(0,1)
    for i in range(10001):
        leibniz=leibniz.add(Fraction((-1)**i, 2*i+1))
    leibniz=leibniz.simplify()
    X=(leibniz.numerator/leibniz.denominator)
    print(X)
    print(X-pi/4) #vérification que la valeur obtenur est très proche de pi/4







