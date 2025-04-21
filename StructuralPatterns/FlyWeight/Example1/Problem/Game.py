class Bullet:
    def __init__(self, color,x ,y, speed):
        self.color = color # intrensic property, shared by all bullets of the same color
        self.x = x         # extrinsic property, unique to each bullet
        self.y = y         # extrinsic property, unique to each bullet
        self.speed = speed # extrinsic property, unique to each bullet
        print(f"Bullet created with color {self.color} at position ({self.x}, {self.y}) with speed {self.speed}")


if __name__ == "__main__":
    # Create a bullet with color "red" at position (10, 20) with speed 5
    bullet1 = Bullet("red", 10, 20, 5)
    
    # Create another bullet with color "red" at position (30, 40) with speed 10
    bullet2 = Bullet("red", 30, 40, 10)
    
    # Create a third bullet with color "red" at position (50, 60) with speed 15
    bullet3 = Bullet("red", 50, 60, 15)

    # memory usage: redundant data for color "red" is stored in each bullet object
    # instead of sharing the color property across all bullets