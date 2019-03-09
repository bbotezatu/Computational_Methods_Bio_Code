#Brandon Botezatu
#CS-327, Spring 2018
from Bio import SubsMat
from Bio.SubsMat import MatrixInfo

def read_input(filename):
   file = open(filename, 'r')
   sequence_one = file.readline().rstrip('\n')
   sequence_two = file.readline().rstrip('\n')
   similarity_score = int(file.readline().rstrip('\n'))
   answer = float(file.readline())
   return sequence_one, sequence_two, similarity_score, answer

def similarity(seq_one, seq_two):
   score = 0
   identical = 0
   for i in range(0, len(seq_one)):
      if seq_one[i] == seq_two[i]:
         identical += 1
      key = seq_one[i], seq_two[i]
      if key in MatrixInfo.blosum55.keys():
         score += MatrixInfo.blosum55[key]
      else:
         key = seq_two[i], seq_one[i]
         score += MatrixInfo.blosum55[key]
   percentage = identical / len(seq_one) * 100
   
   return score, percentage

def check(filename):
   sequence_one, sequence_two, score, answer = read_input(filename)
   my_score, my_answer = similarity(sequence_one, sequence_two)
   if my_score == score and my_answer == answer:
      print("Test passed for " + filename)
   else:
      print("Test FAILED for " + filename)

def main():
   check('P1_short.txt')
   check('P1_long.txt')

if __name__ == '__main__':
   main()