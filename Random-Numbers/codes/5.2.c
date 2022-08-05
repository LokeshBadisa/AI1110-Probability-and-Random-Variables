// Generates 1000000 samples of a random variable Y = AX + N

// Name: Lokesh Badisa
// Roll number: AI21BTECH11005

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	generateY("y.dat", NUM, 5);
	return 0;	
}
