# from model import adn as a
from vendor import fasta as fa
fa=fa.fasta("file.fa")
print(fa.getFileAsSequences())
print(fa.ADNProfile())
print(fa.ADNconsensus())
# print(fa.ADNconsensus())
# adn = a.adn("actg")
# fi=fasta.getFileAsSequences()
# print (adn.generate(20))
# arn =adn.TranscribeARN()
# print(adn.findMotifADN("AT"))
# # print (adn.FrequencyNucleotides())
# Prot=arn.TranscribeProtein()
# print(Prot.getProtein())
# print(Prot.printProtein())

# print(adn.reverseComplement())
# print(adn.tauxCG())
# print(adn.FrequencyCodons())
# print(adn.mutations(3).getSequance())
