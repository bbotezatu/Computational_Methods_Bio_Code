#Brandon Botezatu
#CS-327, Spring 2018

from spectrum import cyclic_spectrum
from scoring import score
import heapq
import collections
from spectral_convolution import convolution

def read_input(file_name):
   file = open(file_name, 'r')
   m_val = int(file.readline().rstrip('\n'))
   n_val = int(file.readline().rstrip('\n'))
   exp_spectrum = file.readline().rstrip('\n')
   exp_spectrum = list(map(int, exp_spectrum.split(" ")))
   answer = file.readline().rstrip('\n')
   return m_val, n_val, exp_spectrum, answer

def leaderboard(m_val, n_val, exp_spectrum):
   #masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
   masses = list(map(int, convolution(m_val, exp_spectrum).split(' ')))
   candidates = list(masses)
   max_exp = max(exp_spectrum)
   leader = '0'
   
   while candidates:
      d = collections.defaultdict(list)
      candidates = branch(masses, candidates)
      copy_candidates = list(candidates)
      for item in copy_candidates:
         current_peptide = item
         cyclic_theo = cyclic_spectrum(current_peptide)
         max_theo = max(cyclic_theo)
         if max_theo > max_exp:
            #candidates.remove(current_peptide) // This didn't work, threw 'x not in candidates' error.
            copy_candidates.remove(current_peptide)
         else:
            score_theo = score(cyclic_theo, exp_spectrum)#score of cyclic theo spectrum
            leader_cyclic_theo = cyclic_spectrum(leader)#cyclic theo spectrum of current leader peptide
            score_leader = score(leader_cyclic_theo, exp_spectrum)#score of leader cyclic theo spectrum
            if score_theo > score_leader:
               leader = current_peptide
            d[score_theo].append(current_peptide)         
         #bound pt2
         top_n_scores = get_top_n_scores(d, n_val)
         candidates = get_top_scorers(d, top_n_scores, n_val)
   return leader
   
def get_top_n_scores(d_list, n_val):
     key_list = d_list.keys()
     n_largest = heapq.nlargest(n_val, key_list)
     return n_largest   
     
     
# ranch with building blocks   
def branch(masses, candidate_list):
   #bb = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
   new_candidates = []
   for i in candidate_list:
      for j in masses:#bb:
         new_candidates.append(str(i) + '-' + str(j))
   return new_candidates
      
      
      
def get_top_scorers(d, top_n_scores, n_val):
     top_scorers = []
     i = 0
     while len(top_scorers) < n_val and i < len(top_n_scores):
          top_scorers.extend(d[top_n_scores[i]])
          i += 1
     return top_scorers

def check(leaderboard_res, answer):
   pass
"""
def init(exp_spectrum):

   candidates = []
   
   for i in exp_spectrum:
      if i in masses:
         candidates.append(i)
   return candidates
"""
def main():
   short_m_val, short_n_val, short_exp_spectrum, short_answer = read_input('P2_short.txt')
      
   if sorted(leaderboard(short_m_val, short_n_val, short_exp_spectrum).split('-')) == sorted(short_answer.split('-')):
      print("Test passed for P2_short.txt")
   else:
      print("Test failed for P2_short.txt")
   
   
   
   long_m_val, long_n_val, long_exp_spectrum, long_answer = read_input('P2_long.txt')
   if sorted(leaderboard(long_m_val, long_n_val, long_exp_spectrum).split('-')) == sorted(long_answer.split('-')):
      print("Test passed for P2_long.txt")
   else:
      print("Test failed for P2_long.txt")

if __name__ == '__main__':
   main()