
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
def PatternCount(Pattern,Text):
    count = 0
    for i in range(len(Pattern)):
        if Pattern[i:i+len(Text)] == Text:
            count +=1
    return count

def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    print(ExtendedGenome[-1])
    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

#Genome ='AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT'
#symbol = 'CC'
#print(SymbolArray(Genome,symbol))
#print(FasterSymbolArray('AAAAGGGG', 'A'))
#print(FasterSymbolArray(Genome, symbol))


#20180510 thu
print('Hello world')
#print(len(split('0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2')))

a=('0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2')
b=a.split()
c = len(b)
print(c)

Genome = 'CATGGGCATCGGCCATACGCC'
#0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
def SkewArray1(Genome):
    # your code here
    skew =[0]
    l = len(Genome)
    for i in range(0, 4):
        print(Genome[i])
        if Genome[i] == 'C':
            skew.append(skew[i-1]-1)
            print(skew)
        elif Genome[i] == 'A'or'T':
            skew.append(skew[i])
            print(skew)
        else:
            skew.append(1)
    return skew

#20180516 wed
# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = []
    SkewVariable = SkewArray(Genome)
    #find the minimum value of all values in the skew array
    minNumber = min(SkewVariable.values())
    #ragne over the length of the skew array and add all positions achieving the min to positions
    for i in SkewVariable:
        if SkewVariable[i] == minNumber:
            positions.append(i)

    return positions

# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    Skew={0:0}
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == "C":
            Skew[i] = Skew[i-1]-1
        elif Genome[i-1] == "G":
            Skew[i] = Skew[i-1]+1
        else:
            Skew[i] = Skew[i-1]
    return(Skew)

#20180517 thu
#1.5 Some Hidden Messages Are More Elusive than Others
# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(0,len(p)):
        if p[i] != q[i]:
            count += 1
    return count

# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
# Pattern ='ATTCTGGA'
# Text ='CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT'
# d=3
# [6, 7, 26, 27]
def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    n = len(Text)
    m = len(Pattern)
    for i in range(0,n-m+1):
        if HammingDistance (Pattern, Text[i:i+m]) <= d:
            positions.append(i)
    return positions


def HammingDistance(p, q):
    # your code here
    count = 0
    for i in range(0,len(p)):
        if p[i] != q[i]:
            count += 1
    return count

#20180518 fri
# Insert your Hamming distance function on the following line.
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    # your code here
    positions = ApproximatePatternMatching(Text, Pattern, d)
    count = len(positions)
    return count

# def ApproximatePatternCount(Pattern, Text, d):
#     return len(ApproximatePatternMatching(Text, Pattern, d))

#20180523
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"Motifs.py"
# Profile = {
# 'A' : [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.1, 0.2, 0.3, 0.4, 0.5],
# 'C' : [0.3, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.4, 0.3, 0.2, 0.2, 0.1],
# 'G' : [0.2, 0.1, 0.4, 0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1],
# 'T' : [0.3, 0.4, 0.1, 0.1, 0.1, 0.1, 0.0, 0.2, 0.4, 0.4, 0.2, 0.3]
# }
# Text ='TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA'
# k = 12
# def ProfileMostProbablePattern(Text, k, Profile):
#     ip = -1
#     pmpp = []
#     for i in range (len(Text)-k+1):
#         temp = Text[i:i+k]
#         pr = Pr(temp, Profile)
#         if pr > ip:
#             ip = pr
#             pmpp = temp
#     return pmpp
# Copy the ten strings occurring in the hyperlinked DosR dataset below.
# Dna = ['GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC',
# 'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG',
# 'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC',
# 'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC',
# 'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG',
# 'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA',
# 'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA',
# 'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG',
# 'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG',
# 'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC']
#Motifs = ['AACGTA','CCCGTT','CACCTT','GGATTA','TTCCGG']
def Count(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
#20180524 thu
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = Count(Motifs)
    for i in profile.keys():
        k = profile[i]
        profile[i] = list(map(lambda a: a/t, k))
    return profile
# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus
def Score(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    score = 0
    consensus = Consensus(Motifs)
    for i in range(t):
        for j in range(k):
            if consensus[j] != Motifs[i][j]:
                score += 1
    return score
#20180525
#1.4 Greedy Motif Search
def Pr(Text, Profile):
    p =1
    k = len(Text)
    for i in range(k):
        p = Profile[Text[i]][i]*p
    return p
#20180528 mon
def ProfileMostProbablePattern(Text, k, Profile):
    patterns = {}
    for i in range(len(Text) - k + 1):
        patterns[Text[i:i + k]] = Pr(Text[i:i + k], Profile)
    return max(patterns.items(), key=lambda x: x[1])[0]
#20180530 wed
def GreedyMotifSearch(Dna, k, t):
	# type your GreedyMotifSearch code here.
	BestMotifs = []
	for i in range(0, t):
		BestMotifs.append(Dna[i][0:k])
	n = len(Dna[0])
	for i in range(n-k+1):
		Motifs = []
		Motifs.append(Dna[0][i:i+k])
		for j in range(1, t):
			P = Profile(Motifs[0:j])
			Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs
###week4 Which DNA Patterns Play The Role of Molecular Clocks? (Part 2)
#20180531 thu
def CountWithPseudocounts(Motifs):
    count = {} # initializing the count dictionary
    k = len(Motifs[0])
    t = len(Motifs)
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = CountWithPseudocounts(Motifs)
    for i in profile.keys():
        val = profile[i]
        profile[i] = list(map(lambda a: float(a)/(t+4), val))
        #profile[i] = [float(x)/ (t+4) for x in profile[i]]
    return profile
#20180605 tue
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = [] # output variable
    # your code here
    for i in range(0,t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
# Dna = [
# 'GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC',
# 'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG',
# 'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC',
# 'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC',
# 'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG',
# 'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA',
# 'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA',
# 'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG',
# 'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG',
# 'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC'
# ]
# t = len(Dna)
# k = 15
# Motifs = GreedyMotifSearchWithPseudocounts(Dna, k, t)
# print(Motifs)
# print(Score(Motifs))
# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    k = len(Profile['A'])
    for i in range(t):
        motifs.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return motifs
#20180608 fri
# import Python's 'random' module here
import random
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t): #from solution
    Motifs = []
    for i in range(t):
        ind = random.randint(0, len(Dna[0])-k)
        motif = Dna[i][ind:ind+k]
        Motifs.append(motif)
    return Motifs


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M
     while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs
# Copy the ten strings occurring in the hyperlinked DosR dataset below.

# Dna = [
# 'GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC',
# 'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG',
# 'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC',
# 'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC',
# 'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG',
# 'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA',
# 'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA',
# 'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG',
# 'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG',
# 'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC'
# ]
#
# # set t equal to the number of strings in Dna, k equal to 15, and N equal to 100.
# t = len(Dna)
# k =15
# N =100
# # Call RandomizedMotifSearch(Dna, k, t) N times, storing the best-scoring set of motifs
# # resulting from this algorithm in a variable called BestMotifs
# BestMotifs = RandomizedMotifSearch(Dna, k, t)
# for i in range(N-1):
#     M = RandomizedMotifSearch(Dna,k,t)
#     if Score(BestMotifs)>Score(M):
#         BestMotifs = M
# # Print the BestMotifs variable
# print(BestMotifs)
# # Print Score(BestMotifs)
# print(Score(BestMotifs))
#20180610 sun
#1.4 Gibbs Sampling
# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    sumPr = sum(Probabilities.values())
    dickey=Probabilities.keys()
    for i in dickey:
        Probabilities[i] /= sumPr
    return Probabilities
#20180610
def WeightedDie(Probabilities):
    random_float = random.uniform(0,1)
    input_keys = []
    input_values = []
    for key, value in sorted(Probabilities.items()):
        input_keys.append(key)
        input_values.append(value)

    current = 0
    range_of_values = []
    for i, value in enumerate(input_values):
        current += value
        range_of_values.append(current)

    for i, value in enumerate(range_of_values):
        if value >= random_float:
            return(input_keys[i])
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

def GibbsSampler(Dna, k, t, N):
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = RandomizedMotifSearch(Dna,k,t)
    for j in range(N-1):
        i = random.randint(0,t-1)
        Profile = ProfileWithPseudocounts(Motifs)
        #Motifi = ProfileGeneratedString(Dna, Profile, i)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        return BestMotifs
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    #randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    Motifs = RandomMotifs(Dna, k, t)
    #BestMotifs ← Motifs
    BestMotifs = Motifs.copy()
    #for j ← 1 to N
    for j in range(N):
    #    i ← randomly generated integer between 1 and t
        i = random.randint(0,t-1)
    #    Profile ← profile matrix formed from all strings in Motifs except for Motifi
        Profile = ProfileWithPseudocounts(Motifs[0:i] + Motifs[i+1:])
    #    Motifi ← Profile-randomly generated k-mer in the i-th string
        Motifs[i] = ProfileGeneratedString(Dna[i], Profile, k)
    #if Score(Motifs) < Score(BestMotifs)
        if Score(Motifs) < Score(BestMotifs):
    #    BestMotifs ← Motifs
            BestMotifs = Motifs
    return BestMotifs
Dna=['GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC',
'CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG',
'ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC',
'GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC',
'GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG',
'CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA',
'GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA',
'GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG',
'GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG',
'TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC']

# set t equal to the number of strings in Dna, k equal to 15, and N equal to 100
t = len(Dna)
k=15
N=100
# Call GibbsSampler(Dna, k, t, N) 20 times and store the best output in a variable called BestMotifs
BestMotifs = GibbsSampler(Dna, k, t, N)
for i in range(20):
    B = GibbsSampler(Dna, k, t, N)
    if Score(BestMotifs) < Score(B):
        BestMotifs = B
# Print the BestMotifs variable
print(BestMotifs)
# Print Score(BestMotifs)
print(Score(BestMotifs))

#COURSE1 Finding Hidden Messages in DNA (Bioinformatics I)
#https://www.coursera.org/specializations/bioinform
#20180612 tue Where in the Genome Does DNA Replication Begin
#1.2 Hidden Messages in the Replication Origin
Text ='CGATGTGCGACGGAGCGACGGGGGAGATTCGCGACGGAGCGACGGGCGACGGGCGACGGTGCGACGGCCGCGACGGGCGACGGCCGCGACGGGAATGCGACGGAGCGACGGGCGCGACGGAGCGACGGCCGCGACGGGCGCGACGGAGCGACGGGTGCAGCGGCCGGCGACGGGCGACGGGCGCGACGGAGCGACGGCGCGACGGAGCGACGGGCGACGGGCGACGGCTGGCGACGGTGCGACGGCTTGGGCGACGGTGGCGACGGCGCGACGGCTGCGACGGCGCGACGGGAGCGACGGGCGACGGTTGCGACGGGGGCGACGGCGCGACGGCCAGCGTACGCGCGACGGCCGCGACGGGCGACGGGCGACGGGAGCGACGGATGCGACGGCGCGACGGGCGACGGTCGCGACGGTTCTGCGACGGCCGCGACGGCGCGACGGTGCGACGGGCGACGGACGGCGACGGGCGACGGCGCGACGGTTGCGACGGGGCGACGGGCGACGGTGCGACGGGTGCGACGGCGTCGCGACGGTACAGCGACGGCGGCGACGGGTCTCGCGACGGGCCGCGACGGCGTCTCAGTTTGCTAGCGCGACGGCCGTCTGCGACGGTATGGCGACGGGTGCGACGGGCGCGACGGGGATGCGACGGGCGACGGGCGACGGGCGTATGCGACGGAGCGACGGGCGACGGAGGCGACGGGCGACGGATGCGACGGGCGACGGGGAAGGGTGAAACCTGTAACGCGACGGTGCGACGGGCGACGGGAGCGACGGATGGCGACGGAGCGACGGCGCGACGGTGAAACGCGACGGGCGACGGGCGACGGGGCCCGCGACGGGCGACGGTTAGCGACGGATGCGACGGAGCGACGGATCGTGCGACGGATGCGACGGATGCGACGGCCACTGCGACGGGTGCGACGGCTGGCGACGGCGCGACGGCAGTGCGACGG'
Pattern ='GCGACGGGC'
def PatternCount(Text, Pattern):
    count = 0
    T = len(Text)
    P = len(Pattern)
    for i in range(T-P+1):
        if Text[i:i+P] == Pattern:
            count += 1
    return count
def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = []
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count.append(PatternCount(Text, Pattern))
    maxCount = max(Count)
    for i in range(len(Text)-k+1):
        if Count[i] == maxCount:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatterns =list(set(FrequentPatterns))
    return FrequentPatterns
#1.3 Some Hidden Messages are More Surprising than Others
def ReverseComplement(Pattern):
    PatternCom=[]
    for i in range(len(Pattern)):
        if Pattern[i] == "A":
            PatternCom.append('T')
        elif Pattern[i] == "T":
            PatternCom.append('A')
        elif Pattern[i] == "C":
            PatternCom.append('G')
        elif Pattern[i] == "G":
            PatternCom.append('C')
    PatternCom.reverse()
    PatternCom = ''.join(PatternCom)
    print(type(PatternCom))
    return PatternCom
def PatternMatching(Pattern, Genome):  #20180619
    positions = []  # output variable
    # your code here
    Patternle = len(Pattern)
    Genomele = len(Genome)
    for i in range(Genomele):
        if Pattern == Genome[i:i+Patternle]:
            positions.append(i)
    positions = ' '.join(str(e) for e in positions)
    return positions
#1.4 An Explosion of Hidden Messages
