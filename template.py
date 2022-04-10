#! /usr/bin/env python

#dependencies:
#pyopengl
#pyggel
#pygame


import sys
import pyggel
from pyggel import *


#============================== class tictac3d
class template:

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self):

        #initialize pygel screen
        pyggel.init(screen_size=(640,480))

        #create pygel scene
        self.scene = pyggel.scene.Scene()

        #Set window title
        pyggel.view.set_title("Jestermon's TicTac3D")

        #create a pygel light
        self.light = pyggel.light.Light((0,100,0),#so this is aobve most the elements
                          (0.5,0.5,0.5,1),#ambient color
                          (1,1,1,1),#diffuse color
                          (50,50,50,10),#specular
                          (0,0,0),#spot position - not used
                          True) #directional, not a spot light
        self.scene.add_light(self.light)

        #create a pygel camera
        self.camera = pyggel.camera.LookAtCamera((0,1,0),distance=5)

        #setup pygel event handler
        self.event_handler = pyggel.event.Handler()

        #setup game objects
        self.setup()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def event_handler(self):
        pass


    #~~~~~~~~~~~~~~~~~~~~~~~~~~
    def setup(self):

        #setup pygel objects.. 
        tex1 = pyggel.data.Texture("wood.png")

        #place spheres anywhere, pyode calculates final positons
        s1 = pyggel.geometry.Sphere(0.2, pos=(0, 0, 0), texture=tex1)
        s2 = pyggel.geometry.Sphere(0.2, pos=(0, 0, 0), texture=tex1)

        #add objects to pygel scene
        self.scene.add_3d((s1,s2))
        


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

            #clear screen for new drawing...
            pyggel.view.clear_screen()

            #render the scene... NOTE to pass the camera parameter
            self.scene.render(self.camera) 
            
            #flip the display buffer
            pyggel.view.refresh_screen()

            #limit FPS
            clock.tick(fps)


#============================== main
if __name__ == '__main__':

    game = template()
    game.run()











