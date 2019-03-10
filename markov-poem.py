#!/usr/bin/python
import random 
ngrams = {}
order = 1 
group_size = order + 1
total_words_to_generate = 30

with open("poem",'r') as poem_file:
    poems = poem_file.readlines()

def train(text):
  text = text.split()
  for i in range(0,len(text) - group_size):
    key = tuple(text[i: i + order])
    value = text[i + order]
    
    if key in ngrams:
      ngrams[key].append(value)
    else:
      ngrams[key] = [value]


def get_seed_word(ngrams):
    choice = random.choice(list(ngrams))
    return choice

def generate_poem():
    seed = get_seed_word(ngrams)
    result = []
    print("Seed word: {}".format(seed))
    result.append(seed[0])
    for i in range(total_words_to_generate):     
        next_word = random.choice(ngrams[seed])
        next_word_formatted_tuple = (next_word,)
        result.append(next_word)
        if next_word not in ngrams:
            seed = next_word_formatted_tuple
        else:
          break

    return " ".join(result)        

for poem in poems:
  train(poem)

print(generate_poem())  

