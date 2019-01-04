/*
@author: mabuelanin
*/

#include <SPI.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <Servo.h>


byte G1 = 14;
byte G2 = 15;

byte motor1pin = 2;
byte motor2pin = 3;
byte motor3pin = 4;
byte motor4pin = 5;
byte motor5pin = 6;
byte motor6pin = 7;
byte motor7pin = 8;
byte motor8pin = 9;

Servo m1;
Servo m2;
Servo m3;
Servo m4;
Servo m5;
Servo m6;
Servo m7;
Servo m8;

// Forward 1500 > 1800
// Reverse 1500 > 1100


int OFF = 1500;

// int rate = 20;


byte mac[] = {  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 178);
unsigned int localPort = 8888;      // local port to listen on

EthernetUDP Udp;

char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //buffer to hold incoming packet,

void setup() {

  Ethernet.begin(mac, ip);
  Udp.begin(localPort);
  Serial.begin(9600);

  m1.attach(motor1pin);
  m2.attach(motor2pin);
  m3.attach(motor3pin);
  m4.attach(motor4pin);
  m5.attach(motor5pin);
  m6.attach(motor6pin);
  m7.attach(motor7pin);
  m8.attach(motor8pin);


  pinMode(G1, OUTPUT);
  pinMode(G2, OUTPUT);


  m1.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m2.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m3.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m4.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m5.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m6.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m7.writeMicroseconds(OFF); // send "stop" signal to ESC.
  m8.writeMicroseconds(OFF); // send "stop" signal to ESC.


  delay(3500); // delay to allow the ESC to recognize the stopped signal



}

void loop() {

  int packetSize = Udp.parsePacket();

  if (packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    Serial.println(packetBuffer);

  }


  // DOWN
  if ( packetBuffer[0] == 'a' && packetBuffer[1] == 'u') {

    m1.writeMicroseconds(1100);
    m2.writeMicroseconds(1100);
    m3.writeMicroseconds(1100);
    m4.writeMicroseconds(1100);
    m5.writeMicroseconds(OFF);
    m6.writeMicroseconds(OFF);
    m7.writeMicroseconds(OFF);
    m8.writeMicroseconds(OFF);

  }


  // UP
  if ( packetBuffer[0] == 'b' && packetBuffer[1] == 'u') {


    m1.writeMicroseconds(1800);
    m2.writeMicroseconds(1800);
    m3.writeMicroseconds(1800);
    m4.writeMicroseconds(1800);
    m5.writeMicroseconds(OFF);
    m6.writeMicroseconds(OFF);
    m7.writeMicroseconds(OFF);
    m8.writeMicroseconds(OFF);

  }


  // Forward
  if ( packetBuffer[0] == 'm' && packetBuffer[1] == 'f') {
    m1.writeMicroseconds(OFF);
    m2.writeMicroseconds(OFF);
    m3.writeMicroseconds(OFF);
    m4.writeMicroseconds(OFF);
    m5.writeMicroseconds(forward(packetBuffer[2]));
    m6.writeMicroseconds(forward(packetBuffer[2]));
    m7.writeMicroseconds(forward(packetBuffer[2]));
    m8.writeMicroseconds(forward(packetBuffer[2]));
  }

  // Backward
  if ( packetBuffer[0] == 'm' && packetBuffer[1] == 'b') {

    m1.writeMicroseconds(OFF);
    m2.writeMicroseconds(OFF);
    m3.writeMicroseconds(OFF);
    m4.writeMicroseconds(OFF);
    m5.writeMicroseconds(reverse(packetBuffer[2]));
    m6.writeMicroseconds(reverse(packetBuffer[2]));
    m7.writeMicroseconds(reverse(packetBuffer[2]));
    m8.writeMicroseconds(reverse(packetBuffer[2]));

  }

  //Right
  if ( packetBuffer[0] == 'm' && packetBuffer[1] == 'r') {

    m1.writeMicroseconds(OFF);
    m2.writeMicroseconds(OFF);
    m3.writeMicroseconds(OFF);
    m4.writeMicroseconds(OFF);
    m5.writeMicroseconds(reverse(packetBuffer[2]));
    m6.writeMicroseconds(forward(packetBuffer[2]));
    m7.writeMicroseconds(forward(packetBuffer[2]));
    m8.writeMicroseconds(reverse(packetBuffer[2]));

  }

  //Left
  if ( packetBuffer[0] == 'm' && packetBuffer[1] == 'l') {

    m1.writeMicroseconds(OFF);
    m2.writeMicroseconds(OFF);
    m3.writeMicroseconds(OFF);
    m4.writeMicroseconds(OFF);
    m5.writeMicroseconds(forward(packetBuffer[2]));
    m6.writeMicroseconds(reverse(packetBuffer[2]));
    m7.writeMicroseconds(reverse(packetBuffer[2]));
    m8.writeMicroseconds(forward(packetBuffer[2]));

  }

  //Stop
  if ( packetBuffer[0] == 's') {

    m1.writeMicroseconds(OFF);
    m2.writeMicroseconds(OFF);
    m3.writeMicroseconds(OFF);
    m4.writeMicroseconds(OFF);
    m5.writeMicroseconds(OFF);
    m6.writeMicroseconds(OFF);
    m7.writeMicroseconds(OFF);
    m8.writeMicroseconds(OFF);

  }






}



int forward(char s) {
  return map(s, 0, 25, 1500, 1100);
}

int reverse(char s) {
  return map(s, 0, 25, 1500, 1800);
}
