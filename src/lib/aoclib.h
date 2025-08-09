#ifndef AOCLIB_H
#define AOCLIB_H

#include <stdio.h>

/**
 * Get the input file for a specified year and date.
 *
 * @param year  Year of challenge
 * @param day   Day of challenge
 * @return Input file stream
 */
FILE *get_data(size_t year, size_t day);

#endif // AOCLIB_H