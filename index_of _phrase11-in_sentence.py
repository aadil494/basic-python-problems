phrase = "aabbcc" #phrase to be searched
sentence = "aabbaabbcc" # string in which we are searching a phrase

if phrase in sentence : # check if phrase exists in a sentence 
    print(sentence.index(phrase)) # find and print the starting index of the phrase in the sentence
