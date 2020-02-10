from random import randint
from random import choice


class acids():
    __Sequance = ""
    __nucleotides = list()

    def __init__(self, Sequance):
        """
        @parms String
        test & assignment Acide 
        @Return Object
        """
        try:

            if(not self.validtor(Sequance.upper())):
                # if Sequance not valide throw exception
                raise TypeError()

            self.__Sequance = Sequance.upper()

        except TypeError:
            print("Oops!  That was no valid ADN...")

    def validtor(self, Sequance):
        """
        @params String
        Test if acide is valide 
        @return Boolean
        """
        lenNecleotide =\
            Sequance.count(self.__nucleotides[0]) +\
            Sequance.count(self.__nucleotides[1]) +\
            Sequance.count(self.__nucleotides[2]) +\
            Sequance.count(self.__nucleotides[3])

        return lenNecleotide == len(Sequance)

    def generate(self, size=4):
        """
        @params int
        generate acides from __nucleotides with size
        @return String
        """
        self.__Sequance = self.__ranStr(self.__nucleotides, size)
        return self.getSequance()

    def reverseComplement(self):
        """
        @params None
        Create reverse Complement of acide
        @return String
        """
        reverseComp = ""

        for nucleotide in self.__Sequance:

            reverseComp += self.__reverseNucleotide(nucleotide)

        return reverseComp[::-1]

    def mutations(self, number):
        """
        @params Int 
        mutate an acids
        @return String
        """
        Sequance = list(self.__Sequance)

        for i in range(number):
            i
            # mutate with random index from [0,len(Sequance)]
            Sequance = self.__mutation(
                Sequance, randint(0, len(self.__Sequance)))

        self.__Sequance = "".join(Sequance)

        return self

    def FrequencyNucleotides(self):
        """
        @params None
        return Frequency of all Nucleotides in Sequance
        @return dict
        """
        return {
            self.__nucleotides[0]: self.__FrequencyNucleotide(self.__nucleotides[0]),
            self.__nucleotides[1]: self.__FrequencyNucleotide(self.__nucleotides[1]),
            self.__nucleotides[2]: self.__FrequencyNucleotide(self.__nucleotides[2]),
            self.__nucleotides[3]: self.__FrequencyNucleotide(
                self.__nucleotides[3])
        }

    def tauxCG(self):
        """
        @params None
        Return Rate Of CG %
        @return Float
        """
        freqNucleo = self.FrequencyNucleotides()
        
        sumfreq = sum(freqNucleo.values())
        
        return ((freqNucleo["G"]+freqNucleo["C"])*100)/sumfreq

    def FrequencyCodons(self):
        """
        @params None
        return Frequency of Codons 
        @return Dict
        """
        FreqCodons = {}

        #loop from 0 to len-3 step 3
        for i in range(0, len(self.__Sequance)-3, 3):

            #get Codon from Sequance
            codon = self.__Sequance[i:i+3]

            #if the codon exists increment
            if(codon in FreqCodons.keys()):

                FreqCodons[codon] += 1

            else:
                #create codon
                FreqCodons.update({codon: 1})

        return FreqCodons

#################### HELPERS ###################################
                                                               #
    def __FrequencyNucleotide(self, nucleotide):
        """
        @params String
        return Frequency of Nucleotide in Sequance
        @return int
        """
        # index of nucleotide
        index = self.__nucleotides.index(nucleotide)

        return self.__Sequance.count(self.__nucleotides[index])

    def __reverseNucleotide(self, nucleotide):
        """
        @params String
        return reverse of each nucleotides
        @return String
        """
        if(nucleotide == "C"):
            return "G"
        else:
            if(nucleotide == "G"):
                return "C"
            else:
                if(nucleotide == "A"):
                    return "T"
                else:
                    if(nucleotide == "T"):
                        return "A"

    def __mutation(self, Sequance, index):
        """
        @parms String,Int
        mutate nucleotide 
        @return
        """
        while True:
            # mutate
            nucleotide = choice(self.__nucleotides)

            # ensure if nucleotide has mutated
            if(nucleotide != Sequance[index]):

                Sequance[index] = nucleotide

                return Sequance

    def __ranStr(self, str, size):
        """
        @params string , size
        create random acide from str
        @return String
        """
        return ''.join(choice(str) for i in range(size))

################################################################
#################### GETTERS ###################################
                                                               #

    def getSequance(self):
        """
        @params None
        Return Sequance
        @return String
        """
        return self.__Sequance

    def getNucleotides(self):
        """
        @params None
        return nucleotides
        @return list
        """
        return self.__nucleotides

################################################################
#################### SETTERS ###################################
                                                               #

    def setSequance(self, Sequance):
        """
        @parms String
        Test & assignemnt new Sequance 
        @return None
        """
        try:
            if(not self.validtor(Sequance.upper())):
                raise TypeError()
            self.__Sequance = Sequance.upper()
        except TypeError:
            print("Oops!  That was no valid ADN.  Try again...")

    def setNucleotides(self, nucleotides):
        """
        @parms String
        Test & assignemnt new nucleotides 
        @return None
        """
        self.__nucleotides = nucleotides
        return self.__nucleotides

################################################################