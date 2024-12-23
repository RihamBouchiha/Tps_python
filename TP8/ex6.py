class Forme:
    def _init_(self, largeur, longueur):
        self.__largeur = largeur
        self.__longueur = longueur

    
    def get_largeur(self):
        return self.__largeur

    def get_longueur(self):
        return self.__longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def set_longueur(self, longueur):
        self.__longueur = longueur


class Triangle(Forme):
    def aire(self):
        return (self.get_largeur() * self.get_longueur()) / 2


class Rectangle(Forme):
    def aire(self):
        return self.get_largeur() * self.get_longueur()


class Cube(Forme):
    def _init_(self, largeur, longueur, hauteur):
        super()._init_(largeur, longueur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.get_largeur() * self.get_longueur() * self.__hauteur


if __name__ == "_main_":
    triangle = Triangle(largeur=5, longueur=10)
    rectangle = Rectangle(largeur=4, longueur=8)
    cube = Cube(largeur=3, longueur=3, hauteur=3)

    print("Aire du triangle :", triangle.aire())
    print("Aire du rectangle :", rectangle.aire())
    print("Volume du cube :", cube.volume())