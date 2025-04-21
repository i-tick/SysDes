class BulletType:
    # flyweight class
    def __init__(self, color):
        self.color = color # intrinsic property, shared by all bullets of the same color
        print(f"BulletType created with color {self.color}")
#     # memory usage: redundant data for color "red" is stored in each bullet object

class BulletTypeFactory:
    _bullet_types = {} # cache for bullet types

    @classmethod
    def get_bullet_type(cls, color):
        if color not in cls._bullet_types:
            cls._bullet_types[color] = BulletType(color)
        return cls._bullet_types[color]
    

class Bullet:
    def __init__(self,color, x ,y, speed):
        self.bullet_type = BulletTypeFactory.get_bullet_type(color)
        self.x = x         # extrinsic property, unique to each bullet
        self.y = y         # extrinsic property, unique to each bullet
        self.speed = speed # extrinsic property, unique to each bullet
        print(f"Bullet created with color {self.bullet_type.color} at position ({self.x}, {self.y}) with speed {self.speed}")


if __name__ == "__main__":
    # Create a bullet with color "red" at position (10, 20) with speed 5
    bullet1 = Bullet("red", 10, 20, 5)
    
    # Create another bullet with color "red" at position (30, 40) with speed 10
    bullet2 = Bullet("red", 30, 40, 10)
    
    # Create a third bullet with color "red" at position (50, 60) with speed 15
    bullet3 = Bullet("red", 50, 60, 15)