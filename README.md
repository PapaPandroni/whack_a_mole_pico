# Whack-a-Mole Game for Raspberry Pi Pico 2W

A fun reaction-time game built with a Raspberry Pi Pico 2W, three LEDs, and three buttons.

## How It Works

The game randomly lights up one of three LEDs (red, yellow, or green). Your goal is to press the matching button before time runs out!

- **Hit the correct button**: Earn a point and move to the next round
- **Hit the wrong button**: No points, move to next round
- **Time runs out**: Miss! No points, move to next round

The game gets progressively harder - every 5 rounds, the time window decreases by 200ms. The game ends after 50 rounds, and all LEDs blink to show your final score.

## Hardware Requirements

- Raspberry Pi Pico 2W
- 3x LEDs (Red, Yellow, Green)
- 3x 220Ω resistors
- 3x Push buttons
- Breadboard and jumper wires

### Wiring Diagram

**LEDs (with 220Ω resistors in series):**
- GP10 → 220Ω → Red LED → GND
- GP11 → 220Ω → Yellow LED → GND
- GP12 → 220Ω → Green LED → GND

**Buttons (no external resistors needed):**
- GP13 → Green Button → GND
- GP14 → Yellow Button → GND
- GP15 → Red Button → GND

The buttons use the Pico's internal pull-up resistors, so they only need to connect between the GPIO pin and ground.

## Running the Game

1. Wire up your components according to the schematic
2. Copy the code to your Pico 2W (save as `main.py` or run in Thonny)
3. Reset the Pico or run the script
4. Watch for LEDs to light up and press the matching button as fast as you can!
5. Check the console/serial output to see your score after each round

## Tuning the Game

You can adjust these variables at the top of the code to customize difficulty:

### `roundtime = 2000`
The starting time window in milliseconds for each round.
- **Default**: 2000ms (2 seconds)
- **Easy mode**: Try 3000 or higher
- **Hard mode**: Try 1500 or 1000

### `roundtime = max(500, roundtime - 200)`
How much time decreases every 5 rounds, and the minimum time allowed.
- Change `200` to make difficulty ramp faster/slower
- Change `500` to set a different minimum time window

### `if rounds_played >= 50:`
Total number of rounds before the game ends.
- **Default**: 50 rounds
- **Quick game**: Try 20 or 30
- **Marathon**: Try 100

### `if rounds_played % 5 == 0:`
How often the difficulty increases.
- **Default**: Every 5 rounds
- **Gradual**: Try 10 for slower difficulty increase
- **Intense**: Try 3 for faster difficulty increase

### `sleep(0.5)`
Pause between rounds in seconds.
- **Default**: 0.5 seconds
- **Fast-paced**: Try 0.2
- **Relaxed**: Try 1.0

## Example Score Output

```
Whack-a-Mole Started!
HIT! 1
HIT! 2
WRONG BUTTON! No points.
miss, score is still: 2
HIT! 3
lvl up! it goes faster: 1800
...
Well done! Here is your score: 42
```

## Troubleshooting

**LEDs don't light up**: Check your resistor connections and make sure LEDs are oriented correctly (long leg to resistor, short leg to ground).

**Buttons don't respond**: Verify your buttons are wired from GPIO to GND, and that you're using `Pin.PULL_UP` in the code.

**Wrong LED/button pairing**: Double-check your GPIO pin numbers match your physical wiring.

---

*Written by AI, edited by Author*