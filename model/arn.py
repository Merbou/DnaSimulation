from model import acids as acide
from model import protein as pro
acide = acide.acids


class arn(acide):

    def __init__(self, Sequance="AUCD"):
        """
        @parms String,String
        Init attributes
        @return Object
        """
        self.setNucleotides(["A", "U", "C", "G"])
        super().__init__(self.__parseARN(Sequance))

    def __parseARN(self, Sequance):
        """
        @parms String
        change T with U 
        @return String
        """
        return Sequance.replace("T", "U")

    def TranscribeProtein(self):
        """
        @params None
        Ceate Protein Object from RNA Object
        @return Object
        """
        return pro.protein(self)
