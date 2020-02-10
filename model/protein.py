from model import arn as a


class protein:
    __arn = object()
    __AMINOACID = {'UUU': 'Phe', 'UCU': 'Ser', 'UAU': 'Tyr', 'UGU': 'Cys', 'UUC': 'Phe', 'UCC': 'Ser', 'UAC': 'Tyr', 'UGC': 'Cys',
                   'UUA': 'Leu', 'UCA': 'Ser', 'UAA': '---', 'UGA': '---', 'UUG': 'Leu', 'UCG': 'Ser', 'UAG': '---', 'UGG': 'Urp',
                   'CUU': 'Leu', 'CCU': 'Pro', 'CAU': 'His', 'CGU': 'Arg', 'CUC': 'Leu', 'CCC': 'Pro', 'CAC': 'His', 'CGC': 'Arg',
                   'CUA': 'Leu', 'CCA': 'Pro', 'CAA': 'Gln', 'CGA': 'Arg', 'CUG': 'Leu', 'CCG': 'Pro', 'CAG': 'Gln', 'CGG': 'Arg',
                   'AUU': 'Ile', 'ACU': 'Thr', 'AAU': 'Asn', 'AGU': 'Ser', 'AUC': 'Ile', 'ACC': 'Thr', 'AAC': 'Asn', 'AGC': 'Ser',
                   'AUA': 'Ile', 'ACA': 'Thr', 'AAA': 'Lys', 'AGA': 'Arg', 'AUG': 'Met', 'ACG': 'Thr', 'AAG': 'Lys', 'AGG': 'Arg',
                   'GUU': 'Val', 'GCU': 'Ala', 'GAU': 'Asp', 'GGU': 'Gly', 'GUC': 'Val', 'GCC': 'Ala', 'GAC': 'Asp', 'GGC': 'Gly',
                   'GUA': 'Val', 'GCA': 'Ala', 'GAA': 'Glu', 'GGA': 'Gly', 'GUG': 'Val', 'GCG': 'Ala', 'GAG': 'Glu', 'GGG': 'Gly'}
    __molecule = list()

    def __init__(self, arn):
        """
        @parms Object
        Init attributes
        @return Object
        """
        self.__arn = arn
        self.parseProtein()

    def parseProtein(self):
        """
        @params None
        create list of aminoacids
        @return None
        """
        sequance = self.__arn.getSequance()
        self.__molecule = list()

        # loop with 3 step
        for i in range(0, len(sequance)-3, 3):
            if(self.__AMINOACID[sequance[i:i+3]]=="---"):
                continue
            self.__molecule.append(self.__AMINOACID[sequance[i:i+3]])

    def getProtein(self):
        """
        @parms None
        return list of aminoAcids
        @return list
        """
        return self.__molecule

    def printProtein(self):
        """
        @params None
        Print protein AC-AC-AC
        @return String
        """
        Protein = ""

        for amino in self.__molecule:
            amino += "-"
            Protein += amino
        return Protein[:-1]
