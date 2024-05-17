def concatFirstLastDigit(text: str) -> int:
    answer = ''
    for x in text:
        if(x.isnumeric()):
            answer+=x
            break
    for x in text[::-1]:
        if(x.isnumeric()):
            answer+=x
            break
    return int(answer)

    return 0

def preprocess(text: str) -> str:
    thisdict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for x, y in thisdict.items():
        text = text.replace(x,x+y+x)

    return text


def main():
    f = open("input.txt", "r")
    sum = 0
    for line in f:
        sum+=concatFirstLastDigit(preprocess(line))
    print(sum)

    


if __name__ == "__main__":
    main()
