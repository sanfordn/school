/***********************************************************
 * Name of program: strings.c
 * Authors: Nick Sanford
 * Description: Takes an input and tells you the amount of vowels in the 
 * 	string.
 **********************************************************/

/* These are the included libraries.  You may need to add more. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>

/* Put any symbolic constants (defines) here */
#define True 1 
#define False 0
#define MAX_SIZE 256
#define VOWEL_STR "AEIOU"
#define CONSONANTS "BCDFGHJKLMNPQRSTVWXYZ"
/* Declarations go here for functions that are called before they
 * are defined.  For example, the function named helper is called
 * in main before it is defined, so I declare it here. 
 */
void helper(char strInput[]);



/* This is the main function of your project, and it will be run
 * first before all other functions.
 */
int main(int argc, char *argv[])
{

	/* Variable definitions go at the top of functions */
	char strInput[MAX_SIZE];
	char quitStr[] = "quit\n";
	printf("Hello, Welcome to the strings program.\n");
	printf("If you want to quit at any point, type \"quit\" and press ENTER.\n");
	while (1) {
		
		printf("Please enter a string: ");
		fgets(strInput,MAX_SIZE,stdin);
		if(strcmp(strInput,quitStr) == 0) {
			break;
		}
		printf("Your String is: %s\n", strInput);
		helper(strInput);
		
		//research and use strtok
	}
	printf("Goodbye!\n");
	return 0;
}



void helper(char strInput[])
{
	for(int i = 0; i<strlen(strInput); i++) {
		strInput[i] = toupper(strInput[i]);
	}
	int numVowels = 0;
	int numCons = 0;
	int numWords = 0;
	char *token;
	char splitter[2] = " ";
	
	for(int i = 0; i<strlen(strInput); i++) {
		//search for vowels
		for(int j = 0; j<strlen(VOWEL_STR); j++) {
			if(strInput[i] == VOWEL_STR[j]) {
				numVowels++;
			}
		}
		//search for consonants
		for(int k = 0; k<strlen(CONSONANTS); k++) {
			if(strInput[i] == CONSONANTS[k]) {
				numCons++;
			}
		}
	}
	token = strtok(strInput, splitter);
	while(token != NULL) {
		numWords++;
		token = strtok(NULL, splitter);
	}
	
	printf("Your String has %i Vowels\n", numVowels);
	printf("Your string has %i Consonants\n", numCons);
	printf("Your String has %i Words\n", numWords);
}
