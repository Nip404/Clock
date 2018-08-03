import pygame
import math
import sys

pygame.font.init()

class Clock:    
    def __init__(self,surface,fontsize=20,radius=200,centre=[250,250]):
        # Initialisations
        self.surface = surface
        self.s = [self.surface.get_width(),self.surface.get_height()]
        self.font = pygame.font.SysFont("Garamond MS",fontsize)
        self.radius = radius
        self.centre = centre
        self.datebox = [self.centre[0],self.centre[1]+(100*(self.radius/200))]
        self.timebox = [self.centre[0],self.centre[1]-(100*(self.radius/200))]

        self.main_points = [[[self.radius*math.cos(i)+self.centre[0],self.radius*math.sin(i)+self.centre[1]],[(self.radius+20)*math.cos(i)+self.centre[0],(self.radius+20)*math.sin(i)+self.centre[1]],p+1] for p,i in enumerate([math.radians(e+270 if e+270 < 360 else e-90) for e in [360*(k/12) for k in range(1,13)]])]
        self.sub_points = [[[(self.radius+5)*math.cos(i)+self.centre[0],(self.radius+5)*math.sin(i)+self.centre[1]],[(self.radius-5)*math.cos(i)+self.centre[0],(self.radius-5)*math.sin(i)+self.centre[1]]] for i in [math.radians(e) for e in [360*(k/60) for k in range(60)]]]
        
    def update(self,datetimeObject):
        # Update local time input to global time        
        self.datetime = str(datetimeObject)

        self.date = self.font.render("%s %s %s" % ((self.datetime[8:10] if int(self.datetime[8]) else self.datetime[9])+{i+1:e for i,e in enumerate("st nd rd".split(" ")+(["th"]*27))}[int(self.datetime[8:10])],{p+1:j for p,j in enumerate("January/February/March/April/May/June/July/August/September/October/November/December".split("/"))}[int(self.datetime[5:7])],self.datetime[:4]),True,(0,0,0))
        self.time = self.font.render("%s:%s:%s" % (self.datetime[11:13],self.datetime[14:16],self.datetime[17:19]),True,(0,0,0))

    def draw(self):
        # Main points on circumference
        for pointData in self.main_points:
            pygame.draw.circle(self.surface,(0,0,0),list(map(int,pointData[0])),4,0)
            self.surface.blit(self.font.render(str(pointData[2]),True,(0,0,0)),self.font.render(str(pointData[2]),True,(0,0,0)).get_rect(center=pointData[1]))

        # Sub points on circumference
        for point in self.sub_points:
            pygame.draw.line(self.surface,(0,0,0),list(map(int,point[0])),list(map(int,point[1])),2)

        # Digital date and time
        self.surface.blit(self.date,self.date.get_rect(center=self.datebox))
        self.surface.blit(self.time,self.time.get_rect(center=self.timebox))
        
        pygame.draw.rect(self.surface,(0,0,0),[self.centre[0]-(self.date.get_width()/2)-10,self.centre[1]+(100*(self.radius/200))-(self.date.get_height()/2)-10,self.date.get_width()+20,self.date.get_height()+20],4)
        pygame.draw.rect(self.surface,(0,0,0),[self.centre[0]-(self.time.get_width()/2)-10,self.centre[1]-(100*(self.radius/200))-(self.time.get_height()/2)-10,self.time.get_width()+20,self.time.get_height()+20],4)

        # Frame
        pygame.draw.circle(self.surface,(0,0,0),self.centre,self.radius,4)

        # Red hour hand & circles
        pygame.draw.circle(self.surface,(255,0,0),self.centre,20,0)
        pygame.draw.line(self.surface,(255,0,0),self.centre,((50*(self.radius/200))*math.cos(math.radians(int(self.datetime[11:13])*15-90))+self.centre[0],(50*(self.radius/200))*math.sin(math.radians(int(self.datetime[11:13])*15-90))+self.centre[1]),6)
        pygame.draw.circle(self.surface,(255,0,0),list(map(lambda i: int(i+1.5),((50*(self.radius/200))*math.cos(math.radians(int(self.datetime[11:13])*15-90))+self.centre[0],(50*(self.radius/200))*math.sin(math.radians(int(self.datetime[11:13])*15-90))+self.centre[1]))),3,0)

        # Green minute hand & circles
        pygame.draw.circle(self.surface,(0,255,0),self.centre,15,0)
        pygame.draw.line(self.surface,(0,255,0),self.centre,((170*(self.radius/200))*math.cos(math.radians(int(self.datetime[14:16])*6-90))+self.centre[0],(170*(self.radius/200))*math.sin(math.radians(int(self.datetime[14:16])*6-90))+self.centre[1]),4)
        pygame.draw.circle(self.surface,(0,255,0),list(map(lambda i: int(i+1),((170*(self.radius/200))*math.cos(math.radians(int(self.datetime[14:16])*6-90))+self.centre[0],(170*(self.radius/200))*math.sin(math.radians(int(self.datetime[14:16])*6-90))+self.centre[1]))),2,0)

        # Blue second hand & circles
        pygame.draw.circle(self.surface,(0,0,255),self.centre,10,0)
        pygame.draw.line(self.surface,(0,0,255),self.centre,((190*(self.radius/200))*math.cos(math.radians(int(self.datetime[17:19])*6-90))+self.centre[0],(190*(self.radius/200))*math.sin(math.radians(int(self.datetime[17:19])*6-90))+self.centre[1]),2)

        # Centrepiece
        pygame.draw.circle(self.surface,(0,0,0),self.centre,5,0)

    def events(self,**additionalevents):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                # User defined event must be an existing pygame event and be followed by a function         
                for user_event in additionalevents.keys():
                    if event.type == user_event:
                        try:
                            addtionalevents[user_event]()
                        except Exception as e:
                            print("An error occurred: %s" % e)
