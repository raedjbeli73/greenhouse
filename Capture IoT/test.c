#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    // Initialisation aléatoire
    srand(time(NULL));

    // Simulation capteurs
    float temperature = 20 + (rand() % 1000) / 100.0;   // 20 → 30°C
    float humidity = 40 + (rand() % 600) / 10.0;        // 40 → 100%
    int soil = rand() % 1024;                           // 0 → 1023

    // Création JSON
    printf("{\n");
    printf("  \"device_id\": \"greenhouse_01\",\n");
    printf("  \"temperature\": %.2f,\n", temperature);
    printf("  \"humidity\": %.2f,\n", humidity);
    printf("  \"soil_moisture\": %d\n", soil);
    printf("}\n");

    return 0;
}
