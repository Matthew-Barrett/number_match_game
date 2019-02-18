

bingo_match = [7,26,40,58,73,14,22,34,55,68]


print ("Welcome to Bingo!")
while True:
    x = int(input("pick a number:"))
    if x in bingo_match:
        print("correct!")
        bingo_match.remove(x)
    elif x < 1:
        print("pick a bigger number:")
    elif x > 80:
        print("pick a smaller number:")
    else:
        print("incorrect!")
    if len(bingo_match) == 0:
        print ("you win!")
        break




