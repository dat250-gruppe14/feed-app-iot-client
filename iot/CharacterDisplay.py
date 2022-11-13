import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

class CharacterDisplay:
	lcd_columns = 16
	lcd_rows = 2
	lcd = None

	def __init__(self, config):
		lcd_rs = digitalio.DigitalInOut(config['lcd_rs'])
		lcd_en = digitalio.DigitalInOut(config['lcd_en'])
		lcd_d7 = digitalio.DigitalInOut(config['lcd_d7'])
		lcd_d6 = digitalio.DigitalInOut(config['lcd_d6'])
		lcd_d5 = digitalio.DigitalInOut(config['lcd_d5'])
		lcd_d4 = digitalio.DigitalInOut(config['lcd_d4'])

		self.lcd = character_lcd.Character_LCD_Mono(
			lcd_rs, 
			lcd_en, 
			lcd_d4, 
			lcd_d5, 
			lcd_d6, 
			lcd_d7, 
			self.lcd_columns, 
			self.lcd_rows
		)
		self.lcd.clear()
	def send_message(self, line1=None, line2=None):
		self.lcd.clear()

		if line1 == None:
			self.lcd.message = 'DAT250\nGroup 14'
		elif line2 == None:
			self.lcd.message = line1
		else:
			self.lcd.message = line1 + '\n' + line2
		

if __name__ == '__main__':
	from sys import argv
	from board_config import board_config
	lcd = IoTDisplay(board_config)
	lcd.send_message("hello DAT250" if len(argv) == 1 else argv[1], None if len(argv) < 3 else argv[2])

