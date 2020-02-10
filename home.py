from vendor import chart as ch
from vendor import fasta as fa
from vendor import excel as xl
from model import adn as a

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
import sys
from itertools import permutations
Config.set('graphics', 'width', '1350')
Config.set('graphics', 'height', '270')
Config.set('graphics', 'resizable', '0')


class homeWindow(BoxLayout):
    fasta=None

###################### INITIATIONS #############################
                                                               #
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.index = 0
        self.whichArg()

    def whichArg(self):
        """
        @parms None
            Choose & Create dna
        @return None
        """
        if(sys.argv[2] == "path"):
            self.fastaToField(sys.argv[1])
            self.ADNconsensus()
        else:
            self.generateDna()

    def initField(self, adn):
        """
        @parms object
            init field of RNA,protein,reverseComplemen
        @return none
        """
        dna_reverse_field = self.ids.dna_reverse_field
        
        self.TranscribeRna(adn)
        self.TranscribeProtein()
        
        dna_reverse_field.text = adn.reverseComplement()

    def intiAdn(self, adn):
        """
        @parms object
            init all fields
        @return none
        """
        dna_field = self.ids.dna_field
        title_dna_field = self.ids.title_dna_field
        
        title_dna_field.text = adn.title
        dna_field.text = adn.getSequance()
        
        self.initField(adn)

    def generateDna(self):
        """
        @parms None
        generate DNA & assignemnt field of dna
        @return None
        """
        dna_size = int(sys.argv[1])
        self.ADNs = [a.adn()]

        self.ADNs[self.index].generate(dna_size)
        
        self.intiAdn(self.ADNs[self.index])

    def fastaToField(self, path):
        """
        @parms string
        assignemnt field of dna from fasta
        @return None
        """
        self.ADNs = self.__getDnaFromFasta(path)
        self.intiAdn(self.ADNs[self.index])

################################################################

###################### PAGINATIONS #############################
                                                               #
    def nextDna(self):
        """
        @parms None
            pass to the next DNA
        @return None
        """
        if(self.index < len(self.ADNs)-1):
            self.index += 1

            self.intiAdn(self.ADNs[self.index])

    def prevDna(self):
        """
        @parms
        back to the previous DNA
        @return
        """
        if(self.index > 0):
            self.index -= 1

        self.intiAdn(self.ADNs[self.index])

################################################################

###################### OPERATIONS ##############################
                                                               #
    def TranscribeRna(self, adn):
        """
        @parms Object
        Transcribe Rna & assignemnt field
        @return None
        """
        rna_field = self.ids.rna_field
       
        self.arn = adn.TranscribeARN()
       
        rna_field.text = self.arn.getSequance()

    def TranscribeProtein(self):
        """
        @parms
        Transcribe Protein & assignemnt field
        @return
        """
        protein_field = self.ids.protein_field
        self.protein = self.arn.TranscribeProtein()
        protein_field.text = self.protein.printProtein()

    def mutations(self):
        """
        @parms None
            mutate dna & init all field
        @return None
        """
        dna_mutations_nombre_field = self.ids.dna_mutations_nombre_field
        
        if(dna_mutations_nombre_field.text != ""):
            
            self.ADNs[self.index].mutations(
                int(dna_mutations_nombre_field.text))

            self.intiAdn(self.ADNs[self.index])

    def searchMotif(self):
        """
        @parms None
        start a schedule motif.py with position of motif
        @return None
        """
        dna_search_field = self.ids.dna_search_field
        
        if(dna_search_field.text != ""):
        
            positions = self.ADNs[self.index].findMotifADN(
                dna_search_field.text)

            from subprocess import Popen, PIPE
            Popen(['python', "motif.py", dna_search_field.text,
                   self.__listePosToString(positions)], stdout=PIPE, stderr=PIPE)

    def ADNconsensus(self):
        """
        @parms None
        assignemnt field of ADNconsensus 
        @return None
        """
        dna_cos_field = self.ids.dna_cos_field
        dna_cos_field.text = self.fasta.ADNconsensus()

################################################################


###################### CHART ###################################
                                                               #
    def rand_histo_nucleotide(self):
        """
        @parms None
        view chart histogram of Nucleotides in dna
        @return None
        """
        data = {"Nucleotides": ["A", "T", "C", "G"]}
        
        histo = ch.chart(self.__rand_histo_mutlip_nucleotide(data))
        
        histo.histo_chart("Nucleotides", "bar", "Frequency",
                          "Frequency Nucleotides")

    def rand_histo_codons(self):
        """
        @parms None
        view chart histogram of codons in dna
        @return None
        """
        ###create all codon
        codons = [''.join(codon) for codon in list(permutations("ATCG", 3))]

        data = {"Codons": codons}
        
        histo = ch.chart(self.__rand_histo_mutlip_codons(data))
        
        histo.histo_chart("Codons", "bar", "Frequency", "Frequency Codons")

    def rand_pie_rate_CG(self):
        """
        @parms None
        view Piezza chart of CG%
        @return None
        """
        data = {"Nucleotide": ["CG", "AT"]}
        
        data = self.__rand_PIE_mutlip_CG(data)

        chart = ch.chart(data)
        chart.pie_chart("Rate of CG%-TA%")

################################################################


#################### HELPERS ###################################
                                                               #

    def __getDnaFromFasta(self, path):
        """
        @parms string
            return object of dna from fasta file 
        @return list Of Object
        """
        self.fasta = fa.fasta(path)
        return self.fasta.createDnaObjects()

    def __listePosToString(self, positions):
        """
        @parms list
            convert list of int to string 
        @return string
        """
        fieldString = ""
        
        for position in positions:

            fieldString += ","
            fieldString += str(position)
        
        return fieldString[1:]

    def __rand_histo_mutlip_nucleotide(self, data):
        """
        @parms None
        create data from multipl dna
        @return dict
        """
        for dna in self.ADNs:

            title = dna.title
        
            nucleotidesFq = dna.FrequencyNucleotides()
            
            data.update({title: list(nucleotidesFq.values())})
        
        return data

    def __rand_histo_mutlip_codons(self, data):
        """
        @parms None
        create data from multipl dna
        @return dict
        """
        for dna in self.ADNs:
            ##title & Frequency codons of and[i]
            title = dna.title
            codonsFq = dna.FrequencyCodons()
            
            ## loop of all codons
            for codon in data["Codons"]:

                ##create title of dna[i]
                if(title not in data.keys()):
                    data[title] = list()
                
                #add 0 for no existing codon
                if(codon not in codonsFq.keys()):
                    data[title].append(0)
                    continue
                #add Frequency for existing codon
                data[title].append(codonsFq[codon])
        return data

    def __rand_PIE_mutlip_CG(self, data):
        """
        @parms dict
        create data for all dna
        @return dict
        """
        for dna in self.ADNs:
           
            title = dna.title
            rateCG = dna.tauxCG()
        
            data.update({title: [rateCG, 100-rateCG]})
        
        return data

################################################################

#################### EXPORTATION ###############################
                                                               #
    def export_to_excel(self):
        """
        @params None
        prepare & send to Excel class
        @return None
        """
        dna=self.ADNs[self.index]
        arn=dna.TranscribeARN()
        protein=arn.TranscribeProtein()
        
        data=self.__data_form(dna,arn,protein)
        
        xlx=xl.excel(data)
        path="C:/Users/Merouane/Desktop/BIOINFO-M1/S1/Projets/Projet_Sys"
        xlx.export_excel(path)
        
    def __data_form(self,dna,arn,protein):
        """
        @params Object,Object,Object
        Create dict of data dna
        @return dict
        """
        data={
            "sequances":{
                
                dna.title:dna.getSequance(),
                "Reverse Complement":dna.reverseComplement(),
                "RNA":arn.getSequance(),
                "Protein":protein.printProtein(),
                },

            "static":{

                "Rate CG%":{"CG":dna.tauxCG(),"AT":100-dna.tauxCG()},
                "Frequency Nucleotides":dna.FrequencyNucleotides(),
                "Frequency Codons":dna.FrequencyCodons()
                }
                
            }
        
        #if dna from fasta file send DNA consensus
        if (self.fasta is not None):
            data["sequances"].update({"DNA consensus":self.fasta.ADNconsensus()})
        
        return data


################################################################



class homeApp(App):
    def build(self):
        return homeWindow()


if __name__ == "__main__":
    homeApp().run()
