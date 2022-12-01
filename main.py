numbers = ["0", "4", "2", "1", "6", "5", "3", "8", "7"]
x = 0 

#main loop
while True:
    #gettin gindex of 0 = empty field
    zero = numbers.index("0")
    print(" ")

    #printing initial list
    for nums in numbers:
        print(numbers[x])
        x += 1
    x = 0

    #user input for swap
    user_input = input()

    def move(user_input):
        x = 0
        if user_input != "0":
            index = numbers.index(user_input)

        #left column
        if index == 0:
            plus3(index)
            minus3(index)
            plus1(index)
        elif index == 3:
            plus3(index)
            minus3(index)
            plus1(index)
        elif index == 6:
            plus3(index)
            minus3(index)
            plus1(index)

        #center column
        if index == 2:
            plus3(index)
            minus3(index)
            plus1(index)
        elif index == 4:
            plus3(index)
            minus3(index)
            plus1(index)
        elif index == 7:
            plus3(index)
            minus3(index)
            plus1(index)    

        #right column
        if index == 2:
            plus3(index)
            minus3(index)
            minus1(index)
        elif index == 5:
            plus3(index)
            minus3(index)
            minus1(index)
        elif index == 8:
            plus3(index)
            minus3(index)
            minus1(index)        

    def plus3(index):
        x = 0
        if index == zero + 3:
            numbers[zero], numbers[index] = numbers[index], numbers[zero]
            print(" ")
            for nums in range(9):
                print(numbers[nums])
                x += 1

    def minus3(index):
        x = 0
        if index == zero - 3:
            numbers[zero], numbers[index] = numbers[index], numbers[zero]
            print(" ")
            for nums in range(9):
                print(numbers[nums])
                x += 1

    def plus1(index):
        x = 0
        if index == zero + 1:
            numbers[zero], numbers[index] = numbers[index], numbers[zero]
            print(" ")
            for nums in range(9):
                print(numbers[nums])
                x += 1

    def minus1(index):
        x = 0
        if index == zero - 1:
            numbers[zero], numbers[index] = numbers[index], numbers[zero]
            print(" ")
            for nums in range(9):
                print(numbers[nums])
                x += 1

    move(user_input)

    if numbers == ["4", "2", "3", "0", "5", "6", "7", "8", "1"]:
        print("You won!")
        break
