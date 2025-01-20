''' Calculate area, volume, perimeter, and surface area'''


def area(l,w):
    return l*w

def perimeter(l,w):
    return 2*(l+w)

def surfaceArea(l,w,h):
    return 2*(l*w+w*h+h*l)

def volume(l,w,h):
    return l*w*h

 
l=int(input('Length:'))
w=int(input('Width:'))
h=int(input('Height:'))
print("area: ",area(l,w))
print("perimeter: ",perimeter(l,w))
print("surface area: ",surfaceArea(l,w,h))
print("Volume: ", volume(l,w,h))

 