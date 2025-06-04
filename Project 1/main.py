


def filledList():
    with open('todolist.txt', 'r') as file:
        returnedlist = [line.strip() for line in file]
    return returnedlist


def newTxt(changedList):
    with open('todolist.txt', 'w') as file:
            for i, item in enumerate(changedList, 1):
                file.write(str(i) + ". " + item + "\n")
                 
def main():
    todolist = filledList()
    while True:
        commandInput = input("Pick a command (v, a, d, x): ")
        if commandInput == "v":
            print(todolist)

        if commandInput == "a":
            addedTask = input('Enter the task you want to add: ')
            print(todolist)
            numTask = int(input('Where in the list do you want to add?'))
            todolist.insert(numTask, addedTask)
            newTxt(todolist)

        if commandInput == "d":
            print(todolist)
            numTask = int(input("What task would you like to delete?: "))
            todolist.pop(numTask)
            newTxt(todolist)
        if commandInput == "x":
            break

if __name__ == "__main__":
    main()