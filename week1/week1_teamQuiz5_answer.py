# Quiz 5.

from multiprocessing import Value
from pickle import TRUE
from tkinter import FALSE


inputs = "cat32dog16cow5"

def find_string(inputs):
    word = ''
    words = []
    for i, value in enumerate(inputs):
        if value.isdigit():
            if word != '':
                words.append(word)
            word = ''
        else:
            word += inputs[i]
    return words

string_list = find_string(inputs)
print(string_list)
