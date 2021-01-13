# MIT License

# Copyright (c) 2021 OldGameBox

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

__name__ = "HiPPe Engine"
__version__ = "0.1.1"
__author__ = "OldGameBox Polus"

import pygame
import math
import tkinter as tk
from tkinter import filedialog
import os
import win32gui, win32con

root = tk.Tk()
root.withdraw()

global running
running=True
getTicksLastFrame=0

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
PINK=(255,0,255)
GRAY=(127,127,127)

K_UP = pygame.K_UP
K_DOWN = pygame.K_DOWN
K_LEFT = pygame.K_LEFT
K_RIGHT = pygame.K_RIGHT
K_W = pygame.K_w
K_D = pygame.K_d
K_A = pygame.K_a
K_S = pygame.K_s
K_Q = pygame.K_q
K_E = pygame.K_e
K_R = pygame.K_r
K_T = pygame.K_t
K_Y = pygame.K_y
K_U = pygame.K_u
K_I = pygame.K_i
K_O = pygame.K_o
K_P = pygame.K_p
K_F = pygame.K_f
K_G = pygame.K_g
K_H = pygame.K_h
K_J = pygame.K_j
K_K = pygame.K_k
K_L = pygame.K_l
K_Z = pygame.K_z
K_X = pygame.K_x
K_C = pygame.K_c
K_V = pygame.K_v
K_B = pygame.K_b
K_N = pygame.K_n
K_M = pygame.K_m
K_LSHIFT = pygame.K_LSHIFT
K_RSHIFT = pygame.K_RSHIFT
K_LCTRL = pygame.K_LCTRL
K_RCTRL = pygame.K_RCTRL
K_ESC = pygame.K_ESCAPE
K_LALT = pygame.K_LALT
K_RALT = pygame.K_RALT
K_ENTER = pygame.K_RETURN
K_1 = pygame.K_1
K_2 = pygame.K_2
K_3 = pygame.K_3
K_4 = pygame.K_4
K_5 = pygame.K_5
K_6 = pygame.K_6
K_7 = pygame.K_7
K_8 = pygame.K_8
K_9 = pygame.K_9
K_0 = pygame.K_0

def HideDebbuger():
    win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)

class Vector:
    x=0
    y=0
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Sprite:
    path=""
    position = Vector(0,0)
    scale=(0,0)
    rotation=0
    def __init__(self,path,vector,scale, rotation):
        self.position = vector
        self.path=path
        self.scale=scale
        self.rotation=rotation

class ColliderRect:
    position = Vector(0,0)
    width=0
    height=0
    scale=(0,0)
    rotation=0
    def __init__(self,Vector,width,height,scale,rotation):
        self.position = Vector
        self.scale = scale
        self.rotation = rotation
        self.width=width
        self.height=height

class Button:
    position = Vector(0,0)
    width = 0
    height = 0
    rotation = 0
    color = (0,0,0)
    text = ""
    text_color = (0,0,0)
    fontpath = ""
    fontsize = 0
    antialias = True
    
    def __init__(self,position,width,height,rotation,color,text,text_color,fontpath,fontsize,antialias):
        self.position = position
        self.width = width
        self.height = height
        self.rotation = rotation
        self.text = text
        self.color = color
        self.text_color = text_color
        self.fontpath = fontpath
        self.fontsize = fontsize
        self.antialias = antialias
    

def init(width,height,APP_NAME,Enable_Music):
    pygame.init()
    os.system("cls")
    if Enable_Music:
        pygame.mixer.init()
    global screen
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption(APP_NAME)
    global clock
    clock = pygame.time.Clock()

def OnExit():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def SetWindowIcon(path):
    pygame.display.set_icon(pygame.image.load(path))

def Drawing():
    return running

def Exit():
    pygame.quit()

def Quit():
    global running
    running=False

def Clear():
    screen.fill(BLACK)

def Fill(color):
    screen.fill(color)

def Line(color,Vector,width):
    pygame.draw.line(screen,color,Vector.x,Vector.y,width)

def Render():
    pygame.display.flip()
    pygame.display.update()

def Delta():
    global getTicksLastFrame
    t = pygame.time.get_ticks()
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t
    return deltaTime

def GetFPS():
    return str(int(clock.get_fps()))

def DrawSprite(Sprite):
    image = pygame.image.load(Sprite.path)
    image = pygame.transform.scale(image, (Sprite.scale[0]*image.get_width(),Sprite.scale[1]*image.get_height()))
    image = pygame.transform.rotate(image, -Sprite.rotation)
    image_rect = image.get_rect(center = image.get_rect(center=(Sprite.position.x,Sprite.position.y)).center)
    screen.blit(image,image_rect)

def DrawRect(left,top,width,height,color):
    pygame.draw.rect(screen, color, pygame.Rect(left,top,width,height))

def CollideWith(object,list):
    res=[]
    if isinstance(object, ColliderRect):
        col1 = pygame.Rect(object.position.x-(object.width/2),object.position.y-(object.height/2),object.width*object.scale[0],object.height*object.scale[1])
        #col1 = pygame.transform.rotate(col1,-object.rotation)
    for i in range(len(list)):
        if isinstance(list[i], ColliderRect):
            col2 = pygame.Rect(list[i].position.x-(list[i].width/2),list[i].position.y-(list[i].height/2),list[i].width*list[i].scale[0],list[i].height*list[i].scale[1])
            #col2 = pygame.transform.rotate(col2,-list[i].rotation)
            if col1.colliderect(col2):
                res.append(True)
            else:
                res.append(False)
    return res
def DrawCollider(object):
    if isinstance(object, ColliderRect):
        col = pygame.Surface((object.width,object.height), pygame.SRCALPHA)   # per-pixel alpha
        col.fill((150,150,150,128))                         # notice the alpha value in the color
        screen.blit(col, (object.position.x-(object.width/2),object.position.y-(object.height/2)))
                
def NormalizeVector(vector,speed,rotation):
    new_x = vector.x + (speed*math.cos(math.radians(rotation)))
    new_y = vector.y + (speed*math.sin(math.radians(rotation)))
    return Vector(new_x,new_y)

def FPSLimit(FPS):
    clock.tick(FPS)

def ButtonDown(Button):
    if pygame.key.get_pressed()[Button]:
        return True
    else:
        return False

def DrawButton(Button):
    but = pygame.Surface((Button.width,Button.height))
    but.fill(Button.color)
    screen.blit(but,(Button.position.x-(Button.width/2),Button.position.y-(Button.height/2)))
    font = pygame.font.Font(Button.fontpath,Button.fontsize)
    text = font.render(str(Button.text),Button.antialias,Button.text_color)
    text = pygame.transform.rotate(text,-Button.rotation)
    screen.blit(text,(Button.position.x-(text.get_width()/2),Button.position.y-(text.get_height()/2)))

def ButtonClick(Button,mouse_button):
    if pygame.mouse.get_pressed()[mouse_button-1]:
        but = pygame.Rect(Button.position.x-(Button.width/2),Button.position.y-(Button.height/2),Button.width,Button.height)
        if but.collidepoint(pygame.mouse.get_pos()):
            return True
        else: return False
    else: return False


def Text(text,Vector,color,rotation,fontpath,fontsize,antialias,center):
    font = pygame.font.Font(fontpath,fontsize)
    text = font.render(str(text),antialias,color)
    text = pygame.transform.rotate(text,-rotation)
    if center:
        screen.blit(text,text.get_rect(center = text.get_rect(center=(Vector.x,Vector.y)).center))
    elif not center:
        screen.blit(text,(Vector.x,Vector.y))

def SmartMove(player_vector,speed,wasd):
    if not wasd:
        if ButtonDown(K_RIGHT) and not ButtonDown(K_UP) or ButtonDown(K_RIGHT) and not ButtonDown(K_DOWN):
            player_vector.x+=speed
        if ButtonDown(K_RIGHT) and ButtonDown(K_UP) or ButtonDown(K_RIGHT) and ButtonDown(K_DOWN):
            if ButtonDown(K_UP):
                player_vector.x+=speed/2
                player_vector.y-=speed/2
            if ButtonDown(K_DOWN):
                player_vector.x+=speed/2
                player_vector.y+=speed/2
        if ButtonDown(K_RIGHT) and  ButtonDown(K_UP) and ButtonDown(K_DOWN):
            player_vector.x += speed
        if ButtonDown(K_LEFT) and not ButtonDown(K_UP) or ButtonDown(K_LEFT) and not ButtonDown(K_DOWN):
            player_vector.x-=speed
        if ButtonDown(K_LEFT) and ButtonDown(K_UP) or ButtonDown(K_LEFT) and ButtonDown(K_DOWN):
            if ButtonDown(K_UP):
                player_vector.x-=speed/2
                player_vector.y-=speed/2
            if ButtonDown(K_DOWN):
                player_vector.x-=speed/2
                player_vector.y+=speed/2
        if ButtonDown(K_LEFT) and  ButtonDown(K_UP) and ButtonDown(K_DOWN):
            player_vector.x += speed
        if not ButtonDown(K_LEFT) and ButtonDown(K_UP) or not ButtonDown(K_RIGHT) and ButtonDown(K_UP):
            player_vector.y-=speed
        if not ButtonDown(K_LEFT) and ButtonDown(K_DOWN) or not ButtonDown(K_RIGHT) and ButtonDown(K_DOWN):
            player_vector.y+=speed
    else:
        if ButtonDown(K_D) and not ButtonDown(K_W) or ButtonDown(K_D) and not ButtonDown(K_S):
            player_vector.x+=speed
        if ButtonDown(K_D) and ButtonDown(K_W) or ButtonDown(K_D) and ButtonDown(K_S):
            if ButtonDown(K_W):
                player_vector.x+=speed/2
                player_vector.y-=speed/2
            if ButtonDown(K_S):
                player_vector.x+=speed/2
                player_vector.y+=speed/2
        if ButtonDown(K_D) and  ButtonDown(K_W) and ButtonDown(K_S):
            player_vector.x += speed
        if ButtonDown(K_A) and not ButtonDown(K_W) or ButtonDown(K_A) and not ButtonDown(K_S):
            player_vector.x-=speed
        if ButtonDown(K_A) and ButtonDown(K_W) or ButtonDown(K_A) and ButtonDown(K_S):
            if ButtonDown(K_W):
                player_vector.x-=speed/2
                player_vector.y-=speed/2
            if ButtonDown(K_S):
                player_vector.x-=speed/2
                player_vector.y+=speed/2
        if ButtonDown(K_A) and  ButtonDown(K_W) and ButtonDown(K_S):
            player_vector.x += speed
        if not ButtonDown(K_A) and ButtonDown(K_W) or not ButtonDown(K_D) and ButtonDown(K_W):
            player_vector.y-=speed
        if not ButtonDown(K_A) and ButtonDown(K_S) or not ButtonDown(K_D) and ButtonDown(K_S):
            player_vector.y+=speed

def GetFolder():
    folder = filedialog.askdirectory()
    return folder

def GetFile():
    file = filedialog.askopenfile()
    return file