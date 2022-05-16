import time
import pygame

# Global Variables
# constants
FPS = 15
HEIGHT = 720
WIDTH = 1024

HEIGHT_2_3 = 2/3 * HEIGHT
WIDTH_2_3 = 2/3 * WIDTH
HEIGHT_1_10 = 1/10 * HEIGHT
WIDTH_OVER_255 = WIDTH/255

colour = [0, 0, 0]
r, g, b = 0, 0, 0
r_mod, g_mod, b_mod = 1, 3, 2

uptime_counter = 0
uptime_text = None

pygame.init()
font = pygame.font.Font(None, 180)
font_small = pygame.font.Font(None, 20)
clock = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Time Test')
pygame.event.pump()


def update_colour():
    global colour
    global r, g, b
    global r_mod, g_mod, b_mod
    global uptime_counter, uptime_text

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

    # print difference in colour and its bounded version
    # print(r_c - r, b_c - b, g_c - g)
    colour = [r_c, g_c, b_c]

    uptime_counter += 1
    uptime_text = font_small.render(str(uptime_counter), True, (g_c, r_c, b_c), (0,0,0))
    print(uptime_counter, uptime_text)


while True:
    clock.tick(FPS)
    t = time.strftime("%H:%M:%S", time.localtime())
    t = font.render(str(t), True, (255, 255, 255), (0, 0, 0,))
    # colour_text = font.render(str(colour), True, (255, 255, 255), (0, 0, 0))
    
    pygame.event.pump()
    update_colour()
    screen.fill(colour)
    # pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0,100,100,10))
    # Rect(left, top, width, height) -> Rect
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
        r * WIDTH_OVER_255, HEIGHT_2_3, 50, HEIGHT_1_10))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
        g * WIDTH_OVER_255, HEIGHT_2_3 + HEIGHT_1_10, 50, HEIGHT_1_10))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(
        b * WIDTH_OVER_255 + 30, HEIGHT_2_3 + HEIGHT_1_10 + HEIGHT_1_10, 50, HEIGHT_1_10))
    

    screen.blit(t, (WIDTH//2 - 200, HEIGHT//2 - 200))
    screen.blit(uptime_text, (0,0))
    # screen.blit(colour_text, (0,150))

    pygame.display.update()
