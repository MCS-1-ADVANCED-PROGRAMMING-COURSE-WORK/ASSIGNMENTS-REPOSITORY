

def words(string):                                                 #function taking in one argument              
    accumulating_word = ""                                         #variable to store words as they accumulate character by character
    provisional_output_list = []                                   #list to hold all fully formed words
    output_list = []                                               #list to hold words with no repitition
    for c in string:                                               #for loop iterating over the input string               
        accumulating_word += c                                     #concatenating characters one by one to the word holder
        if c == " ":                                               #checking for space to delimit the word
            provisional_output_list.append(accumulating_word)      #add word as list item
            accumulating_word = ""                                 #reset word holder
    for i in provisional_output_list:                              #for loop iterating over the all words list
        if i not in output_list:                                   #checking if teh current list item is present in the output list
            output_list.append(i)                                  #adding only list items that aren't yet added to teh final output list
    return output_list


#TESTING
random_string = "to be or not to be"
print(words(random_string))
