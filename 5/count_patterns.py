def read_input(filename):
   file = open(filename, 'r')
   text = file.readline()
   pattern = file.readline()
   answer = int(file.readline())
   return text, pattern, answer

def count(text, pattern):
   count = 0
   text = text.rstrip()
   pattern = pattern.rstrip('\n')
   for i in range (len(pattern), len(text) + 1):
      check = text[i-len(pattern):i]
      if check == pattern:
         count += 1
   return count

def main():
   #first pattern file
   first_text, first_pattern, first_answer = read_input("pattern1.txt")
   if first_answer == count(first_text, first_pattern):
      print("Test passed for first text pattern.")
   else:
      print("Test failed for first text pattern.")
      
   #second pattern file
   second_text, second_pattern, second_answer = read_input("pattern2.txt")
   if second_answer == count(second_text, second_pattern):
      print("Test passed for second text pattern.")
   else:
      print("Test failed for second text pattern.")
   
if __name__ == "__main__":
    main()
    