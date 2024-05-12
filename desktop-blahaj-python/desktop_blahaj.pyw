import pygame
import win32api
import win32con
import win32gui
import os

dir_name = os.path.dirname(__file__)

pygame.init()

#getting the size of the main monitor
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size, pygame.NOFRAME) # For borderless, use pygame.NOFRAME
running = True
clock = pygame.time.Clock()
fuchsia = (255, 0, 128)  # Transparency color
frame = 0
haj = ""

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

# Set window transparency color
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

# set window to always on top
win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

def loadframe(frame):
    if len(str(frame)) == 1:
        return pygame.image.load(dir_name + r"\frames\frame_0" + str(frame) + ".gif")
    else:
        return pygame.image.load(dir_name + r"\frames\frame_" + str(frame) + ".gif")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(fuchsia)  # Transparent background
    haj = loadframe(frame)
    screen.blit(pygame.transform.scale_by(haj, 1.5), pygame.Rect(10, screen_height -  122, 72, 72))

    pygame.display.update()
    clock.tick(30)
    frame += 1
    if frame == 60:
        frame = 0
    
pygame.quit()
