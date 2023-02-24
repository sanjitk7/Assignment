import json
import random
import argparse
from multiprocessing import Pool


# all possible alpha numeric chars
aph = [chr(i) for i in range(ord('a'), ord('z')+1)]
num = [str(i) for i in range(0,10)]
aph_num = aph + num

# generate_random_KV_pairs
def generate_key():
  word = ""
  for i in range(24):
    word = word + random.choice(aph_num)
  return word

def generate_value():
  word = ""
  for i in range(10):
    word = word + random.choice(aph_num)
  return word

# define arg to take - number of pairs
my_parser = argparse.ArgumentParser(description='Random Key:Pair Json Generator')
my_parser.add_argument('Pairs', metavar='pairs', type=int, help='number of key:value pairs to generate')

# take cli arg(s)
args = my_parser.parse_args()
pairs = args.Pairs
key_value = dict()

count = 1
for x in range(pairs):
  if count%50==0:
    print("PROGRESS: ",count)
  key = generate_key()
  value = generate_value()
  # print("key,valye:",(key, value))
  key_value.update({key: [value, 0]})
  count+=1

jsonString = json.dumps(key_value)
# print(jsonString)

# write to file
with open("new_million_word_dataset_" + str(pairs) + ".json", "w") as outfile:
    outfile.write(jsonString)