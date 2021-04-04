##
# Tic Tac Toe
##

def createField():
    for row in range(5):
        if(row%2==0):
            for column in range(5):
                if(column%2==0):
                    if column != 4:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
            print("-----")

Player =1
currentField= [[" "," "," "],[" "," "," "],[" "," "," "]]

while(True):
    print("Players turn: ", Player)
    SelectRow = int(input("Please enter the row\n"))
    SelectColumn = int(input("Please enter the column\n"))

    if Player ==1:
        if currentField[SelectRow][SelectColumn] == " ":
            currentField[SelectRow][SelectColumn] = "X"
            Player =2
    else:
        if currentField[SelectRow][SelectColumn] == " ":
            currentField[SelectRow][SelectColumn] = "O"
            Player =1

    print(currentField)
