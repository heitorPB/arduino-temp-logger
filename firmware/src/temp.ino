#include <Arduino.h>
#include <Wire.h>
#include <stdlib.h>
// temp includes
#include <math.h>
// DHT lib from Adafruit
#include <DHT.h>


const unsigned int ledPin = 13;
const unsigned int dhtPin = 2;


DHT dht(dhtPin, DHT22);

void setup()
{
	dht.begin();
	Serial.begin(115200);
	while (!Serial);
	pinMode(ledPin, OUTPUT);
}

void loop()
{
	static double bla = -50;	// double is the same as a float in avr
	char result[8] = "-87.940";

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
			bla = dht.readTemperature();
			if (isnan(bla))
				bla = -50;
			dtostrf(bla, 4, 3, result);
			Serial.write('t');
			Serial.print(strlen(result));
			Serial.print(result);
			Serial.write('T');
			break;

		case 'H':
		case 'h':
			bla = dht.readHumidity();
			if (isnan(bla))
				bla = -50;
			dtostrf(bla, 4, 3, result);
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
	}
}
