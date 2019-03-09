
def linear_spectrum(peptide):
   pref_mass = [0]
   #pref_mass.append(0)
   int_masses = {'G':57, 'A':71, 'S': 87, 'P': 97, 
                 'V':99, 'T':101, 'C':103, 'I':113,
                 'L':113, 'N':114, 'D':115, 'K':128,
                 'Q':128, 'E':129, 'M':131, 'H':137,
                 'F':147, 'R':156, 'Y':163, 'W':186}
   
   for i in range(0, len(peptide)):
      for j in range(1, 20):
         if int_masses[j] == peptide[i]:
            pref_mass[i] = pref_mass[i-1] + int_mass[j]
   spectrum = [0]
   for i in range (0, len(peptide)-1):
      for j in range(i+1, len(peptide)):
         spectrum.append(pref_mass[j] - pref_mass[i])
   spectrum.sort()
   return spectrum

def cyclic_spectrum(sequence):
   pass

def read_input(filename):
   file = open(filename, 'r')
   amino_acid_sequence = file.readline()
   answer = file.readline()
   return amino_acid_sequence, answer

def main():
   sequence, answer = read_input('P1a_short.txt')
   print(linear_spectrum(sequence))

if __name__ == '__main__':
   main()