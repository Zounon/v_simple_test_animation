import pygame, time, sys

### User Preference Variables ###

# set background to a constant colour, set in (R,G,B) format Ex: (100,255,0)
constant_colour = None

# Set to True ensures colours never get darker than light grey, (100,100,100)
no_dark_colours = True 

# FPS stands for Frames per Second, Box speed and colour value are directly proportional
# to FPS. So higher FPS means faster moving boxes and faster changing colours 
FPS = 30

# Custom screen size, set to True if desired otherwise will detect fullscreen resolution
use_custom_size = True 
HEIGHT = 1080/2 
WIDTH = 1920/2 
FONT_SIZE = 180
BOX_WIDTH = 100
BOX_HEIGHT = 200 


### End of User Preferences ###


pygame.init()
font = pygame.font.Font(None, FONT_SIZE)
clock = pygame.time.Clock()

if use_custom_size:
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
else:
    info_obj = pygame.display.Info()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    HEIGHT = info_obj.current_h
    WIDTH = info_obj.current_w 

    

# init some more constants
HEIGHT_1_3 = 1/3 * HEIGHT
HEIGHT_2_3 = 2/3 * HEIGHT
WIDTH_2_3 = 2/3 * WIDTH
HEIGHT_1_10 = 1/10 * HEIGHT
WIDTH_OVER_255 = WIDTH/255
colour = [0, 0, 0]
r, g, b = 0, 0, 0
r_mod, g_mod, b_mod = 1/2, 3/2, 1

current_time = time.strftime("%H:%M:%S", time.localtime())
time_text = font.render(str(current_time), True, (255, 255, 255), (0, 0, 0))
text_box_pos = (WIDTH//2 - time_text.get_size()[0]//2, HEIGHT_1_3)
first_box_pos = HEIGHT_1_3 + time_text.get_size()[1]
second_box_pos = first_box_pos + BOX_HEIGHT
third_box_pos = second_box_pos + BOX_HEIGHT

pygame.display.set_caption('Time Test')
pygame.event.pump()

def update_colour():
    global colour
    global r, g, b
    global r_mod, g_mod, b_mod

    r += r_mod
    b += b_mod
    g += g_mod

    if r > 255 or r < 0:
        r_mod = (-1) * r_mod

    if g > 255 or g < 0:
        g_mod = (-1) * g_mod

    if b > 255 or b < 0:
        b_mod = (-1) * b_mod

    # bounds checking
    r_c = min(max(r, 0), 255)
    b_c = min(max(b, 0), 255)
    g_c = min(max(g, 0), 255)

    if no_dark_colours:
        r_c = min(max(r, 100), 255)
        b_c = min(max(b, 100), 255)
        g_c = min(max(g, 100), 255)

    if constant_colour is None:
        colour = [r_c, g_c, b_c]
    else:
        colour = constant_colour


while True:
    clock.tick(FPS)
    current_time = time.strftime("%H:%M:%S", time.localtime())
    time_text = font.render(str(current_time), True, (255, 255, 255), (0, 0, 0))
    
    pygame.event.pump()
    update_colour()

    screen.fill(colour)

    # Draw the moving rectangles 
    # pyagame.draw.rect(surface, colour, rect)
    #   Pygame.Rect(left, top, width, height)
    pygame.draw.rect(screen, (0, 0, 0), 
        pygame.Rect(r * WIDTH_OVER_255, first_box_pos, BOX_WIDTH, BOX_HEIGHT))

    pygame.draw.rect(screen, (0, 0, 0), 
        pygame.Rect(g * WIDTH_OVER_255, second_box_pos, BOX_WIDTH, BOX_HEIGHT))

    pygame.draw.rect(screen, (0, 0, 0), 
        pygame.Rect(b * WIDTH_OVER_255, third_box_pos, BOX_WIDTH, BOX_HEIGHT))
    
    screen.blit(time_text, text_box_pos)


    # Handle user quit
    for event in pygame.event.get():
        # if event.type == QUIT:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == (pygame.key.get_mods and pygame.KMOD_CTRL and pygame.K_c):
                pygame.quit()
                sys.exit()
        
    # update the display after changes have been made
    pygame.display.update()