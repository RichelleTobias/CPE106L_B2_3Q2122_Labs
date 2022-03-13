"""
File name: LR2_2.py

Write a program that allows the user to navigate the lines of text in a file. 
The program should prompt the user for a filename and input the lines of text into a list. 
The program then enters a loop in which it prints the number of lines in the file and prompts the user for a line number. 
Actual line numbers range from 1 to the number of lines in the file. If the input is 0, the program quits. 
Otherwise, the program prints the line associated with that number. 
"""
#Prompt the user to enter the input file name
inputFile = input("Enter the input file name: ")

#Open the file 
fileOpen = open(inputFile, "r")

#Create Empty List
fileList = list()

#Loop read the content of input file line by line and
#store each line into variable 'line' till end of input file for line in fileOpen:
for line in fileOpen:
    #Strip new line
    line = line.strip('\n')
    #Add line read from file into list
    fileList.append(line)

cont = True
while cont:
    #Print total number of lines in file
    print('The file has', len(fileList), 'lines.')
    #Prompt and read line number
    lineNumber = int(input('Enter a line number [Enter 0 to quit]'))
    if lineNumber == 0:
        cont = False
    else:
        #Print the line
        print(str(lineNumber)+ ':' + fileList[lineNumber-1]+ '\n')

fileOpen.close()




