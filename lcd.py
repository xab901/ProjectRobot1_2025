import lcd
import time

lcd.init()

lcd.clear(lcd.BLUE)
lcd.rotation(0)
lcd.draw_string(30, 30, "1, 2, 3", lcd.WHITE, lcd.BLUE)
time.sleep(1)