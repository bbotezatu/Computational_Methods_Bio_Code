#Brandon Botezatu
#CS-327, Spring 2018
from similarities import similarity
import numpy as np

def read_input(filename):
   file = open(filename, 'r')
   line_one = file.readline().rstrip('\n').split(' ')
   n_val = int(line_one[0])
   m_val = int(line_one[1])
   
   vert_string = ""
   
   for i in range(0, n_val - 1):
      vert_string += file.readline()
      if not i == n_val - 2:
         vert_string += ';'
      
   vert_edge_matrix = np.matrix(vert_string)
   
   hyphen = file.readline()
   horiz_string = ""
   
   for i in range(0, n_val):
      horiz_string += file.readline()
      if not i == n_val - 1:
         horiz_string += ';'
   horiz_edge_matrix = np.matrix(horiz_string)
   
   answer = int(file.readline().rstrip('\n'))
   return n_val, m_val, vert_edge_matrix, horiz_edge_matrix, answer
   
def mtp(n_val, m_val, vert_matrix, horiz_matrix):
   s = np.zeros((n_val, m_val))
   for j in range(1, m_val):
      s[0, j] = s[0, j-1] + horiz_matrix[0, j-1]
   for i in range(1, n_val):
      s[i, 0] = s[i-1, 0] + vert_matrix[i-1, 0]
   
   for i in range(1, n_val):
      for j in range(1, m_val):
         s[i,j] = max(s[i, j-1] + horiz_matrix[i,j-1], s[i-1,j] + vert_matrix[i-1, j])
   return(s[n_val-1, m_val-1])
   
def check(filename):
   n_val, m_val, vert_edge_matrix, horiz_edge_matrix, answer = read_input(filename)
   if mtp(n_val, m_val, vert_edge_matrix, horiz_edge_matrix) == answer:
      print("Test passed for " + filename)
   else:
      print("Test FAILED for " + filename)

def main():
   check('P2_short.txt')
   check('P2_long.txt')
   
if __name__ == '__main__':
   main()