#Brandon Botezatu
#CS-327-1, Spring 2018

from frequent_words import pattern_to_number, number_to_pattern

def computing_frequencies(dna_text, k):
   freqs = [0] * (4**k)
   for i in range(0, len(dna_text) - k): 
      pattern = dna_text[i:i+k]
      j = pattern_to_number(pattern)
      freqs[j] += 1
   return freqs

   
def frequent_words_faster(dna_text, k):
   freq_words = [] 
   freqs = computing_frequencies(dna_text, k)
   maximum = max(freqs)
   for index, value in enumerate(freqs):
      if value == maximum:
         pattern = number_to_pattern(index, k)
         freq_words.append(pattern)
   frequent_word_list = ' '.join(freq_words)
   return frequent_word_list


def read_input(filename):
   file = open(filename, 'r')
   dna_string = file.readline()
   k_val = file.readline()
   answer = file.readline()
   return dna_string.rstrip(), int(k_val.rstrip()), answer.rstrip()

   
def main():
   p12_short_string, p12_short_k, p12_short_answer = read_input('P12_short.txt')
   if frequent_words_faster(p12_short_string, p12_short_k) == p12_short_answer:
      print("Test passed for P12_short.txt")
   else:
      print("Test failed for P12_short.txt")
   
   p12_long_string, p12_long_k, p12_long_answer = read_input('P12_long.txt')
   if frequent_words_faster(p12_long_string, p12_long_k) == p12_long_answer:
      print("Test passed for P12_long.txt")
   else:
      print("Test failed for P12_long.txt")
   
   
if __name__ == '__main__':
   main()