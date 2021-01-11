import pygame
import pynput
from pynput.mouse import Button, Controller
import time

mouse = Controller()
keyboard = pynput.keyboard.Controller()

def map(val, min1, max1, min2, max2):
    range1 = max1 - min1
    range2 = max2 - min2
    
    scale = range2 / range1
    return (val - min1) * scale + min2

def main(): 
    xmovement = 0
    ymovement = 0
    sideMovement = 0
    gas = False
    brake = False

    joysticks = []

    # for all the connected joysticks
    for i in range(0, pygame.joystick.get_count()):
        # create an Joystick object in our list
        joysticks.append(pygame.joystick.Joystick(i))
        # initialize them all (-1 means loop forever)
        joysticks[-1].init()
        # prints controller name
        print( "Detected joystick ",joysticks[-1].get_name(),"")

    while True:
        for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    print( "Joystick ",joysticks[event.joy].get_name()," axis",event.axis,"motion.", event.value)
                    if event.axis == 0:
                        # xmovement = map(event.value, -1, 1, -1680, -1)
                        xmovement = map(event.value, -1, 1, -100, 100)
                        
                    if event.axis == 1:
                        if (event.value > 0.02):    # brake pedal pressed
                            brake = True
                            gas = False
                        elif (event.value < -0.02): # gas pedal pressed
                            gas = True
                            brake = False
                        else:
                            brake = False
                            gas = False
                        
                elif event.type == pygame.JOYBUTTONDOWN:
                    print( "Joystick ",joysticks[event.joy]," button",event.button,"down.")
                    if event.button == 0:
                        mouse.press(Button.left)
                        # background.fill((255, 0, 0))
                    elif event.button == 1:
                        mouse.press(Button.right)
                        # background.fill((0, 0, 255))

                    elif event.button == 4:
                        keyboard.press("e")
                    elif event.button == 5:
                        keyboard.press("f")
                    elif event.button == 6:
                        return      # Terminate script
                    elif event.button == 7:
                        keyboard.press("x")

                elif event.type == pygame.JOYBUTTONUP:
                    print( "Joystick ",joysticks[event.joy].get_name()," button",event.button,"up.")
                    if event.button == 0:
                        mouse.release(Button.left)
                    elif event.button == 1:
                        mouse.release(Button.right)
                elif event.type == pygame.JOYHATMOTION:
                    print( "Joystick ",joysticks[event.joy].get_name()," hat switch at ",event.value," position ")
                    
                    if event.value == (0,1):    # upward hat switch placement
                        ymovement = -5
                    elif event.value == (0,-1): # downward hat switch placement
                        ymovement = 5
                    elif event.value == (0,0):  # middle hat switch placement
                        ymovement = 0
                        sideMovement = 0
                    if event.value == (1,0):    # right hat switch placement
                        sideMovement = 1
                    elif event.value == (-1,0): # left hat switch placement
                        sideMovement = -1
        
        #   WASD movements ↓
        if gas:
            keyboard.press("w")
        else:
            keyboard.release("w")
        
        if brake:
            keyboard.press("s")
        else:
            keyboard.release("s")
        
        if sideMovement == 1:
            keyboard.press("d")
            keyboard.release("a")
        elif sideMovement == -1:
            keyboard.press("a")
            keyboard.release("d")
        else:
            keyboard.release("a")
            keyboard.release("d")
        
        mouse.move(xmovement, ymovement)    # Mouse movement

        time.sleep(0.02)                    # time delay prevents unregistered or delayed actions in apps

pygame.init()
main()
pygame.quit()
