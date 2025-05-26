
class triangulo:
    def __init__(self,ladoa,ladob,ladoc):
        self.ladoa = ladoa
        self.ladob = ladob
        self.ladoc = ladoc
        
    
    def area_triangulo(self):
        semi_area = ((self.ladoa + self.ladob + self.ladoc)/2)
        area = (semi_area*(semi_area - self.ladoa)*(semi_area - self.ladob)*(semi_area - self.ladoc))
        print(f" area igual a {area**0.5:.2f}")
    
triangulo1 = triangulo(20,20,30)
triangulo1.area_triangulo()
    