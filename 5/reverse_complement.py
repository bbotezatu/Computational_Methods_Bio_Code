def read_input(filename):
   file = open(filename)
   s = file.read().splitlines()
   return s
   
def original_dna(file):
   s = read_input(file)[0]
   return s

def rev_comp(original_dna):
   check_dna = ""
   new_dna = ""
   for i in range(len(original_dna)-1, 0-1, -1):
      check_dna += original_dna[i]
   for c in check_dna:
      if c == 'A':
         new_dna += 'T'
      if c == 'T':
         new_dna += 'A'
      if c == 'G':
         new_dna += 'C'
      if c == 'C':
         new_dna += 'G'
   return new_dna
   
def correct_comp(file):
   s = read_input(file)[1]
   return s
   
def main():
   #short dna
   original = original_dna("short_dna.txt")
   if(rev_comp(original) == correct_comp("short_dna.txt")):
      print("Correct reverse complement for short dna.")
   else:
      print("Incorrect reverse complement for short dna.")
   
   #long dna
   original = original_dna("long_dna.txt")
   if(rev_comp(original) == correct_comp("long_dna.txt")):
      print("Correct reverse complement for long dna.")
   else:
      print("Incorrect reverse complement for long dna.")
   

if __name__ == "__main__":
    main()