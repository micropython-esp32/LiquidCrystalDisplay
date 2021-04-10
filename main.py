"""
Name: Liquic Crystal Project
Purpose: To turn On and Off the LED in a loop 

Requirements: Micropython, ESP32 board, JHD162A (16x2) LCD Module

Usage:
Method 1:
    a. Copy main.py, LCD.py, commands.py to PC
    b. Copy all the below lines except import statements to end of LCD.py and save
    c. similar copy the constant defintion from commands to LCD.py
    c. run LCD.py
    
Method 2:
    To run the project, Copy main.py, LCD.py, commands.py to ESP32 to device
    This method is not suitable when you are developing the script
    
For more projects, visit www.micropythonforu.com

"""
from time import sleep_ms
from time import sleep_us
from LiquidCrystalDisplay import LCD
from commands import *

lcd_disp = LCD(12, 14, 27, 26, 25, 33, 32, 5, 18, 19, 21)
lcd_disp.set_config(8, LCD_5x8DOTS, 2)

print("Program Started ... ")
lcd_disp.lcd_init()
lcd_disp.clear()
lcd_disp.home()
lcd_disp.show_text("MicroPython for U")

print("Starting loop, use Ctrl-C to break out.")
while True:
    try:
        lcd_disp.scrollDisplayLeft()
        sleep_ms(200)
        
    except KeyboardInterrupt: # Ctrl-C to come out of loop
        print("User Interruption, exiting loop")   
        break
lcd_disp.clear()
lcd_disp.home()