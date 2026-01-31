*****************************************************************************
		PYTHON PROJECT-PASSWORD STRENGTH ANALYSER
*****************************************************************************
RE library:

Used RE library to pattern match the regex and password.

The pattern matching helps us in scoring the password with 5 criteria such as 
size, upper case and lower case, symbols and special characters.

alternating_mix:

This function is created to check if the password has an alternating sequence.
And a ratio: Alternating pairs to All possible pairs is returned.
Here Regex is not used like[A-Z][a-z]|[a-z][A-Z] because of the regex overhead
which will lead to slower performance if it reaches beyond a limit.

password_strength:
 
This function is created to score and give the result of the analysis. The regex 
pattern matching is done here for a simpler understanding.
So the password is given a score and the scoring is through regex pattern matching.
Then the score is used to give corresponding note if the password is strong or not.

main:

This main function has the input command and output command.

Note:

This program has been created in such a way that it can be implemented in another 
module and using it doesnt affect the working of the other module. 
This proper execution is possible through:
if __name__ == "__main__":
    main()
which ensures that only if the program is directly run the main function runs directly 
or else the main function of the parent module is run ensuring proper execution.
*****************************************************************************
