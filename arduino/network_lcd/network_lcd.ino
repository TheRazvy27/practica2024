#include <ESP8266WebServer.h>
#include <LiquidCrystal_I2C.h>
#include <Pinger.h>

Pinger pinger;
const char* ssid = "Telecom Academy";
const char* password = "telacad2024";
LiquidCrystal_I2C lcd(0x27, 16, 2);

void connectToWiFi()
{ 
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Conectare");
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  lcd.setCursor(0, 1);
  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    lcd.print(".");
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Retea:");
  lcd.print(ssid);
}

void setup() 
{
  lcd.init();
  lcd.backlight();
  Serial.begin(115200);
  delay(1000);
  connectToWiFi();
  lcd.setCursor(0, 1);
  lcd.print("Internet:");
  if(pinger.Ping("google.com") == false)
  {
    lcd.print(" X");
  }
  else lcd.print(" OK");
  delay(10000);
}

void loop() 
{
 delay (10000);
 if(pinger.Ping("google.com") == false)
 {
  lcd.setCursor(0, 1);
  lcd.print("Internet: X ");
 }
 else {
  lcd.setCursor(0, 1);
  lcd.print("Internet: OK");
 }
 if (WiFi.status() != WL_CONNECTED);{
  lcd.print("Deconectat.");
 }
}
