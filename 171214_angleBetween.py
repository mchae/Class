
# Angle Between Two Vectors
# Using the dot product to compute the angle between two vectors

def setup():
    size(640, 360)


def draw():
    background(255)
    
    # A "vector" (really a point) to store the mouse position and screen center position
    mouseLoc = PVector(mouseX, mouseY)
    centerLoc = PVector(width/2, height/2)  
    
    # Aha, a vector to store the displacement between the mouse and center
    v = PVector.sub(mouseLoc, centerLoc)
    v.normalize()
    v.mult(75)
    
    xaxis = PVector(75, 0)
    # Render the vector
    drawVector(v, centerLoc, 1.0)
    drawVector(xaxis, centerLoc, 1.0)
    
    
    theta = PVector.angleBetween(v, xaxis)
    
    fill(0)
    #text(str(degrees(theta)) + " degrees\n", 10, 160)
    text(str(degrees(theta)) + " degrees\n" + str(theta) + " radians", 10, 160)
    

# Renders a vector object 'v' as an arrow and a position 'loc'
def drawVector(v, pos, scayl):
    pushMatrix()
    arrowsize = 6
    # Translate to position to render vector
    translate(pos.x, pos.y)
    stroke(0)
    strokeWeight(2)
    # Call vector heading function to get direction (pointing up is a heading of 0)
    rotate(v.heading2D())
    # Calculate length of vector & scale it to be bigger or smaller if necessary
    len = v.mag()*scayl
    # Draw three lines to make an arrow 
    line(0, 0, len, 0)
    line(len, 0, len-arrowsize, +arrowsize/2)
    line(len, 0, len-arrowsize, -arrowsize/2)
    popMatrix()
