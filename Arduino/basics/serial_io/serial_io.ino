#define LED_PIN 10
#define SWITCH_BYTE '1'

boolean state = false;

int loop_index = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  char c;
  while (Serial.available() == 0);
  c = Serial.read();
  if (c == SWITCH_BYTE) { 
    state = !state;
    digitalWrite(LED_PIN, state);
  }
}
