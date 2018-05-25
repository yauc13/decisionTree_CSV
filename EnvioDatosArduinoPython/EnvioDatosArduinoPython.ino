
/*
Este Sketch captura la lectura desde el puerto serie,
enviado desde python.
si el valor que se recibe es L, entonces desde Arduino
se envia por puerto serie la lectura del sensor DHT22,
para que desde python sea leido.

ademas los valores del sensor se pueden
ver en una LCD
 pinLCD   Arduino Mega
  RS    = 24;
  E      = 25;
  11-D4 = 26;
  12-D5 = 27;
  13-D6 = 28;
  14-D7 = 29
  D0-D1-D2-D3 = GND
  

*/
#include <LiquidCrystal.h>
#include <DHT.h>
#include <Adafruit_Sensor.h>

int SENSOR = 2; // puerto sensor DHT22


// puertos para LCD
  int RS = 24;
  int E = 25;
  int D4 = 26;
  int D5 = 27;
  int D6 = 28;
  int D7 = 29;
  
DHT dht (SENSOR, DHT22);
LiquidCrystal lcd (RS, E, D4, D5 , D6, D7);

void setup () {
  dht.begin();
  Serial.begin(9600);
  lcd.begin(16, 2); 
     lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Bienvenido");
    delay(500); 
}

void loop () {
      int humedad = dht.readHumidity();
      int temp = dht.readTemperature();
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("T:");
      lcd.print(temp);
      lcd.print("C");
      lcd.setCursor(0, 1);
      lcd.print("HR: ");
      lcd.print(humedad);
      lcd.print("%");  
  
      if(Serial.available()) {      
        char c = Serial.read();
        if (c=='L') {
          Serial.print(humedad);
          Serial.print(',');
          Serial.println(temp);              
            } 
      }       
   delay(500);       
}
