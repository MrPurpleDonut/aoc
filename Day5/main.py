import farmMap

def preprocess(fileContents: list)->tuple[list, list]:
    formated = []
    for line in fileContents:
        formated.append(line.replace("\n", ""))
    mapList = []

    formated.append("")
    seeds = [int(x) for x in formated[0].split(":")[1].split()]

    
    gather = []
    for i in range(2, len(formated)):
        if formated[i] == "":
            mapList.append(gather)
            gather = []
        elif formated[i].endswith(":"):
            pass
        else:
            gather.append([int(x) for x in formated[i].split()])

    returnList = [farmMap.farmMap(x) for x in mapList]

    return seeds, returnList


def main():
    f = open("input.txt", "r")
    seeds, maps = preprocess(f.readlines())
    seedResult = []
    for seed in seeds:
        for seedMap in maps:
            seed = seedMap.transform(seed)
        seedResult.append(seed)
    print(min(seedResult))

    seedTuples= []
    for i in range(len(seeds)):
        if i % 2 == 0:
            seedTuples.append([seeds[i], seeds[i+1]])


    seedResult2 = []
    for seedRange in seedTuples:
       internalTransform = [seedRange]
       temp = []
       for seedMap in maps:
            for i in range(len(internalTransform)):
                temp.extend(seedMap.processRanges(internalTransform[i]))
            internalTransform = temp
            temp = []
       seedResult2.extend([x[0] for x in internalTransform])
       
    print(min(seedResult2))



if __name__ == "__main__":
    main()