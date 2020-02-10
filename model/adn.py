from model import acids as acide
from model import arn as a
acide = acide.acids

class adn(acide):
    __arn = object()

    def __init__(self, Sequance="ATCG", title="adn"):
        """
        @parms String,String
            Init attributes
        @return Object
        """
        self.setNucleotides(["A", "T", "C", "G"])
        self.title = title
        super().__init__(Sequance)

    def TranscribeARN(self):
        """
        @params None
        Create Object of RNA FROM DNA
        @return Object
        """
        self.__arn = a.arn(self.getSequance())
        return self.__arn

    def findMotifADN(self, motif):
        """
        @parms String
        Search motif from dna & return all positions
        @return list
        """
        Sequance = self.getSequance()
        positionMotif = list()

        lenMotif = len(motif)
        motif = motif.upper()

        for index in range(len(Sequance)-lenMotif+1):

            if(motif in Sequance[index:index+lenMotif]):

                positionMotif.append(index)

        return positionMotif
