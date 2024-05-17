small = [[71530], [940200]]
large = [[58996469],[478223210191071]]


def main(thing):
    product = 1
    for i in range(len(thing[0])):
        count = 0
        for j in range(thing[0][i]):
            if j*(thing[0][i]-j) > thing[1][i]:
                count +=1
        product*= count
    print(product)
            

    

if __name__ == "__main__":
    main(large)