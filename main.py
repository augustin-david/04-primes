"""
Module permettant de determiner des nombres premiers inférieurs à 100.
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    # votre code ici
    """
    Retourne True si p est premier, False sinon.
    """
    if p < 2:
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Applique la fonction secondaire pour afficher les nombres premiers inférieurs à 100.
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
