#include <Arduino.h>
#include <Wire.h>
#include <stdlib.h>
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
	static double bla = -13.74;	// double is the same as a float in avr
	char result[7] = "87.940";

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
			// fake temperature for now
			dtostrf(bla, 4, 2, result);
			Serial.write('t');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('T');
			break;

		case 'H':
		case 'h':
			dtostrf(bla / 2, 4, 2, result);
			Serial.write('h');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('H');
			break;

		default:
			Serial.print("Command ");
			Serial.print(command);
			Serial.println(" not recognized.");
		}

		bla += 0.666;
	}
}
