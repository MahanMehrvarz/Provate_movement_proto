
from utility import *

import pygame, sys, random

#text to be printed

not_yet="more participants needed"
enough="enough to start"

#-----------------------------------------------

"""intial settings for pygame"""

pygame.init()
width=1000
heigth=800
windowsize = (width, heigth)

screen = pygame.display.set_mode(windowsize)

myfont=pygame.font.SysFont("Myriad Pro", 42)

#-------------------------------------------------


myfont.render(not_yet, 1,(255,0,255),(255,255,255))

point = pygame.image.load("on.gif")
point=point.convert()
rect=point.get_rect()

#point = pygame.transform.scale(point, (50, 50))

x0, y0 = 0, 0

#hiding the mmouse cursur
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()


inbox= last_message()
print inbox
p_list= [ ]
counter=0

# programs run instantly
while True:
    print "first while"
    time.sleep(1)
    a= False
    c=False
    time.sleep(1)
    #the event loop which breaks at the end
    while inbox!= last_message():

        print "while 2"


        if a== False:

            new_inbox= last_message()
            new_inbox["name"]= p_name()

            # if the new message is from a different number
            if counter>0 and new_inbox['number']!= p_list[-1]['number']:
                p_list.append(new_inbox)
                counter+=1
                print "first if"

            # if this is the first new message
            elif counter==0:

                p_list.append(new_inbox)
                counter+=1
                print "elif"
            #if the same person is trying to mimic the new message
            else:
                txt="error"
                sending_txt(txt,p_list[-1]['number'])
                print "else"

            a=True
            inbox= last_message()
            time.sleep(0.5)
            #print p_list
            print "lengh of p_list: " + str(len(p_list))

            current=len(p_list)
        e=1

        time.sleep(1)

        # for testing purposes


        #whenever someone txt stop this the program goes to the instant while
        #the pygame render while

        while last_message()['text']!="STOP THIS":

            clock.tick(40)
            print "while pygame"
            point.set_alpha(e)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            screen.fill((0, 0, 0))

            time.sleep(1)

            #if enough participants

            if len(p_list)>1 and c==False:
                print "pygame 1f"
                log=myfont.render(enough, 1,(255,0,255),(0,0,0))
                screen.blit(log, (x0, y0))


                for i in p_list:

                    x1, y1 = random.randrange(0,width-100), random.randrange(0,heigth-100)

                    #this for only renders the circles nicer from 0% opac to 100%
                    for e in range(1,255):
                        point.set_alpha(e)
                        screen.blit(point, (x1, y1))
                        pygame.display.update()
                        time.sleep(0.001)

                # c variable help  us not to repeat the whole pygame loop if there is no change
                c=True


            # if there is not enough members

            elif current>0 and len(p_list)== current and c==False:
                print "pygame el1f"
                log=myfont.render(not_yet, 1,(255,0,255),(0,0,0))

                screen.blit(log, (x0, y0))
                pygame.display.update()
                break


            elif c==False:
                print "pygame else"
                log=myfont.render("to start; txt I can\'t breath \
                followed by your name", 1,(255,0,255),(0,0,0))

                screen.blit(log, (x0, y0))
                pygame.display.update()
                break

            time.sleep(1)
            break



            #pygame.display.update()

