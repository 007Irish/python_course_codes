class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def print_point(self):
        return f"x is {self.x} and y is {self.y}"
    
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def __sub__(self, p):
        return Point((self.x - p.x), (self.y - p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2)
p = p1 + p2
p = p1 - p2

print(p.print_point())  # Output: x is 9 and y is 5