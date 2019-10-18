#####################################################################################################
# 1. Grids
scl = 20
w = 600
h = 400

def setup():
    global rows, cols
    size(800, 800)
   
    rows = h / scl
    cols = w / scl
   
   
def draw():
    background(0)
    stroke(255)
    noFill()
   
    for y in range(rows):
        for x in range(cols):
            rect(x*scl, y*scl, scl, scl)
            
#####################################################################################################
# 2. Triangles
scl = 20
w = 600
h = 400

def setup():
    global rows, cols
    size(800, 800)
   
    rows = h / scl
    cols = w / scl
   
def draw():
    background(0)
    stroke(255)
    noFill()
   
    for y in range(rows):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl)
            vertex(x*scl, (y+1)*scl)
        endShape()
#####################################################################################################
# 3 Translation & Lotation
scl = 20
w = 600
h = 600

def setup():
    global rows, cols
    size(600, 600, P3D)
   
    rows = h / scl
    cols = w / scl
   
def draw():
    background(0)
    stroke(255)
    noFill()
   
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-w/2, -h/2)
   
    for y in range(rows):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl)
            vertex(x*scl, (y+1)*scl)
        endShape()
#####################################################################################################
# 4. Static terrain
scl = 20
w = 1200
h = 900

def setup():
    global rows, cols, terrain
    size(600, 600, P3D)
   
    rows = h / scl
    cols = w / scl
    print(rows, cols)
    
    terrain = [[0 for y in range(rows)] for x in range(cols)]
    
    for y in range(rows):
        for x in range(cols):
            terrain[x][y] = random(-20, 20)
    
def draw():
    background(0)
    stroke(255)
    noFill()
   
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-w/2, -h/2)
   
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
        
    noLoop()
#####################################################################################################
# 5. Smooth terrain
scl = 20
w = 1200
h = 900

def setup():
    global rows, cols, terrain
    size(600, 600, P3D)
   
    rows = h / scl
    cols = w / scl
    print(rows, cols)

    terrain = [[0 for y in range(rows)] for x in range(cols)]
    
    yoff = 0
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -100, 100)
            xoff += 0.2
        yoff += 0.2
    
def draw():
    background(0)
    stroke(255)
    noFill()
   
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-w/2, -h/2)
   
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
        
    noLoop()
#####################################################################################################
# 6. Final
scl = 20
w = 1200
h = 900
flying = 0

def setup():
    global rows, cols, terrain
    size(600, 600, P3D)
   
    rows = h / scl
    cols = w / scl
    print(rows, cols)

    terrain = [[0 for y in range(rows)] for x in range(cols)]
    
    
def draw():
    global terrain, flying
    flying -= 0.1
    yoff = flying
    for y in range(rows):
        xoff = 0
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -100, 100)
            xoff += 0.2
        yoff += 0.2
    
   
    background(0)
    stroke(255)
    noFill()
   
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-w/2, -h/2)
   
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
        
