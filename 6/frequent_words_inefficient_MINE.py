from count_patterns import count

def frequent_words(dna_string, k):
   #For loop parsing the dna string, check string from idx 0 to idx k and 
   #call count_patterns with the string as the 'pattern' param. Have a 
   most_frequent_list = []
   max = 3
   most_frequent = ""
   for i in range(0, len(dna_string)-k):
      current_pattern = dna_string[i:i+k]
      if count(dna_string, current_pattern) >= max:
         most_frequent_list.append(current_pattern)
         max = count(dna_string, current_pattern)
   #return list(set(most_frequent_list))
   for item in sorted(list(set(most_frequent_list))):
      most_frequent += item + " "
   return most_frequent.rstrip()

def read_input(filename):
   file = open(filename, 'r')
   DNA_string = file.readline()
   k_int = int(file.readline())
   answer = file.readline()
   return DNA_string, k_int, answer

def main():
   #P1_short test
   
   first_string, first_k, first_answer = read_input("P1_short.txt")
   if frequent_words(first_string, first_k) == first_answer:
      print("Test passed for P1_short.txt")
   else:
      print("Test failed for P1_short.txt")
      
   #P1_long test   
   
   second_string, second_k, second_answer = read_input("P1_long.txt") 
   if frequent_words(second_string, second_k) == second_answer:
      print("Test passed for P1_long.txt")
   else:
      print("Test failed for P1_long.txt")   

if __name__ == "__main__":
    main()
    