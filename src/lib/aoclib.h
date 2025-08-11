#ifndef AOCLIB_H
#define AOCLIB_H

#include <stdio.h>

/**********************************************
 *  LOGGERS                                   *
 *********************************************/

#if DEBUG

#define LOG(mode, fmt, ...) printf("%s " fmt "\n", mode, ##__VA_ARGS__)

#else

#define LOG(mode, fmt, ...)

#endif

/**
 * Print an array of <SOMETHING> separated by spaces.
 *      s -> String
 *      d -> Int
 *      l -> Long
 *      f -> Double
 *
 * @param a         Array to print
 * @param n         Number of elements to print
 */
void sprint(const char **a, size_t n);
void dprint(const int *a, size_t n);
void lprint(const long *a, size_t n);
void fprint(const double *a, size_t n);

/**********************************************
 *  UTILITIES                                 *
 *********************************************/

/**
 * Performs a Python-like strip() method to remove whitespace from
 * a string.
 *
 * @param str       String to strip
 * @return In-place stripped string
 */
char *strip(char *str);

/**
 * Performs Python-like split() mechanics.
 *
 * @param str       String to split
 * @param delim     Delimiter substring
 * @param len       Number of elements in returned list
 * @return List of split substrings
 */
char **split(const char *str, const char *delim, size_t *len);

/**
 * Read the lines of a string.
 *
 * @param fp        File pointer
 * @param len       Number of elements in returned list
 * @return List of lines found in file
 */
char **readlines(FILE *fp, size_t *len);

/**
 * Get the index of a character of a string.
 *
 * @param str       String to index
 * @param chr       Character to index
 * @param index if found, else -1
 */
int index_of(const char *str, char chr);

/**
 * In-place reversal of an array.
 *
 * @param arr       Array to reverse
 * @param len       Size of arr
 * @return Array post-reversal
 */
int *rev_array(int *arr, size_t len);

/**
 * Replaces every instance of a character with another.
 *
 * @param str       String to perform replacement
 * @param old       Old character
 * @param new       New character
 * @return Copy of string with characters replaced
 */
char *replace(const char *s, char old, char new);

/**
 * Gets the GCD of two numbers.
 *
 * @param a     First long
 * @param b     Second long
 * @return gcd(a,b)
 */
long gcd(long a, long b);

/**
 * Gets the LCM of two numbers.
 *
 * @param a     Array of numbers
 * @param n     Size of the array
 * @return LCM of a
 */
long lcm(const long a[], size_t n);

/**
 * Convert an array of strings into <SOMETHING>.
 *
 * @param a     Array of numbers
 * @param n     Size of the array
 * @return Converted array
 */
int *intify(char **a, size_t n);
long *longify(char **a, size_t n);

/**********************************************
 *  MAIN METHODS                              *
 *********************************************/

/**
 * Get the input file for a specified year and date.
 *
 * This method supports running the binary from anywhere, mainly
 * for debugging reasons. This requires the existence of the .git
 * directory so this method can find the root of the project.
 *
 * @param year      Year of challenge
 * @param day       Day of challenge
 * @return Input file stream
 */
FILE *get_datafile(size_t year, size_t day);

/**
 * Get the input data for a specified year and date.
 *
 * This method calls get_datafile and reads the buffer into a heap-
 * allocated string and returns this string. The user must free it.
 *
 * @param year      Year of challenge
 * @param day       Day of challenge
 * @return Input data string
 */
char *get_data(size_t year, size_t day);

#endif // AOCLIB_H
