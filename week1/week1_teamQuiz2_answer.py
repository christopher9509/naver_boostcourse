# Quiz 2.

sentence = 'way a is there will a is there Where'

def reverse_sentence(sentence):
    sentence_split = sentence.split(' ')
    reverse_word = sentence_split[::-1]
    
    return reverse_word

print(' '.join(reverse_sentence(sentence)))