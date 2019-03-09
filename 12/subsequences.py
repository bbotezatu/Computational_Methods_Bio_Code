#Brandon Botezatu
#CS-327, Spring 2018
from backtrack import backtrack_matrix

def find_lcs(backtrack, v, w):
   subsequence = ""
   for i in range(len(v), 1, -1):
      for j in range(len(w), 1, -1):
         if backtrack[i,j] == -1:
            i = i-1
            
         if backtrack[i,j] == 1:
            j = j-1
            
         if backtrack[i,j] == 0:
            subsequence += v[i-1]
            i = i-1
            j = j-1
   #reversal
   temp = ""
   for i in range (len(subsequence)-1, -1, -1):
      temp += subsequence[i]
   
   return temp
   
def find_lcs_alignment(backtrack, v, w):
   v_sub = ""
   w_sub = ""
   new_v = ""
   new_w = ""
   for i in range(len(v), 1, -1):
      for j in range(len(w), 1, -1):
         if backtrack[i,j] == 1:
            v_sub += '-'
            w_sub += w[j-1]
            j = j-1
         if backtrack[i,j] == -1:
            v_sub += v[i-1]
            w_sub += '-'
            i = i-1
         if backtrack[i,j] == 0:
            v_sub += v[i-1]
            w_sub += w[j-1]
            i = i-1
            j = j-1
   print(v_sub)
   print(w_sub)
   for i in range(len(v_sub)-1, 0, -1):
      new_v = v_sub[i]
   for i in range(len(w_sub)-1, 0, -1):
      new_w = w_sub[i]
   return new_v, new_w
      
            
def read_input(filename):
   file = open(filename, 'r')
   v = file.readline().rstrip('\n')
   w = file.readline().rstrip('\n')
   answer = file.readline().rstrip('\n')
   return v, w, answer

def check(filename):
   v, w, answer = read_input(filename)
   my_answer = find_lcs(backtrack_matrix(v, w), v, w)
   ans = ""
   for i in range(len(my_answer) - len(answer), len(answer)):
      ans += my_answer[i]
   
   if ans == answer:
      print("Test passed for " + filename)
   else:
      print("Test FAILED for " + filename)

def main():
   v, w, answer = read_input('P2b_short.txt')
   short_b = backtrack_matrix(v, w)
   check('P2a_short.txt')
   
   s = find_lcs(short_b, v, w)
   ans = ""
   for i in range (len(s)- len(answer), len(s)):
      ans += s[i]
   
   print(find_lcs_alignment(short_b, v, w))
   
if __name__ == '__main__':
   main()