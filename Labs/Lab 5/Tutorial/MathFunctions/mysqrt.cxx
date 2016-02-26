#include <math.h>

double sqrt(double x) {
    // Catch negative numbers
    if (x <= 0)
        return 0;
    int exp = 0;
    x = frexp(x, &exp); // extract binary exponent from x
    // we want exponent to be even
    if (exp & 1) {
        exp--;
        x *= 2;
    }
    double y = (1+x)/2; // first approximation
    double z = 0;
    while (y != z) {
        z = y;
        y = (y + x/y) / 2;
    }
    return ldexp(y, exp/2); // multiply answer by 2^(exp/2)
}
