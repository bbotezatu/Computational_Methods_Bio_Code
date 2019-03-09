#Brandon Botezatu
#CS-327, Spring 2018

from collections import Counter

def read_input(file_name):
   file = open(file_name, 'r')
   first_line = file.readline().rstrip('\n').split(' ')
   second_line = file.readline().rstrip('\n').split(' ')
   answer = int(file.readline().rstrip('\n'))
   return first_line, second_line, answer

def score(theo_spectrum, exp_spectrum):
   a = Counter(theo_spectrum)
   b = Counter(exp_spectrum)
   output = 0
   
   for key in a:
      temp = 0
      if a[key] < b[key]:
         temp = int(a[key])
      elif b[key] <= a[key]:
         temp = int(b[key])
      output += temp
   return output

def main():
   theo_short, exp_short, short_ans = read_input('score_short.txt')

   if score(theo_short, exp_short) == short_ans:
      print("Test passed for score_short.txt")
   else:
      print("Test FAILED for score_short.txt")
   
   theo_long, exp_long, long_ans = read_input('score_long.txt')
   if score(theo_long, exp_long) == long_ans:
      print("Test passed for score_long.txt")
   else:
      print("Test FAILED for score_long.txt")
   
   
if __name__ == '__main__':
   main()