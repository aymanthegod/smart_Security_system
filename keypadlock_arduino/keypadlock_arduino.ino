#include <Keypad.h>

// Bluetooth Variables
char incomingChar;

#define RED_LED 8
#define GREEN_LED 9
#define TRIGGER_PIN 7

// Keypad Configuration
const byte ROWS = 4;
const byte COLS = 4;

char keys[ROWS][COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

byte rowPins[ROWS] = {2, 3, 4, 5};
byte colPins[COLS] = {6, 10, 11, 12};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String password = "A2B3";    // Example password
String inputPassword = "";   // User input
bool acceptingInput = true;  // Flag to control input

void setup() {
  Serial.begin(9600);

  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(TRIGGER_PIN, OUTPUT);

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(TRIGGER_PIN, LOW);
}

void loop() {
  // Bluetooth Section
  if (Serial.available()) {
    incomingChar = Serial.read();

    if (incomingChar == 'c') {
      digitalWrite(RED_LED, HIGH);
      digitalWrite(GREEN_LED, LOW);
    }
    else if (incomingChar == 'o') {
      digitalWrite(GREEN_LED, HIGH);
      digitalWrite(RED_LED, LOW);
    }
  }

  // Keypad Section (Strict 4-key input)
  if (acceptingInput) {
    char key = keypad.getKey();

    if (key) {
      Serial.print("Keypad Pressed: ");
      Serial.println(key);

      inputPassword += key;

      if (inputPassword.length() == 4) { // Only accept 4 keys per attempt
        acceptingInput = false;  // Lock input while checking
        checkPassword();         // Check entered password
        inputPassword = "";      // Always reset after checking
        acceptingInput = true;   // Allow new input
      }
    }
  }
}

void checkPassword() {
  if (inputPassword == password) {
    Serial.println("✅ Password Correct");

    digitalWrite(GREEN_LED, HIGH);
    delay(5000);
    digitalWrite(GREEN_LED, LOW);
  } else {
    Serial.println("❌ Password Incorrect");

    digitalWrite(RED_LED, HIGH);
    delay(5000);
    digitalWrite(RED_LED, LOW);

    digitalWrite(TRIGGER_PIN, HIGH);
    delay(500);
    digitalWrite(TRIGGER_PIN, LOW);
  }
}