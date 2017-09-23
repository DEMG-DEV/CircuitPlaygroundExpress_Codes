#include <Adafruit_CircuitPlayground.h>
#include <Adafruit_Circuit_Playground.h>

uint8_t pixeln = 0;

void setup() {
  // put your setup code here, to run once:
  CircuitPlayground.begin();
}

void loop() {
  while(true){    
    Serial.print("Temperatura:");
    Serial.print(CircuitPlayground.temperature());
    Serial.print(" *C");
    Serial.println();
    CircuitPlayground.playTone(500 + pixeln * 500, 250);
    delay(1000);
      CircuitPlayground.setPixelColor(pixeln++, CircuitPlayground.colorWheel(25 * pixeln));
      if (pixeln == 11) {
        pixeln = 0;
      CircuitPlayground.clearPixels();
      }
  }
}
