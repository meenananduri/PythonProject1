savedSeats = []
def main() :
    
    #get filename
    filename = input("Enter file name, if not, default file will be used: ")
    if filename == "" :
        filename = "lab5input.txt"    
    
    seatingChart = readChart(filename)
    buySeat(seatingChart)
    saveChart(filename, seatingChart)
    printChart(seatingChart, filename)
    
def readChart(filename) :
    seatingChart = [] # a list of lists
    
    with open(filename) as infile :
        for line in infile :
            aline = line.split()
            seatingChart.append(aline) 
    
    return seatingChart
            
def buySeat(seatingChart) :
    numberSeats = int(input("Enter in the number of seats you want to buy: "))
    #for each seat that user buys, check if available
    price = 0 #total price of seats that user wants to buy
    i = 1
    while i <= numberSeats :
        location = input("Enter row,col of seat " + str(i) + ":")
        comma = location.index(",")
        row = int(location[0 : comma])
        col = int(location[comma + 1 :])
        #check if its available
        if seatingChart[row][col] != 'X' : #if available
            #calculate price
            price += int(seatingChart[row - 1][col - 1])
            seatingChart[row][col] = 'X'
            savedSeats.append((row, col))
            i += 1
        else :
            print("That seat is not available")
    print("Total price: $" + str(price))
        


def saveChart(filename, seatingChart) :
    
    with open(filename, "w") as infile :
        row = len(seatingChart) - 1
        col = len(seatingChart[0]) - 1
        for i in range(row) :
            if i != 0 :
                infile.write("\n")        
            for j in range(col) :
                if seatingChart[i - 1][j - 1] == 'X' :
                    infile.write('- ')
                else :
                    infile.write(seatingChart[i - 1][j - 1] + " ")  
                    
def printChart(seatingChart, filename) :
    
    file = readChart(filename)
    
    row = len(seatingChart) - 1
    col = len(seatingChart[0]) - 1   
    
    for i in range(row + 1) :
        if i != 0 :
            print()
        for j in range(col + 1) :
            #if seatingChart[i][j] == '-', and not in savedSeats, then print as '-'
            if file[i - 1][j - 1] == '- ' and (i - 1, j - 1) not in savedSeats :
                print('-' + " ", end = "")
            elif (seatingChart[i - 1][j - 1]).isdigit() :
                print("$" + seatingChart[i - 1][j - 1] + " ", end = "")
            else : #prints the X's
                print(seatingChart[i - 1][j - 1] + "   ", end = "")        
        

main()
            
    
        
        

        