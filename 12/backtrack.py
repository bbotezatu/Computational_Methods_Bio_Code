#Brandon Botezatu
#CS-327, Spring 2018
import numpy as np


def backtrack_matrix(v, w):
   b = np.zeros((len(v)+1, len(w)+1))
   s = np.zeros((len(v)+1, len(w)+1))
      
   for i in range(1, len(v)+1):
      for j in range(1, len(w)+1):
         if v[i-1] == w[j-1]:
            z = s[i-1,j-1] + 1
         else:
            z = 0
         y = s[i, j-1]
         x = s[i-1,j]
         s[i,j] = max(x, y, z)
            
   #backtrack
   for i in range(len(v), 0, -1):
      for j in range(len(w), 0, -1):
         if s[i,j] == s[i-1,j]:
            b[i,j] = -1
            continue
         if s[i,j] == s[i, j-1]:
            b[i,j] = 1
            continue
         if s[i,j] == s[i-i, j-1]+1 and v[i-1] == w[j-1]:
            b[i,j] = 0
            continue   
   return b
   
def read_input(filename):
   file = open(filename, 'r')
   v = file.readline().rstrip('\n')
   w = file.readline().rstrip('\n')
   temp = file.readlines()
   s = ""
   
   #temp.replace('\n', ';')
   for item in temp:
      item = item.replace('\n', ';')
      s += item
   s = np.matrix(s)
   return v, w, s

def check(filename):
   v, w, answer = read_input(filename)
   temp = 0
   check = 0
   my_answer = backtrack_matrix(v, w)
   for i in range(0, len(v)):
      for j in range(0, len(w)):
         check += 1
         if my_answer[i,j] == answer[i,j]:
            temp += 1
   if temp == check:
      print("Test passed for " + filename)
   else:
      print("Test FAILED for " + filename)
      
def main():
   """Didn't know how to remove the periods from my own backtrack matrix, so
   I wasn't able to just compare the matrices directly to each other.   """
   check('P1_short.txt')
      
if __name__ == '__main__':
   main()
   