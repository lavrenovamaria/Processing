def setup():
    size(800, 200)
def draw():
    if mousePressed:
        fill(0,0,255)
    else:
        fill(255,64,64)
    ellipse(mouseX, mouseY, 80, 80)