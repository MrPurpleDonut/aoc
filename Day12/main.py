from functools import cache

def preprocess(line: str)->list:
    contents = line.split()
    returnList = []
    returnList.append(contents[0])
    gaps = tuple(int(x) for x in contents[1].split(","))
    returnList.append(gaps)
    return returnList

@cache
def countWays(config: str, nums: tuple)->int:
    if config == "": 
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if "#" in config else 1

    count = 0

    if config[0] in ".?":
        count += countWays(config[1:], nums)

    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            count += countWays(config[nums[0]+1:], nums[1:])
        
    return count

    

def main():
    with open("input.txt", "r") as f:
        fileContents = [preprocess(line) for line in f]
    
    totalWays = 0
    for row in fileContents:
        totalWays+=countWays( (row[0]+"?")*4+row[0], row[1]*5)

    print(totalWays)




if __name__ == "__main__":
    main()