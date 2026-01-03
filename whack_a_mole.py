from machine import Pin
from time import sleep, ticks_diff, ticks_ms
from random import randint

red = Pin(10, Pin.OUT, value=0)
yellow = Pin(11, Pin.OUT, value=0)
green = Pin(12, Pin.OUT, value=0)

button_gr = Pin(13, Pin.IN, Pin.PULL_UP)
button_yl = Pin(14, Pin.IN, Pin.PULL_UP)
button_rd = Pin(15, Pin.IN, Pin.PULL_UP)

leds = [green, yellow, red]
buttons = [button_gr, button_yl, button_rd]

score = 0
roundtime = 2000
rounds_played = 0

while True:
    sleep(0.5)
    
    led_index = randint(0,2)
    leds[led_index].value(1)
    
    start_time = ticks_ms()
    hit = False
    
    while ticks_diff(ticks_ms(), start_time) < roundtime:
        if buttons[led_index].value() == 0:
            print(f"HIT! {score}")
            score += 1
            hit = True
            break
        for i in range(3):
            if i != led_index:  # Skip the correct button
                if buttons[i].value() == 0:
                    print(f"WRONG BUTTON! No points.")
                    hit = True  # Mark as "handled" so we don't count it as timeout
                    break  # Exit the for loop
    
        if hit:  # If wrong button was pressed, exit the while loop too
            break
        sleep(0.01)
    
    leds[led_index].value(0)
    
    if not hit:
        print(f"miss, score is still: {score}")
    
    rounds_played += 1
    if rounds_played >= 50:
        break
    if rounds_played % 5 == 0:
        roundtime = max(500, roundtime - 200)
        print(f"lvl up! it goes faster: {roundtime}")
        
for led in leds:
    led.toggle()
print(f"Well done! Here is your score: {score}")




   