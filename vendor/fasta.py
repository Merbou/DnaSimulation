from vendor import file as fl
from model import adn as a
file = fl.file


class fasta(file):

    def __init__(self, path):
        """
        @param String
        init object and the super Object
        @Object
        """
        self.__mode = "r"
        super().__init__(path, "r")

####### Function of course #############
    def __read_FASTA_strings(self):
        return (self.readFile().split('>'))[1:]

    def __read_FASTA_entries(self):
        return [seq.partition('\n') for seq in self.__read_FASTA_strings()]

    def __read_FASTA_sequences(self):
        return [[seq[0][:], seq[2].replace('\n', '')]
                for seq in self.__read_FASTA_entries()]
########################################

    def getFileAsSequences(self):
        """
        @param none
         Test&Return the content of fasta file
        @return list of list 
        """
        if 'fa' == self.getExtension():
            return self.__read_FASTA_sequences()

    def createDnaObjects(self):
        """
        @params None
        Create dna Objects from fasta file 
        @return list of Objects
        """
        ADNs = list()
        for sequance in self.__read_FASTA_sequences():
            # assignment title and sequance
            ADNs.append(a.adn(sequance[1], sequance[0]))
        return ADNs

    def __FASTA_sequencesToMatrix(self):
        """
        @params None
        convert all dna of fasta file in one matrix
        @Return Matrix
        """
        MatrixSequences = list()
        sequences = self.__read_FASTA_sequences()

        for sequence in sequences:
            # append sequance dna
            MatrixSequences.append(list(sequence[1]))

        return MatrixSequences

    def ADNProfile(self):
        """
        @params None
        Create dict and assignment list of occurrence each nucleotide
        @Return list profile , int length
        """
        sequences = self.__FASTA_sequencesToMatrix()
        length = len(sequences[0])

        nucleotides = {"A": [0]*length, "T": [0] *
                       length, "C": [0]*length, "G": [0]*length}

        for j in range(length):

            for i in range(len(sequences)):
                # increment nucleotide vertically
                # j lenth of cols of list profile & matrix
                nucleotides[sequences[i][j]][j] += 1
                # sequences Content matrix of nucleotide
                # [A,A,C,T,G]
                # [C,G,G,A,A]
                # [A,T,A,T,T]
                # [G,C,G,T,A]

        return [nucleotides, length]

    def ADNconsensus(self):
        """
        @params None
        create DNA consensus
        @params List
        """

        consensus = ""

        # Get profile list & length
        profileLength = self.ADNProfile()

        # Extract profileLength var
        profile = profileLength[0]
        length = profileLength[1]

        for i in range(length):
            # i => => => =>
            # A=>[2,1,1,1,2]
            # T=>[0,1,0,3,1]
            # C=>[1,1,1,0,0]
            # G=>[1,1,2,0,1]

            # Get value from each nucleotide
            A, T, C, G = profile["A"][i], profile["T"][i], profile["C"][i], profile["G"][i]

            # max of values
            MaxOcc = max(A, T, C, G)

            # Get nucleotide of max Occ
            consensus += self.maxNucleotideOcc(A, T, C, G, MaxOcc)

        return consensus

    def maxNucleotideOcc(self, A, T, C, G, max):
        """
        @params int,int,int,int,int
        return nucleotide of max value
        @return String 
        """
        if(A == max):
            return "A"
        if(T == max):
            return "T"
        if(C == max):
            return "C"
        if(G == max):
            return "G"
