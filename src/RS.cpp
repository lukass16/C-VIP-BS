#include <Arduino.h>
#include <LoRa.h>
#include <SPI.h>
#include <lora_rswrapper.h>

//test

//defining receivable sensor variables
double lat = 0;
double lng = 0;
double alt = 0;

float magx = 0;
float magy = 0;
float magz = 0;

float temp = 0;
float pres = 0;
float bar_alt = 0;
float speed = 0;

//Packet stuff

int counter = 0;
int badPackets = 0;
int corruptedPackets = 0;
double successRate = 0;
float receivedRSSI = 0;
float receivedSNR = 0;
int receivedSize = 0;
int mathCounter = 0;
bool startCorruption = 0;
long freqError = 0;

//defining deserialization function
void deserializeData(char buffer[]){
  sscanf(buffer, "%lf,%lf,%lf,%f,%f,%f,%f,%f,%f,%d", &lat, &lng, &alt, &magx, &magy, &magz, &temp, &pres, &bar_alt, &counter); //for deserialization double ahs to vbe specified as %lf
}

//defining message string and deserialization buffer
String message = "";
char buffer[80] = "";

void setup()
{
  //Testing one by one
  Serial.begin(115200);
  Serial.println("Serial connected");

  //LoRa
  Serial.println("Setup LoRa");
  lora::setup();
}

void loop()
{
  //RSSI update
  receivedRSSI = lora::getPacketRssi();
  receivedSNR = lora::getPacketSNR();
  freqError = lora::freqError();
 
  message = lora::readMessage();
  // message.toCharArray(buffer, 80);
  // deserializeData(buffer);
        
}

  

