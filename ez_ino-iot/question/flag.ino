// lcd1602:SCL is uno:A5, lcd1602:SDA is uno:A4, lcd1602:VCC is num:V5, lcd1602:GND is uno:GND. 

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

int flag[20] = {118, 121, 995, 116, 102, 123, 104, 101, 492, 108, 482, 95, 65, 114, 100, 117, 493, 110, 482, 125};
int line[20] = {10, 3, 14, 4, 0, 13, 10, 3, 14, 0, 14, 0, 0, 7, 13, 5, 14, 0, 14, 7};
int i = 0;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Hello VYctf!");
}

void loop() {
  delay(1000);
  lcd.clear();
  lcd.print("flag is:");
  lcd.setCursor(line[i], 1);
  lcd.print(flag[i]);
  i++;
}