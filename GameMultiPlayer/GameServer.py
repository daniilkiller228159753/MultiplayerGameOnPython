
import socket
import pygame
from time import sleep
pygame.init()
s = socket.socket()
s.bind(('192.168.3.36',12345))
s.listen()
c,addr=s.accept()
winx=400
winy= 400
win = pygame.display.set_mode((winx,winy))
pygame.display.set_caption('dwada')
playerwid=50
playerhei=50
net_wid=None
net_hei=None
x = 300
h1 = False
y = 200
bullet = False
xbul = x
ybul = None
run = True
net_x = None
net_y = None
jump = False
while run:
    ##
    c.send(bytes(f't{xbul}', encoding='utf8'))
    ccwww = c.recv(1024).decode()
    c.send(bytes(f'g{y}', encoding='utf8'))
    cchhh = c.recv(1024).decode()
    ##
    #######################################
    c.send(bytes(f'w{playerwid}', encoding='utf8'))
    ccww = c.recv(1024).decode()
    c.send(bytes(f'h{playerhei}', encoding='utf8'))
    cchh = c.recv(1024).decode()
    #######################################
    c.send(bytes(f'x{x}', encoding='utf8'))
    ccx = c.recv(1024).decode()
    c.send(bytes(f'y{y}', encoding='utf8'))
    ccy = c.recv(1024).decode()
    ##########################################
    if ccww[0:1] == 'w':
        net_wid = int(ccww[1:])
    if cchh[0:1] == 'h':
        net_hei = int(cchh[1:])
    ###########################################
    if ccx[0:1] == 'x':
        net_x = int(ccx[1:])
    if ccy[0:1] == 'y':
        net_y = int(ccy[1:])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    key = pygame.key.get_pressed()
    ##
    if ccwww[0:1] == 't':
        net_xx = int(ccwww[1:])
    if cchhh[0:1] == 'g':
        net_yy = int(cchhh[1:])
    ##
    if key[pygame.K_w] and y > 0:
        y -= 1
    if key[pygame.K_s] and y < winy-playerhei :
        y += 1
    if key[pygame.K_d] and x < winx-playerwid:
        x += 1
    if key[pygame.K_a] and x > 0:
        x -= 1

    #########################
    #########################
    if h1 == True:
        xbul = x
    if xbul > winx:
        print('dwad')
        xbul = x
    if key[pygame.K_e]:
        bullet = True
        h1 = True
        h1 = False
    if xbul > 450:
        bullet = False
        xbul = x
    if bullet == True:
        xbul += 1
##################################
    win.fill((255,255,255))
    pygame.draw.rect(win,'green',[x,y,playerwid,playerhei])
    pygame.draw.rect(win, 'red', [net_x, net_y,net_wid,net_hei])
    ###############################################################
    pygame.draw.rect(win, 'black', [xbul , y, 8, 8])
    pygame.draw.rect(win, 'black', [net_xx , net_y, 8, 8])
    ################################################################
    pygame.display.update()


