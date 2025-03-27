import pygame
from modules.customColors import customColors as cc

def text_to_screen(screen, text, x, y, size=10, color=None, font_type=None):
    #pygame.display.update()
    '''Uses the color argument to distinguish b/w an int or a string passed in the field'''
    if color == None: color = cc.colorlist[text]
    text = str(text)
    if font_type == None:
        font = pygame.font.SysFont('C:/Users/LENOVO/BASESTATION - R2C - WARRIOR (coba)/assets/Consolas.ttf', size, True)
    else:
        font = font_type
    text_width, text_height = font.size(text)
    text = font.render(text, True, color)
    tRect = screen.blit(text, (x - (text_width / 2), y - (text_height / 2)))
    # pygame.display.update()
    return tRect
    
