#Brandon Botezatu
#CS-327-1, Spring 2018

import matplotlib.pyplot as plt

def print_skew(dna_string):
   GC_diff = [0]
   GC_diff[0] = 0
   index_list = []
   c_count = 0
   g_count = 0
   for c in dna_string:
      if c == 'G':
         g_count += 1
      if c == 'C':
         c_count += 1
      GC_diff.append(g_count - c_count)
   min_val = min(GC_diff)
   for i in range(0, len(GC_diff)):
      if GC_diff[i] == min_val:
         index_list.append(str(i))
   index_list_string = ' '.join(index_list)   
   return index_list_string, GC_diff

def plot_skew(GC_diff):
   plt.plot(GC_diff,)
   #plt.axis([0, 6, 0, 20])
   plt.show()
   

def read_input(filename):
   file = open(filename, 'r')
   dna_string = file.readline()
   answer = file.readline()
   return dna_string, answer
   
def main():
   p3_short_string, p3_short_answer = read_input('P3_short.txt')
   p3_index_list_short, GC_diff_short = print_skew(p3_short_string)
   if p3_index_list_short == p3_short_answer:
      print("Test passed for P3_short.txt")
   else:
      print("Test failed for P3_short.txt")
      
   print()
   
   p3_long_string, p3_long_answer = read_input('P3_long.txt')
   p3_index_list_long, GC_diff_long = print_skew(p3_long_string)
   if p3_index_list_long == p3_long_answer:
      print("Test passed for P3_long.txt")
   else:
      print("Test failed for P3_long.txt")
      
   #Using matplotlib
      
   plot_skew(GC_diff_short)
   #plot_skew(GC_diff_long)

if __name__ == '__main__':
   main()