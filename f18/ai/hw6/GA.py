import random

def fitness(genome,key):
    seed = ("ztVvDguRAQDaSXXmLeJkUxRejhCGKfRjWDJCwowiSioIwtDqD"
            "HwelMnDfsXlhceWgMKXBUbsqlDVvXhpXXgtTjNmdBQfVsacmE"
            "vbHxQXodqKLaeFsrwlyMTkvziWPOAbgDjMXZRpUyrMVRmKhZo"
            "tMIQtZHuzkvrlpgYgYAjFgOHYhrDquFTKxfargRnZDtISDpvE"
            "ZqQJgLmRlyJrnqMiampUBMlcyyLqKJypCAiKhFIxuYlZkiYeO"
            "tVQCktDJAvgjiickEOvISfiaJqHUjOfuaRpdGFysIgoyXnVbj"
            "IVfDQhpgtVDIvHRmRnApMTDFQIPFWLNMkCWoMPgvNCpAFFDIE"
            "zxIWAodRAOrErfuTzdbRjMroKhomBBEzvraoKpAMeQXlzantp"
            "vUhWPNNCodmpJaThVTFYevCCwVahUpUncRDKpWhoogIUcpBcS"
            "SudgHrsIjQAcNjWFjOITSBWeASqotPMBIjzomMsdWEnyIkrfP"
            "gnbnYXgrwfZlNfYyAvBsUxQgVoLnHkWtXaKrGiDjEbJeMcOqT"
            "pCzFuSmRhIwPd"
            )
    s = 0
    for x in range(len(genome)):
        s+=(ord(seed[x+key])-ord(seed[key])-1)*(int(genome[x]))+30
    return s

def gaInputs():
    total = 0
    population = int(input("How many chromosomes are there per generation? "))
    while total != population:
        print(("Selection, Mutation, Newblood, and Crossover will have to"
               "equal population..."))
        selection = int(input("How many of these will undergo selection? "))
        mutation = int(input("How many of these will undergo mutation? "))
        newblood = int(input("How many new chromosomes will be added (new blood)? "))
        crossover = 2 * int(input("How many PAIRS of crossover will occur? "))
        total = selection + mutation + newblood + crossover
    print("Thank you, those values match")
    generations = int(input("How many generations? "))
    key = int(input("What is the key to the fitness function (1-500)? "))
    check = False
    while key < 1 or key > 500:
        key = input(("Incorrect key value. What is the key to the fitness "
                    "function? (1-500)? "))
    gaParameters(population, selection, mutation, newblood, crossover, generations, key)

def gaParameters(population, selection, mutation, newblood, crossover, generations, key):
    genomes = genPopulation(population)
    bestGenome = ""
    bestScore = -100
    bestOverall = ""
    bestOverallScore = -100
    #first gen
    for genome in genomes:
        score = fitness(genome,key)
        if score > bestOverallScore:
            bestOverall = genome
            bestOverallScore = score
    lastGen = genomes
    bestGen = 1
    print("Best in generation 1 is {} with a score of {}"\
          .format(bestOverall,bestOverallScore))
    #rest of gens 
    for i in range(1,generations):
        newGen = []
        newGen.extend(genSelections(lastGen,selection,key))
        newGen.extend(genMutations(lastGen,mutation))
        newGen.extend(genNew(lastGen,newblood,key))
        newGen.extend(genCross(lastGen,crossover,key))
        bestGenome = ""
        bestScore = -100
        for genome in newGen:
            score = fitness(genome,key)
            if score > bestScore:
                bestGenome = genome
                bestScore = score
        if bestScore > bestOverallScore:
            bestOverallScore = bestScore
            bestOverall = bestGenome
            bestGen = i+1
        print("Best in generation {} is {} with a score of {}"\
              .format(str(i+1),bestGenome,bestScore))
        lastGen = newGen
    print("Best seen was: {}\nwith score of {}\nfrom generation {}"\
          .format(bestOverall,bestOverallScore,bestGen))

#Generate New Blood
def genNew(lastGen,size,key):
    newPart = []
    for i in range(0,size):
        newPart.append(tournamentSelect(lastGen,key))
    return newPart

#Tournament Selection Method
def tournamentSelect(generation,key):
    selected = ""
    rand1 = random.randint(0,len(generation)-1)
    rand2 = random.randint(0,len(generation)-1)
    score1 = fitness(generation[rand1],key)
    score2 = fitness(generation[rand2],key)
    if score1 > score2:
        return generation[rand1]
    else:
        return generation[rand2]

#Generate Selections
def genSelections(lastGen,size,key):
    newPart = []
    for i in range(0,size):
        newPart.append(tournamentSelect(lastGen,key))
    return newPart

#Generate Mutations
def genMutations(lastGen,size):
    newPart = []
    for i in range(0,size):
        randGen = random.randint(0,len(lastGen)-1)
        selectedGenome = list(lastGen[randGen])
        randBit = random.randint(0,len(selectedGenome)-1)
        if int(selectedGenome[randBit]) == 1:
            selectedGenome[randBit] = 0
        else:
            selectedGenome[randBit] = 1
        newStr = ""
        for bit in selectedGenome:
            newStr += str(bit)
        newPart.append(newStr)
    return newPart

#Generate Crossovers
def genCross(lastGen,size,key):
    newPart = []
    for i in range(0,size):
        randSplit = random.randint(0,len(lastGen)-1)
        genome1 = tournamentSelect(lastGen,key)
        genome2 = tournamentSelect(lastGen,key)
        newPart.append(genome1[:randSplit] + genome2[randSplit:])
        newPart.append(genome2[:randSplit] + genome1[randSplit:])
        
    return newPart

#Generate Population
def genPopulation(size):
    genomes = []
    for i in range(0,size):
        genomes.append(genChromosome())
    return genomes
        
#Randomly Generates a Single Chromosome
def genChromosome():
    bitStr = ""
    for i in range(0,24):
        bitStr += str(random.randint(0,1))
    return bitStr

