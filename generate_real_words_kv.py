import json
import random
import argparse
from multiprocessing import Pool

# words dictionary has list of all possible english words
def load_words():
  with open('words_dictionary.json') as json_file:
     words = json.load(json_file)
  return words

def random_word(words):
  word = random.choice(list(words))
  return word

# processes_count = 8
# processes_pool = Pool(processes_count)

# define arg to take - number of pairs
my_parser = argparse.ArgumentParser(description='Random Key:Pair Json Generator')
my_parser.add_argument('Pairs', metavar='pairs', type=int, help='number of key:value pairs to generate')

# take cli arg(s)
args = my_parser.parse_args()
pairs = args.Pairs

words = load_words()
key_value = dict()

count = 0
for x in range(pairs):
  print("count: ",count)
  key = random_word(words)
  value = random_word(words)
  key_value.update({key: [value, 0]})
  count+=1

jsonString = json.dumps(key_value)
# print(jsonString)

# write to file
with open("million_word_dataset_100k.json", "w") as outfile:
    outfile.write(jsonString)