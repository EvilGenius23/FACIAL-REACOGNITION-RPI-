import lcddriver
from time import *
 
lcd = lcddriver.lcd()
lcd.lcd_clear()
 
lcd.lcd_display_string("Evil_Genius", 1)
lcd.lcd_display_string("      working ", 2)
lcd.lcd_display_string("", 3)
lcd.lcd_display_string("NMCOE", 4)