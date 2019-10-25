#########################################################################################################
#1. One ball
def setup():
    global x, y, xspeed, yspeed
    size(600, 600)
    x = random(width)
    y = random(height)
    
    xspeed = random(-5, 5)
    yspeed = random(-5, 5)
    print(x, y)
    
def draw():
    global x, y, xspeed, yspeed
    background(0)
    
    # show
    circle(x, y, 40)
    
    # update
    x = x + xspeed
    y = y + yspeed
    
    # if onEdge, bounce
    if x < 0 or x > width:
        xspeed  = xspeed * -1
    if y < 0 or y > height:
        yspeed  = yspeed * -1
        
    # display variables on screen
    textSize(20)
    text('x=' + str(x), 0, 20)
    text('y=' + str(y), 0, 40)
    text('xspeed=' + str(xspeed), 0, 60)
    text('yspeed=' + str(yspeed), 0, 80)

def mousePressed():
    global xspeed, yspeed
    if mouseButton == LEFT:
        xspeed += 1
        yspeed += 1
    else:
        xspeed -= 1
        yspeed -= 1
        
def keyPressed():
    global diameter
    
    if (keyCode == UP):
        diameter += 5
    if (keyCode == DOWN):
        diameter -= 5 

#########################################################################################################
#2. Two balls
def setup():
    global x1, y1, xspeed1, yspeed1
    global x2, y2, xspeed2, yspeed2
    size(600, 600)
    x1 = random(width)
    y1 = random(height)
    
    x2 = random(width)
    y2 = random(height)
    
    xspeed1 = random(-5, 5)
    yspeed1 = random(-5, 5)
    
    xspeed2 = random(-5, 5)
    yspeed2 = random(-5, 5)
    
def draw():
    global x1, y1, xspeed1, yspeed1
    global x2, y2, xspeed2, yspeed2
    background(0)
    
    # show
    circle(x1, y1, 40)
    circle(x2, y2, 40)
    
    # update
    x1 = x1 + xspeed1
    y1 = y1 + yspeed1
    
    x2 = x2 + xspeed2
    y2 = y2 + yspeed2
    
    # if onEdge, bounce
    if x1 < 0 or x1 > width:
        xspeed1  = xspeed1 * -1
    if y1 < 0 or y1 > height:
        yspeed1  = yspeed1 * -1
        
    if x2 < 0 or x2 > width:
        xspeed2  = xspeed2 * -1
    if y2 < 0 or y2 > height:
        yspeed2  = yspeed2 * -1

#########################################################################################################
#3 . Line between balls
# 1. Line between balls

stroke(frameCount % 256)	# What does this mean?
line(x1, y1, x2, y2)

# 2. Smooth transition of color, 
# in setup():
col = 0
direction = 1

# in draw():
stroke(col)			# What is the range of col?
strokeWeight(4)
col = col + direction

line(x1, y1, x2, y2)
    
if col < 0 or col > 255:
direction = direction * -1

# if onEdge, bounce		# Change backgroud when ball1 hits wall
if x1 < 0 or x1 > width:
xspeed1  = xspeed1 * -1
background(0)
