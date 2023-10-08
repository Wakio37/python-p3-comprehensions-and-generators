#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [x for x in num_list if x % 2 == 0]
    return even_numbers

result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  


def make_exclamation(sentence_list):
    exclamation_sentences = [sentence + "!" for sentence in sentence_list]
    return exclamation_sentences

result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)  
