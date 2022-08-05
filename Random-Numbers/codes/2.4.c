// Calculates the mean and variance of a Gaussian distribution

// Name: Lokesh Badisa
// Roll number: AI21BTECH11005

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "header.h"

#define NUM 1000000

int main() {
	double *data = readData("codes/gau.dat", 1000000);
	
	printf("Empirical Mean = %lf\n", mean(data, 1000000));
	printf("Theoretical Mean = %lf\n", 0.0);

	printf("Empirical Variance = %lf\n", variance(data, 1000000));
	printf("Theoretical Variance = %lf\n", 1.0);

	return 0;
}
