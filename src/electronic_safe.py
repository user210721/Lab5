from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
from hal import hal_buzzer as buzzer

class ElectronicSafe:
    def __init__(self, correct_pin):
        self.correct_pin = correct_pin
        self.entered_pin = ""
        self.attempts = 0
        self.lcd = LCD.lcd()
        self.buzzer = buzzer.init()

    def display_message(self, line1, line2=""):
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(line1, 1)
        self.lcd.lcd_display_string(line2, 2)

    def enter_pin(self, key):
        # Requirement REQ-02
        self.entered_pin += "*"
        self.display_message("Safe Lock", "Enter PIN: " + self.entered_pin)

    def unlock_safe(self):
        # Requirement REQ-03
        self.display_message("Safe Unlocked")

    def wrong_pin(self):
        # Requirement REQ-04
        self.display_message("Wrong PIN")
        self.buzzer.activate_buzzer(1)  # Activate buzzer for 1 second

    def disable_safe(self):
        # Requirement REQ-05
        self.display_message("Safe Disabled")

    def check_pin(self):
        if self.entered_pin == self.correct_pin:
            self.unlock_safe()
        else:
            self.attempts += 1
            if self.attempts == 3:
                self.disable_safe()
            else:
                self.wrong_pin()

    def run(self):
        self.display_message("Safe Lock", "Enter PIN: ")
        keypad.init(self.enter_pin, self.check_pin)

if __name__ == "__main__":
    # Set the correct PIN
    correct_pin = "1234"  # Change this to your desired PIN

    # Create an instance of the ElectronicSafe class
    electronic_safe = ElectronicSafe(correct_pin)

    # Run the Electronic Safe application
    electronic_safe.run()