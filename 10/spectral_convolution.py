from scoring import score
from spectrum import cyclic_spectrum
from collections import Counter
import collections
import heapq

def read_input(filename):
   file = open(filename, 'r')
   m_val = int(file.readline().rstrip('\n'))
   exp_spectrum = file.readline().rstrip('\n').split(' ')
   exp_spectrum = sorted(list(map(int, exp_spectrum)))
   answer = file.readline()
   return m_val, exp_spectrum, answer
   
def convolution(m_val, exp_spectrum):
   keepers = []
   for i in exp_spectrum:
      for j in exp_spectrum:
         value = i - j
         if 57 <= value <= 200:
            keepers.append(value)
   counts = Counter(keepers)
   most_frequent_list = collections.defaultdict(list)
   
   for key, value in counts.items():
      most_frequent_list[value].append(key)
   m_most_occurring = heapq.nlargest(m_val, most_frequent_list.keys())
   return_list = []
   
   idx = 0
   while len(return_list) < m_val:
      temp = most_frequent_list[m_most_occurring[idx]]
      for i in temp:
         return_list.append(i)
      idx += 1
   
   ret_string = ""
   for i in return_list:
      ret_string += str(i) + ' '
   
   return ret_string.rstrip(' ')
   
def check(my_answer, correct_answer):
   my_answer = sorted(my_answer.split(' '))
   correct_answer = sorted(correct_answer.split(' '))
   if my_answer == correct_answer:
      print("Test passed")
   else:
      print("Test FAILED.")
   
def main():
   
   short_mval, short_exp_spectrum, short_answer = read_input('P1_short.txt')
   check(convolution(short_mval, short_exp_spectrum), short_answer)
   
   long_mval, long_exp_spectrum, long_answer = read_input('P1_long.txt')
   check(convolution(long_mval, long_exp_spectrum), long_answer)
   
if __name__ == '__main__':
   main()