class Snake:

    def __init__(self, health, colour, x, y):
        self.health = health
        self.colour = colour
        self.x = x
        self.y = y

    def move(self, direction, steps):
        print(f"moveing snake in direction {direction} for {steps} steps")

    def print(self):
        print(f"health: {self.health} colour: {self.colour} x: {self.x} y: {self.y}")

    def __str__(self):
        return f"health: {self.health} colour: {self.colour} x: {self.x} y: {self.y}"

snakes = []

for i in range(10):
    newSnake = Snake(100, "red", i, i)
    snakes.append(newSnake)

for snake in snakes:
    print(snake)
    #print(snake.print())

for snake in snakes:
    print(snake.colour)

newAttribute = "foodLevel"

hasNew = hasattr(snakes[0], newAttribute)
print(hasNew)

if not hasNew:
    setattr(snakes[0], newAttribute, "80")
    print(getattr(snakes[0], newAttribute))
    delattr(snakes[0], newAttribute)

