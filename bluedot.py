from bluedot import BlueDot
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED setup
LED_PIN = 10
GPIO.setup(LED_PIN, GPIO.OUT)

# DHT11 setup
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO4

# BlueDot setup
bd = BlueDot()

def on_press(pos):
    if pos.x > 0.5:  # Right side pressed
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print(f"[DHT11] Temperature: {temperature:.1f}°C, Humidity: {humidity:.1f}%")
        else:
            print("[DHT11] Failed to read from sensor.")
    elif pos.y > 0.5:  # Top side pressed
        GPIO.output(LED_PIN, True)
        print("[LED] ON")
    elif pos.y < -0.5:  # Bottom side pressed
        GPIO.output(LED_PIN, False)
        print("[LED] OFF")

bd.when_pressed = on_press

# Keep script running
print("Bluetooth interface ready. Use Blue Dot to send commands.")
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program exited.")

