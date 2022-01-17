int tempPin = 0;

void setup() {
  // Data Transfer Rate set at 9600Kbps
  Serial.begin(9600);
}

void loop() {
  // read analog volt from sensor and save to variable temp
  float temp = analogRead(tempPin);

  // convert the analog volt to its temperature equivalent
  float tempC = temp * 0.48828125;
  float tempF = tempC * 1.8000 + 32;
  float tempK = tempC + 273.15;

  Serial.print("TEMPERATURE :");
  Serial.println();

  Serial.print(tempC);
  Serial.print("*C");
  Serial.println();

  Serial.print(tempF);
  Serial.print("*F");
  Serial.println();

  Serial.print(tempK);
  Serial.print("*K");
  Serial.println();
  Serial.println();
  
  // Update the Sensor Reading Every 1 Second
  delay(1000);
}