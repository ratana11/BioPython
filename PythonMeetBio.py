
#20180419 thu
#https://stepik.org/lesson/23217/step/6?unit=6784
# 1.Where in the Genome Does DNA Replication Begin? (Part1)
# 1.3 Hidden Messages in the Replication Origin (Part2)
def FrequencyMap(Text, k):
    # your code here
    freq = {}
    n=len(Text)
    for i in range (n-k+1):
        Pattern = Text [i:i+k]
        if Pattern not in freq:
            freq [Pattern] = 1
# if a pattern found is not already  in the dictionary freq{}, it is assigned a value of 1 and added to the list
        else:
            freq [Pattern] +=1
# however, if the pattern is already in the dictionary, its value should go up by 1 (so if it has been found, it is initially given a pattern of 1, and then this adds another 1 if it is found again
    return freq

def FrequencyMap1(Text, k):
    freq = {}
    n = len(Text)
    for i in range (n-k+1):
        Pattern = Text [i:i+k]
        if Pattern not in freq:
            freq [Pattern] = 1
        else:
            freq [Pattern] += 1
    return freq
####Replication.py
def Reverse(Pattern):
    # your code here
    a = list(Pattern)
    a.reverse()
    rev = ''
    for cha in a:
        rev += cha
    return rev
def Reverse(Pattern):
    return Pattern[::-1]

def Complement(Pattern):
    # your code here
    rev = []
    for cha in Pattern:
        if cha == 'A':
            rev.append('T')
        elif cha == 'T':
            rev.append('A')
        elif cha == 'C':
            rev.append('G')
        else:
            rev.append('C')
    vef = ''
    for i in rev:
        vef += i
    return vef

#Your code complexity score is 8.12 (best for this step is 2.24).
def Complement(Pattern):
    # your code here
    f = ''
    for i in Pattern:
        if i == 'A':
            f += 'T'
        elif i == 'T':
            f += 'A'
        elif i == 'C':
            f += 'G'
        else:
            f += 'C'
    return f

#Your code complexity score is 2.24 (best for this step is 2.24).
MAPPING = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}
def Complement(Pattern):
    return ''.join(MAPPING[c] for c in Pattern)

#Your code complexity score is 3.61 (best for this step is 2.83).
# Input:  A DNA string Pattern
compdict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    compstring = ''
    for char in Pattern:
        compstring = compstring + compdict[char]
    return compstring

def ReverseComplement(Pattern):
    # your code here
    rev = Reverse(Pattern)
    com = Complement(rev)
    return com

def ReverseComplement(Pattern):
    # your code here
    return Reverse(Complement(Pattern))


def PatternMatching(Pattern, Genome):
    positions = []  # output variable
    # your code here
    Patternle = len(Pattern)
    Genomele = len(Genome)
    for i in range(Genomele):
        if Pattern == Genome[i:i + Patternle]:
            positions.append(i)

    return positions
# Copy your PatternMatching function below this line.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    # your code here
    Patternle = len(Pattern)
    Genomele = len(Genome)
    for i in range(Genomele):
        if Pattern == Genome[i:i+Patternle]:
            positions.append(i)
    return positions
#The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
# import sys                              # needed to read the genome
# input = sys.stdin.read().splitlines()   #
# v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# 1.5 An Explosion of Hidden Messages/
# 20180430 mon

# Copy your PatternCount function below here
def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(len(Text)- len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count +1
    return count

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

print('Hello world')

#20180509 wed
# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
# def SymbolArray(Genome, symbol):
#     array = {}
#     n = len(Genome)
#     ExtendedGenome = Genome + Genome[0:n//2]
#     for i in range(n):
#         array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
#     return array
def SymbolArray(Genome, symbol):
    array = []
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        count = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
        array.append(count)
    return array


# Reproduce the PatternCount function here.
def PatternCount(ExtendedGenome,symbol):
    count = 0
    for i in range(len(ExtendedGenome)):
        if ExtendedGenome[i:i+len(symbol)] == symbol:
            count +=1
    return count

print(SymbolArray('AAAAGGGG', 'A'))
Genome ='AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
symbol = 'CC'
print(SymbolArray(Genome,symbol))

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
