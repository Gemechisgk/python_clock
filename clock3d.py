#! /usr/bin/env python

#File:
#clock3d.py

#dependencies:
#pyopengl
#pyggel
#pygame

#Note:
#A simple analog clock in pygame, using the pyggel pyopengl library
#An example of integrating simple meshes into a group model
#Tap up,down,left,right arrow keys to rotate the clock around its axis

#Tips:
#Use low polygon models for games to keep frame rates high
#To set the pivot point of a mesh, move it to 0,0,0 before saving 

#Author:
#Jestermon.weebly.com
#jestermonster@gmail.com

import sys, datetime, string
import pyggel
from pyggel import *


#============================== class tictac3d
class clock3d:

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):

        #setup useful colour values
        self.setupcolor()

        #initialize pygel screen
        pyggel.init(screen_size=(640,480))

        #create pygel scene
        self.scene = pyggel.scene.Scene()

        #Set window title
        pyggel.view.set_title("Clock3D")

        #create a pygel light
        self.light = pyggel.light.Light((0,100,0),#so this is aobve most the elements
                          (0.5,0.5,0.5,1),#ambient color
                          (1,1,1,1),#diffuse color
                          (50,50,50,10),#specular
                          (0,0,0),#spot position - not used
                          True) #directional, not a spot light
        self.scene.add_light(self.light)

        #Create a pygel camera... Set camera distance based on model size
        #We could also move the model futher away, but we want to place
        #the model at 0,0,0 So we move the camera back a bit.
        self.camera = pyggel.camera.LookAtCamera((0,1,0),distance=40)

        #setup pygel event handler
        self.event_handler = pyggel.event.Handler()

        #setup game objects
        self.loadmodels()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setupcolor(self):
        #colour tupples based on RGB 255 values
        self.red = (255,0,0)
        self.blue = (0,0,255)
        self.green = (0,255,0)
        self.yellow = (255,255,0)
        self.magenta = (255,0,255)
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.orange = (198,138,22)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def event_handler(self):
        pass

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def loadmodels(self):

        #Load modelparts
        self.clockface = pyggel.mesh.OBJ("face.obj",
                                         pos=(0,0,0), swapyz=False,
                                         colorize=(self.rgba(self.red,1)))
        self.clockborder = pyggel.mesh.OBJ("border.obj",
                                         pos=(0,0,0), swapyz=False,
                                         colorize=(self.rgba(self.yellow,1)))
        self.clockmarks = pyggel.mesh.OBJ("marks.obj",
                                         pos=(0,0,0), swapyz=False,
                                         colorize=(self.rgba(self.white,1)))
        self.secondhand = pyggel.mesh.OBJ("secondhand.obj",
                                         pos=(0,0,0), swapyz=False,
                                         colorize=(self.rgba(self.magenta,1)))
        self.hourhand = pyggel.mesh.OBJ("hourhand.obj",
                                         pos=(0,0,0), swapyz=False,
                                         colorize=(self.rgba(self.blue,1)))
        self.minutehand = pyggel.mesh.OBJ("minutehand.obj",
                                         pos=(0,0,0), swapyz=False,
                                         colorize=(self.rgba(self.green,1)))

        #add models to the scene
        self.scene.add_3d(self.clockface)
        self.scene.add_3d(self.clockborder)
        self.scene.add_3d(self.clockmarks)
        self.scene.add_3d(self.secondhand)
        self.scene.add_3d(self.hourhand)
        self.scene.add_3d(self.minutehand)

        #create model group ~ Use groups to tie model parts together
        self.clock = {}
        self.clock['face'] = self.clockface
        self.clock['border'] = self.clockborder
        self.clock['marks'] = self.clockmarks
        self.clock['secondhand'] = self.secondhand
        self.clock['hourhand'] = self.hourhand
        self.clock['minutehand'] = self.minutehand
        self.clockrotation = (0,0,0)
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def rgba(self,colors,alpha):

        #Returns 0-1 colour / alpha tupple, based on RGB values
        r,g,b = colors
        return (r/255,g/255,b/255,alpha)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update(self):

        #Get current time
        today = str(datetime.datetime.today())
        hours = today[11:13]
        minutes = today[14:16]
        seconds = today[17:19]

        #First fotate the entire clock based on key pressed
        #Use group rotate and position before managing the individual parts
        self.rotate_clock()

        #Finally update the clock hands
        self.update_seconds(seconds)
        self.update_minutes(minutes)
        self.update_hours(hours,minutes)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def rotate_clock(self):
        #Iterate through the group dictionary and update all the models
        #in the group
        for part in self.clock:
            self.clock[part].rotation = self.clockrotation

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update_seconds(self,seconds):

        #60 seconds in and minute, convert ratio to angles
        rot = float(seconds)/60.0 * 360.0
        #Rotate the second hand model (rotate anti-clockwise (-))
        x,y,z = self.clockrotation
        self.secondhand.rotation = (x,y,-rot)
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update_minutes(self,minutes):

        #60 minutes in an hour, convert ration to angles
        rot = float(minutes)/60.0 * 360.0

        #Rotate the minute hand model (rotate anti-clockwise (-))
        x,y,z = self.clockrotation
        self.minutehand.rotation = (x,y,-rot)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def update_hours(self,hours,minutes):

        #24 hours in an day, convert ration to angles
        hour = float(hours)
        if hour > 12:
            hour = hour % 12
        baserot = float(hour)/12.0 * 360.0

        #base rotation will place the hour hand exactly, but we want it to
        #advance a little, based on the number of minutes passed
        minute = float(minutes)

        #360 degerees / 12 hour hands / 60 second marks * minutes 
        offset = 360.0 / 12.0 / 60.0 * minute 
        x,y,z = self.clockrotation
        self.hourhand.rotation = (x,y,-(baserot+offset))
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def clock_left(self):
        x,y,z = self.clockrotation
        y -= 5
        self.clockrotation =(x,y,z)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def clock_right(self):
        x,y,z = self.clockrotation
        y += 5
        self.clockrotation =(x,y,z)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def clock_up(self):
        x,y,z = self.clockrotation
        x -= 5
        self.clockrotation =(x,y,z)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def clock_down(self):
        x,y,z = self.clockrotation
        x += 5
        self.clockrotation =(x,y,z)
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def run(self):

        #setup work variables
        fps = 60
        dt = 1.0/fps
        clock = pygame.time.Clock()

        while 1:
            
            #get events!
            self.event_handler.update() 

            if self.event_handler.quit or K_ESCAPE in self.event_handler.keyboard.hit: 
                pyggel.quit()
                sys.exit(0)

            #handle up.down,left, right keys to rotate clock
            for k in self.event_handler.keyboard.hit:
                if k == K_UP:
                    self.clock_up()
                if k == K_DOWN:
                    self.clock_down()
                if k == K_LEFT:
                    self.clock_left()
                if k == K_RIGHT:
                    self.clock_right()

            #clear screen for new drawing...
            pyggel.view.clear_screen()

            #Update the models
            self.update()

            #render the scene... NOTE to pass the camera parameter
            self.scene.render(self.camera) 
            
            #flip the display buffer
            pyggel.view.refresh_screen()

            #limit FPS
            clock.tick(fps)


#============================== main
if __name__ == '__main__':

    game = clock3d()
    game.run()











