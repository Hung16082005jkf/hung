import pygame
import time
import math
pygame.mixer.init()
pygame.init()

man_hinh=pygame.display.set_mode((500,600))
RED=(255,0,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,204)
chu=pygame.font.SysFont("sans", 70)
so=pygame.font.SysFont("sans", 50)
text_1=chu.render("+",True,BLACK)
text_2=chu.render("-",True,BLACK)
text_3=chu.render("+",True,BLACK)
text_4=chu.render("-",True,BLACK)
text_5=chu.render("start",True,BLACK)
text_6=chu.render("reset",True,BLACK)
text_9=so.render(":",True,BLACK)
tong_phut=0
tong_giay=1
giay=60
am = pygame.mixer.Sound("baothuc.mp3")

# chuong=pygame.mixer.Sound('Tieng-chuong-bao-chay-www_tiengdong_com.mp3')
# chuong = pygame.mixer.Sound('sounds/Tieng-chuong-bao-chay-www_tiengdong_com.mp3')


run_1=False
run=True
while run:
    man_hinh.fill(RED)
    pygame.draw.rect(man_hinh,WHITE,(50,50,50,50))
    pygame.draw.rect(man_hinh,WHITE,(150,50,50,50))
    pygame.draw.rect(man_hinh,WHITE,(50,150,50,50))
    pygame.draw.rect(man_hinh,WHITE,(150,150,50,50))
    pygame.draw.rect(man_hinh,WHITE,(250,50,200,50))
    pygame.draw.rect(man_hinh,WHITE,(250,150,200,50))
    pygame.draw.rect(man_hinh,BLACK,(50,500,400,50))
    pygame.draw.rect(man_hinh,WHITE,(55,505,390,40))
    pygame.draw.circle(man_hinh,BLACK,(250,350),120)
    pygame.draw.circle(man_hinh,WHITE,(250,350),115)
    pygame.draw.circle(man_hinh,BLACK,(250,350),5)    
    # pygame.draw.line(man_hinh,BLACK,(250,350),(250,250))

    man_hinh.blit(text_1,(50,30))
    man_hinh.blit(text_2,(50,130))
    man_hinh.blit(text_3,(150,30))
    man_hinh.blit(text_4,(150,130))
    man_hinh.blit(text_5,(250,30))
    man_hinh.blit(text_6,(250,130))
    
    mouse_x,mouse_y=pygame.mouse.get_pos()
    # print(mouse_y,mouse_x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.pause()
                    if 50<mouse_x<100 and 50<mouse_y<100:
                        tong_phut=tong_phut+60
                    if 50<mouse_x<100 and 150<mouse_y<200:
                        if tong_phut == 0:
                            tong_phut=tong_phut-0
                        if tong_phut != 0:
                            tong_phut=tong_phut-60
                    if 150<mouse_x<200 and 50<mouse_y<100:
                        tong_giay=tong_giay+1                  
                    if 150<mouse_x<200 and 150<mouse_y<200:
                        tong_giay=tong_giay-1
                    if 250<mouse_x<450 and 50<mouse_y<100:
                        run_1=True   
                    if 250<mouse_x<450 and 150<mouse_y<200:
                        tong_giay = 0
                        tong_phut = 0
    
    
    
    if run_1:
        tong_giay-=1
        time.sleep(0.03)
    
        

    tong_tat_ca=tong_phut+tong_giay                
    tong_phut_moi=int(tong_tat_ca/60)
    tong_giay_moi=tong_tat_ca-tong_phut_moi*60 
    if tong_phut_moi == 0 and tong_giay_moi == 0:
        run_1=False
        pygame.mixer.Sound.play(am)

        # pygame.mixer.Sound.play(chuong)      
    time_h=str(tong_phut_moi)
    text_7=so.render(time_h,True,BLACK)
    man_hinh.blit(text_7,(80,100))
    time_s=str(tong_giay_moi)
    text_8=so.render(time_s,True,BLACK)
    man_hinh.blit(text_8,(150,100))
    man_hinh.blit(text_9,(120,90))
    chieu_dai=tong_tat_ca*(13/40)
    if chieu_dai<=390:
        pygame.draw.rect(man_hinh,BLUE,(55,505,chieu_dai,40))
    if chieu_dai>390:
        pygame.draw.rect(man_hinh,BLUE,(55,505,390,40))


    x_giay=250 + 100*math.sin(6*tong_giay_moi*math.pi/180)
    y_giay=350 - 100*math.cos(6*tong_giay_moi*math.pi/180)
    pygame.draw.line(man_hinh,BLUE,(250,350),(x_giay,y_giay))
    x_phut=250 + 80*math.sin(6*tong_phut_moi*math.pi/180)
    y_phut=350 - 80*math.cos(6*tong_phut_moi*math.pi/180)
    pygame.draw.line(man_hinh,BLUE,(250,350),(x_phut,y_phut))

        





    pygame.display.flip()