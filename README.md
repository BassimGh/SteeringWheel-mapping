#### This script maps steering wheel and pedal controls to mouse and keyboard controls.

### Why?

* To play pc games that don't support steering wheel and footpedal control
* cuz y not

### How?

*Mouse movement*
1. [Pygame](https://www.pygame.org/wiki/about) captures steering wheel movement
2. This function takes the steering output that ranges from -1 to 1 and maps it to a desired mouse movement value based on a specified range (range depends on sensitivity preference)

```

```

3. [Pynput](https://pynput.readthedocs.io/en/latest/mouse.html) Moves mouse by value received from map function

*Mouse clicking*
1. [Pygame](https://www.pygame.org/wiki/about) captures steering wheel gear shifts
2. [Pynput](https://pynput.readthedocs.io/en/latest/mouse.html) simulates left and right mouse button cicks

*Keyboard control*
1. [Pygame](https://www.pygame.org/wiki/about) captures steering button presses and foot pedal movement
2. [Pynput](https://pynput.readthedocs.io/en/latest/keyboard.html) simulates keyboard key presses for steering wheel and foot pedal controls
*pressing gas pedal would press the 'w' key and the brake pedal would press the 's' key to move forward and backward for WASD game movement.*

**Mapped controls:**

| Steering/footpedal input | Mouse/keyboard output |
| ------------- |:-------------:|
| gearshift up  | left click | 
| col 2 is      | right click |
| right turn | right mouse-x movement |
| left turn | left mouse-x movement |
| upward hat switch placement | upward mouse-y movement |
| downward hat switch placement | downward mouse-y movement |
| gas pedal | 'w' key |
| break pedal | 's' key |
| break pedal | 's' key |

---------------------

## Demo

![4tg1db](https://user-images.githubusercontent.com/67180268/104240667-70a2a900-542a-11eb-9d24-c645abeec538.gif)

![4tg0c6](https://user-images.githubusercontent.com/67180268/104239950-4a303e00-5429-11eb-8af2-0fa71270f8c6.gif)
