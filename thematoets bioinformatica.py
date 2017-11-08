# Ariel Komen
# BIN-1d
# 
def main():
    tekst = '/home/cole/Downloads/yeast_genes.csv'
    d2_lijst = read_file(tekst)
    geveriveerd, twijfelachtig, accesiecode_genen = not_validated(d2_lijst)
    
    ion = ion_involved(d2_lijst)
    
    print("-"*50)
    print("dit is het aantal geveriveerd: ", twijfelachtig)
    print("dit is het aantal ongeveriveerde genen: ", accesiecode_genen) 
    print("waarvan er", ion, "zoveel betrokken zijn bij ion processen")
    print("-"*50)
    
    for regel in geveriveerd:
        print("accesiecode: \t", regel)
        print("ion of niet:\t ik weet het niet, daar ben ik niet uitgekomen")
        print("-"*50)
    
def read_file(bestand):
# input: een tekstbestand
# output: een 2d lijst
    d2_lijst = []

    for regel in open(bestand):
        if regel.startswith("Y"):
            gene = regel.strip().split(",")
            d2_lijst.append(gene)
            
    return d2_lijst
    
def not_validated(lijst):
# input: een 2d lijst
# output: een lijst met accessiecodes van de niet gevalidadeerde genen
    #pass
    accesiecode_genen = []
    geveriveerd = 0
    twijfelachtig = 0

    

    for regel in lijst[0:]:
        if regel[1] == "Verified":
            geveriveerd += 1
        else:
            twijfelachtig += 1
            accesiecode_genen.append(regel[0])
    
    
    return accesiecode_genen, geveriveerd, twijfelachtig
    

def ion_involved(lijst):
# input: een 2d lijst of een sublijst van de 2d lijst, hangt er vanaf wat je wil
# output: een lijst met alle genen die betrokken zijn bij ion processen
    pass
    geveriveerd = 0
    twijfelachtig = 0
    non_geveriveerde_lijst = []

    for regel in lijst[0:]:
        if regel[1] == "Verified":
            geveriveerd += 1
        else:
            twijfelachtig += 1
            non_geveriveerde_lijst.append(regel)
    print(geveriveerd)
    print(twijfelachtig)
           
    print(twijfelachtig)
    
    ion = 0
    de_rest = 0
    ion_processen = []

    for regel in non_geveriveerde_lijst:
        for woord in regel:
            if woord == "ion":
                ion += 1
            else:
                de_rest += 1

    """
    for regel in non_geveriveerde_lijst:
        if regel[2] == "ion":
            continue
            ion_processen.append(regel[0])
            ion += 1
        else:
            de_rest += 1
    """         
        
    #print("dit zijn de keren dat hij ion vindt: ", ion)
    #print("dit zijn de biologische en metabolische processen: ", de_rest)

    return ion

main()
