#Brandon Botezatu
#CS-327, Spring 2018

def read_input(file_name):
   file = open(file_name, 'r')
   peptide = file.readline().rstrip('\n')
   #for i, val in enumerate(peptide):
   #   peptide[i] = int(peptide[i])
   ans = file.readline().rstrip('\n')
   return peptide, ans
   

def integer_masses(acid):
    masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113,
              'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147,
              'R': 156, 'Y': 163, 'W': 186}
    return masses[acid]

    
def accumulating_sums(i, peptide, spectrum, sum):
    for j in range(i + 1, len(peptide)):
        #sum += integer_masses(peptide[j])
        sum += peptide[j]
        spectrum.append(sum)
    return spectrum, sum
    
    
def wrapping_sums(i, peptide, spectrum, sum):
    if i >= 2:
        for k in range(0, i - 1):
            #sum += integer_masses(peptide[k])
            sum += peptide[k]
            spectrum.append(sum)
    return spectrum


def cyclic_spectrum(peptide):
   peptide = peptide.replace('-', ' ').split(' ')
   for i, val in enumerate(peptide):
      peptide[i] = int(peptide[i])

   #given a list of peptide masses
   spectrum = [0]
   for i in range(len(peptide)):
       #sum = integer_masses(peptide[i])
       sum = peptide[i]
       spectrum.append(sum)
       spectrum, sum = accumulating_sums(i, peptide, spectrum, sum)
       spectrum = wrapping_sums(i, peptide, spectrum, sum)
   return sorted(spectrum)


def main():
   cyclic_short, short_ans = read_input('cyclic_short.txt')   
   if cyclic_spectrum(cyclic_short) == short_ans:
      print("Test passed for cyclic_short.txt")
   else:
      print("Test FAILED for cyclic_short.txt")
   
   cyclic_long, long_ans = read_input('cyclic_long.txt')
   if cyclic_spectrum(cyclic_long) == long_ans:
      print("Test passed for cyclic_long.txt")
   else:
      print("Test FAILED for cyclic_long.txt")
   
   print(cyclic_short)
   print(cyclic_spectrum(cyclic_short))
   
if __name__ == '__main__':
   main()
