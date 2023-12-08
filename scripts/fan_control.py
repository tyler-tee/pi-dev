import RPi.GPIO as GPIO
import time

# Set the GPIO pin (using BCM numbering) to which the fan is connected
FAN_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

# Temperature threshold in degrees Celsius
TEMP_THRESHOLD = 50

def get_cpu_temperature():
    """Reads the CPU temperature."""
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temperature = float(file.read()) / 1000.0
    return temperature

def main():
    try:
        while True:
            cpu_temp = get_cpu_temperature()
            if cpu_temp > TEMP_THRESHOLD:
                GPIO.output(FAN_PIN, True)  # Turn on the fan
            else:
                GPIO.output(FAN_PIN, False)  # Turn off the fan
            time.sleep(60)  # Wait 60 seconds before checking again
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # Clean up GPIOs when exiting
        
if __name__ == "__main__":
    main()
