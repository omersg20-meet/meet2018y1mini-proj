
import turtle
import random #We'll need this later in the lab
import time


turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for piece_number in range(START_LENGTH) :
    x_pos=snake.pos()[0]#Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE
    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    DJ = snake.stamp()
    stamp_list.append(DJ)
    
UP_ARROW = "Up" #Make sure you pay attention to upper and lower
 #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 1
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
DOWN=2
LEFT=3
RIGH=4
direction = UP

def UP():
    global direction #snake direction is global (same everywhere)
    direction= UP #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the up key!")
    
def DOWN():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the down key!")
    
def LEFT():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the left key!")

def RIGHT():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
 #Update the snake drawing <- remember me later
    print("You pressed the right key!")
#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(UP, UP_ARROW) # Create listener for up key
turtle.onkeypress(DOWN, DOWN_ARROW)
turtle.onkeypress(LEFT, LEFT_ARROW)
turtle.onkeypress(RIGHT, RIGHT_ARROW)
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    global food_stamps, food_pos
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
        print("Reached")                            #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
    
    #HINT: This if statement may be useful for Part 8

    ...
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
    turtle.ontimer(move_snake,TIME_STEP) #<--Last line of function
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)

    elif direction==UP:
        snake.goto(x_pos, y_pos+ SQUARE_SIZE)

        
    elif direction==DOWN:
        snake.goto(x_pos, y_pos- SQUARE_SIZE)
        
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    if  x_pos>= RIGHT_EDGE:
        print("You DEAD")
        time.sleep(2)
        quit()
    if  x_pos<= LEFT_EDGE:
        print("You DEAD!")
        time.sleep(2)
        quit()
    if  y_pos>= UP_EDGE:
        print("DEAD")
        time.sleep(2)
        quit()
    if  y_pos<= DOWN_EDGE:
        print("You DEAD!")
        time.sleep(2)
        quit()

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    time.sleep(0.002)
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tailS
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)

    if len(food_stamps) < 6 :
        make_food()
    
    #time.sleep(0.02)

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

food = turtle.clone()
screen = turtle.getscreen()
screen.register_shape("trash.gif")


food.shape("trash.gif")
def make_food():
    global food_pos
    global food_stamps
    food.clearstamps()
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    foodposy = (food_x,food_y)
    
    food.goto(food_x,food_y)

    food_pos.append(foodposy)

    food_stamps.append(food.stamp())
    
for this_food_pos in food_pos :
    food.goto(this_food_pos[0],this_food_pos[1])
    food_stamps.append(food.stamp())
  
food.ht()

    
        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

     #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it

# in the same folder as this Python script
#make_food()
move_snake()

#Locations of food


# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!

