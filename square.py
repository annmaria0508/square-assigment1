from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Square properties
rect_x = -1.0  # Starting X position (left side of screen)
rect_y = 0.0   # Center Y position
rect_size = 0.2
speed = 0.01   # How much the square moves per frame

def init():
    # Set background color to black
    glClearColor(0.0, 0.0, 0.0, 1.0)
    # Define the 2D coordinate system from -1 to 1
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw_square():
    global rect_x
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.7, 1.0)  # Pick a nice Cyan color
    
    # Draw the square using vertices
    glBegin(GL_QUADS)
    glVertex2f(rect_x, rect_y - rect_size)
    glVertex2f(rect_x + rect_size, rect_y - rect_size)
    glVertex2f(rect_x + rect_size, rect_y + rect_size)
    glVertex2f(rect_x, rect_y + rect_size)
    glEnd()
    
    glutSwapBuffers()

def update(value):
    global rect_x
    
    # Move the square to the right
    rect_x += speed
    
    # If it goes off the right edge, wrap it back to the left
    if rect_x > 1.0:
        rect_x = -1.0 - rect_size
        
    # Mark the window for redrawing
    glutPostRedisplay()
    
    # Call this function again in 16ms (~60 FPS)
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Python OpenGL Animation")
    
    init()
    
    glutDisplayFunc(draw_square)
    glutTimerFunc(0, update, 0) # Start the animation loop
    
    glutMainLoop()

if __name__ == "__main__":
    main()