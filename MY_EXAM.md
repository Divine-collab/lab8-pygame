**My thinking**
- exercise 1:
This was jsut setting certain sizes for numbered squares 

- exercise 2
This is about re_spwan with the same size
Before we did not specify the size of a respwan, I selected randomly this was my function for birth time
this is what I had 
def create_random_square(birth_time):
    """Create a new square with random properties"""
    size = random.randint(MIN_SIZE, MAX_SIZE)
    x = random.randint(0, SCREEN_WIDTH - size)
    y = random.randint(0, SCREEN_HEIGHT - size)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    speed = (MAX_SIZE - size) / (MAX_SIZE - MIN_SIZE) * MAX_SPEED
    angle = random.uniform(0, 2 * math.pi)
    velocity_x = speed * math.cos(angle)
    velocity_y = speed * math.sin(angle)
    
    if abs(velocity_x) > MAX_SPEED:
        velocity_x = MAX_SPEED if velocity_x > 0 else -MAX_SPEED
    if abs(velocity_y) > MAX_SPEED:
        velocity_y = MAX_SPEED if velocity_y > 0 else -MAX_SPEED
    
    return Square(x, y, size, color, velocity_x, velocity_y, birth_time)

- exercise 3


- exercise 4
1. checking collision by calculate the distance between two squares where distance = 0
2. if two squares colapse/meet each other
3. but here we are using pygame rect


- exercise 5
1. calculate/ check smaller and bigger squares
2. if we have collision check then bigger one eats the small one
3. for eating(the small square has to disapear) and the large one stays
4. afer that we get a respwan of the small square

- execise 6 & exercise 9
1. if the larger sqaure collide with a small one
2. smaller one dies and gets a reswap after
3. bigger one stays but enlargers
4. enlargement = self.size + the size of eaten square # not directly
5. the larger the sqaure the faster it is so the speed increases too
6. speed increases propotionaly to then squares' new size

- exercise 7
1. pygame trails of 30
2. append trails to squares by drawing
3. adjust the trials to squares size

_exercise 8
1. speed was not getting issues everytime because sizes are changing eventualy





