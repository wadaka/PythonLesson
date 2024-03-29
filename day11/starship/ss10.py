import pygame
import sys
import math
import random
from pygame.locals import *

# 画像の読み込み
img_galaxy=pygame.image.load("image_gl/galaxy.png")
img_sship=[
    pygame.image.load("image_gl/starship.png"),
    pygame.image.load("image_gl/starship_l.png"),
    pygame.image.load("image_gl/starship_r.png"),
    pygame.image.load("image_gl/starship_burner.png"),
]
img_weapon=pygame.image.load("image_gl/bullet.png")
img_enemy=[
        pygame.image.load("image_gl/enemy0.png"),
        pygame.image.load("image_gl/enemy1.png"),
]
img_explode=[
        None,
        pygame.image.load("image_gl/explosion1.png"),
        pygame.image.load("image_gl/explosion2.png"),
        pygame.image.load("image_gl/explosion3.png"),
        pygame.image.load("image_gl/explosion4.png"),
        pygame.image.load("image_gl/explosion5.png"),
]
tmr=0 
bg_y = 0

ss_x = 480
ss_y = 360
ss_d = 0 
key_spc = 0
key_z = 0

MISSILE_MAX = 200
msl_no = 0
msl_f = [False]*MISSILE_MAX
msl_x = [0]*MISSILE_MAX
msl_y = [0]*MISSILE_MAX
msl_a = [0]*MISSILE_MAX

ENEMY_MAX = 100
emy_no = 0
emy_f = [False]*ENEMY_MAX
emy_x = [0]*ENEMY_MAX
emy_y = [0]*ENEMY_MAX
emy_a = [0]*ENEMY_MAX
emy_type = [0]*ENEMY_MAX
emy_speed = [0]*ENEMY_MAX

EMY_BULLET = 0
LINE_T=-80
LINE_B=800
LINE_L=-80
LINE_R=1040

EFFECT_MAX = 100
eff_no = 0
eff_p = [0]*EFFECT_MAX
eff_x = [0]*EFFECT_MAX
eff_y = [0]*EFFECT_MAX

def get_dis(x1,y1,x2,y2):
    return ((x1-x2)**2+ (y1-y2)**2)

def move_starship(scrn, key): # 自機の移動
    global ss_x, ss_y, ss_d,key_spc,key_z
    ss_d=0
    if key[K_UP] == 1:
        ss_y = ss_y - 20
        if ss_y < 80:
           ss_y = 80
    if key[K_DOWN] == 1:
        ss_y = ss_y + 20
        if ss_y > 640:
            ss_y = 640
    if key[K_LEFT] == 1:
        ss_d = 1
        ss_x = ss_x - 20
        if ss_x < 40:
            ss_x = 40
    if key[K_RIGHT] == 1:
        ss_d = 2
        ss_x = ss_x + 20
        if ss_x > 920:
            ss_x = 920

    key_spc = (key_spc+1) * key[K_SPACE]
    if key_spc%5 == 1:
        set_missile(0)
    key_z = (key_z+1)*key[K_z]
    if key_z == 1:
        set_missile(10)
    scrn.blit(img_sship[3], [ss_x-8, ss_y+40+(tmr%3)*2])
    scrn.blit(img_sship[ss_d], [ss_x-37, ss_y-48])

def set_missile(typ):
    global msl_no
    if typ == 0:
        msl_f[msl_no]=True
        msl_x[msl_no]=ss_x
        msl_y[msl_no]=ss_y-50
        msl_a[msl_no]=270
        msl_no = (msl_no+1)%MISSILE_MAX
    if typ == 10:
        for a in range(160,390,10):
            msl_f[msl_no]=True
            msl_x[msl_no]=ss_x
            msl_y[msl_no]=ss_y-50
            msl_a[msl_no]=a
            msl_no = (msl_no+1)%MISSILE_MAX

def move_missile(scrn):
    for i in range(MISSILE_MAX):
        if msl_f[i] == True:
            msl_x[i]=msl_x[i]+36*math.cos(math.radians(msl_a[i]))
            msl_y[i]=msl_y[i]+36*math.sin(math.radians(msl_a[i]))
            img_rz=pygame.transform.rotozoom(img_weapon,-90-msl_a[i],1.0)
            scrn.blit(img_rz,[msl_x[i]-img_rz.get_width()/2,msl_y[i]-img_rz.get_height()/2])
            if msl_y[i] < 0 or msl_x[i] < 0 or msl_x[i]>960:
                msl_f[i]=False

def bring_enemy():
    if tmr % 30 == 0:
        set_enemy(random.randint(20,940),LINE_T,90,1,6)

def set_enemy(x,y,a,ty,sp):
    global emy_no
    while True:
        if emy_f[emy_no]==False:
            emy_f[emy_no]=True
            emy_x[emy_no]=x
            emy_y[emy_no]=y
            emy_a[emy_no]=a
            emy_type[emy_no]=ty
            emy_speed[emy_no]=sp
            break
        emy_no=(emy_no+1)%ENEMY_MAX

def move_enemy(scrn):
    for i in range(ENEMY_MAX):
        if emy_f[i] == True:
            ang = -90-emy_a[i]
            png = emy_type[i]
            emy_x[i] = emy_x[i]+emy_speed[i]*math.cos(math.radians(emy_a[i]))
            emy_y[i] = emy_y[i]+emy_speed[i]*math.sin(math.radians(emy_a[i]))
            if emy_type[i] == 1 and emy_y[i] > 360:
                set_enemy(emy_x[i],emy_y[i],90,0,8)
                emy_a[i]=-45
                emy_speed[i]=16
            if emy_x[i] < LINE_L or LINE_R < emy_x[i] or emy_y[i] < LINE_T or LINE_B < emy_y[i]:
                emy_f[i] = False
            if emy_type[i] !=EMY_BULLET:
                w=img_enemy[emy_type[i]].get_width()
                h=img_enemy[emy_type[i]].get_height()
                r=int((w+h)/4)+12
                for n in range(MISSILE_MAX):
                    if msl_f[n] == True and get_dis(emy_x[i],emy_y[i],msl_x[n],msl_y[n]) < r **2:
                        msl_f[n] = False
                        set_effect(emy_x[i],emy_y[i])
                        emy_f[i] = False
            img_rz=pygame.transform.rotozoom(img_enemy[png],ang,1.0)
            scrn.blit(img_rz,[emy_x[i]-img_rz.get_width()/2,emy_y[i]-img_rz.get_height()/2])
def set_effect(x,y):
    global eff_no
    eff_p[eff_no]=1
    eff_x[eff_no]=x
    eff_y[eff_no]=y
    eff_no=(eff_no+1) % EFFECT_MAX

def draw_effect(scrn):
    for i in range(EFFECT_MAX):
        if eff_p[i] > 0:
            scrn.blit(img_explode[eff_p[i]],[eff_x[i]-48,eff_y[i]-48])
            eff_p[i] += 1
            if eff_p[i] == 6:
                eff_p[i] = 0

def main(): # メインループ
    global tmr,bg_y

    pygame.init()
    pygame.display.set_caption("Galaxy Lancer")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screen = pygame.display.set_mode((960, 720), FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == K_ESCAPE:
                    screen = pygame.display.set_mode((960, 720))

        # 背景のスクロール
        bg_y = (bg_y+16)%720
        screen.blit(img_galaxy, [0, bg_y-720])
        screen.blit(img_galaxy, [0, bg_y])

        key = pygame.key.get_pressed()
        move_starship(screen, key)
        move_missile(screen)
        bring_enemy()
        move_enemy(screen)
        draw_effect(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
