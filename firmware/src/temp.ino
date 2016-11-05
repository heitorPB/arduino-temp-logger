#include <Arduino.h>
#include <Wire.h>
// temp includes
#include <inttypes.h>
#include <math.h>


const unsigned int ledPin = 13;


void setup()
{
	Serial.begin(115200);
	while (!Serial);
	pinMode(ledPin, OUTPUT);
}


void loop()
{
	static uint8_t bla = 0;

	// wait serial command
	if (Serial.available()) {
		char command = Serial.read();
		switch (command) {
		case 'E':
		case 'e':
			// send 1 2 3 to confirm this is the firmware
			Serial.write('1');
			Serial.write('2');
			Serial.write('3');
			break;

		case 'T':
		case 't':
			// temperature
			Serial.write((uint8_t) 13);
			Serial.write((uint8_t) bla++);
			Serial.write((uint8_t) 200);
			break;

		case 'H':
		case 'h':
			Serial.write((uint8_t) 42);
			Serial.write((uint8_t) bla++);
			Serial.write((uint8_t) 220);
			break;
		default:
			Serial.print("Command ");
			Serial.print(command);
			Serial.print(" not recognized.");
		}
	}
}
