from threading import Thread
from hal import hal_adc as hal_adc
from hal import hal_servo as hal_servo

def adc_servo(num):
    raw_number = num
    print (raw_number)
    final_value = (180 / 1023 * raw_number)
    final_value = final_value / 180 * 100
    hal_servo.set_servo_position(final_value)

def main():
    hal_servo.init()
    hal_servo.set_servo_position(50)
    
    
    hal_adc.init(adc_servo)
    hal_adc_thread = Thread(target=hal_adc.get_adc_value(1))
    hal_adc_thread.start()

if __name__ == "__main__":
    main()