## Asks for input, and prints a dictionary containing the tally of how many times each letter in the alphabet was used in the word.

## Get user to input sentence.
sentence = (input("Enter sentence to check: ")).lower()
length = len(sentence)
charc = 0
letter_dict = {}
## Iterate through the string and assign each new letter to a key.
while charc < length:

    ## If the letter is not in the current key list
    if sentence[charc] not in letter_dict.keys():

        ## Add it to the dictionary as a new key for that letter
        letter_dict[sentence[charc]] = 1
        charc += 1
    ## If the letter is already a key
    else:
        ## add the letter to the key list.
        letter_dict[sentence[charc]] += 1
        charc += 1
    
print(letter_dict)






## Print out the final count for each letter in the dictionary.
