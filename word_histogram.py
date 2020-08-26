## Asks the user for a sentence as its input and prints a dictionary containing the tally of how many time each word is used.

## Prompt the user for a sentence.
sentence = (input("\nEnter sentence to check: ")).lower()
word_dict = {}
word = ''  ## declare an empty string named "word"
## Iterate through the string looking for each word.
for letter in sentence:  ## Take the each letter in string.
        
    
        ## If the letter is not a space "":
    if letter != " " and letter != ".":
        ## Append the letter to the string "word".
        word = word + letter

    ## Else, the letter is a space
    else:  
        ## If "word" is already a key word.
            if word in word_dict.keys():
            ## Increase the count value of the keyword +1.
                word_dict[word] += 1
                word = ''
            ## Else, assign "word" as a key in a new dictionary and create a count value of 1.
            else:
                word_dict[word] = 1
                word = ''
    ## Back to the top of loop.

## Print the dictionary.
print('\n',word_dict,'\n')