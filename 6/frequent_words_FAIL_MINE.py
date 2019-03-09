import math

def read_input(filename):
   file = open(filename, 'r')
   return file

def pattern_to_number(pattern):
   indexes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
   if pattern == "":
      return 0
   letter = pattern[len(pattern)-1]
   prefix = pattern[:-1]
   return 4 * pattern_to_number(prefix) + int(indexes.get(letter))
   
   
def number_to_pattern(idx, k):
   #indexes = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
   indexes = {0:'A', 1:'C', 2:'T', 3:'G'}
   if k == 1:
      #return list(indexes.keys())[list(indexes.values()).index(idx)]
      return indexes.get(idx)
   prefix_index = math.floor(idx/4)
   r = int(idx % 4)
   #print("r is " + str(r) + " and prefix_index is " + str(prefix_index))
   #letter = list(indexes.keys())[list(indexes.values()).index(r)]
   letter = indexes.get(r)
   prefix_pattern = number_to_pattern(prefix_index, k-1)
   return prefix_pattern + letter
   
   
   

def main():
   #p2a------------------------------------------------
   #short
   p2a_short = read_input("p2a_short.txt")
   p2a_dna_pattern = p2a_short.readline().rstrip()
   p2a_answer =  int(p2a_short.readline())
   if pattern_to_number(p2a_dna_pattern) == p2a_answer:
      print("Test passed for p2a_short.txt")
   else:
      print("Test failed for p2a_short.txt")
   #long
   p2a_long = read_input("p2a_long.txt")
   p2a_dna_pattern_long = p2a_long.readline().rstrip()
   p2a_answer_long = int(p2a_long.readline())
   if pattern_to_number(p2a_dna_pattern_long) == p2a_answer_long:
      print("Test passed for p2a_long.txt")
   else:
      print("Test failed for p2a_long.txt")
   
   
   
   
   
   #p2b------------------------------------------------
   #short
   p2b_short = read_input("p2b_short.txt")
   
   p2b_short_idx = int(p2b_short.readline())
   p2b_short_kval = int(p2b_short.readline())
   p2b_short_answer = p2b_short.readline()
   
   #print(p2b_short_idx)   
   #print(p2b_short_kval)
   print(p2b_short_answer)
   print(number_to_pattern(p2b_short_idx, p2b_short_kval))
   if number_to_pattern(p2b_short_idx, p2b_short_kval) == p2b_short_answer:
      print("Test passed for p2b_short.txt")
   else:
      print("Test failed for p2b_short.txt")
   
   #long
   p2b_long = read_input("p2b_long.txt")
   
   p2b_long_idx = int(p2b_long.readline())
   p2b_long_kval = int(p2b_long.readline())
   p2b_long_answer = p2b_short.readline()


if __name__ == "__main__":
   main()