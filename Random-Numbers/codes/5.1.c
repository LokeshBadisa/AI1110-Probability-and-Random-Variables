// Generates 1000000 samples of a uniform random variable taking values between 0 and 1 and stores them in a file called uni.dat

// Name: Lokesh Badisa
// Roll number: AI21BTECH11005

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	FILE *fp = fopen("ber.dat", "w");
	if (!fp) {
		printf("Couldn't open file\n");
		return 1;
	}
	for (int i = 0; i < NUM; i++) {
		fprintf(fp, "%lf\n", randomBernoulli());
	}
	fclose(fp);
	return 0;	
}
