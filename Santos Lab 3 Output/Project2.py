import random

class Student(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        return self.name
  
    def setScore(self, i, score):
        self.scores[i - 1] = score

    def getScore(self, i):
        return self.scores[i - 1]
   
    def getAverage(self):
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        return max(self.scores)
 
    def __str__(self):
        return "Name: " + self.name  + "\nScores: " + " ".join(map(str, self.scores))
    
    def __eq__(self, student):
        return self.name == student.name
    
    def __lt__(self, student):
        return self.name < student.name
    
    def __gt__(self, student):
        return self.name > student.name or self.name == student.name
    
def printList(students):
    for student in students:
        print(str(student))

def main():
    
    student1 = Student('Ken', 5)
    student2 = Student('Terry', 5)
    student3 = Student('Raymond', 5)
    student4 = Student('Aaron', 5)
    
    students = [student1, student2, student3, student4]
    
    print('Initial List: \n')
    printList(students)
    
    random.shuffle(students)
    print('\nShuffled List: \n')
    printList(students)
    
    list.sort(students)
    print('\nSorted List: \n')
    printList(students)

if __name__ == "__main__":
    main()
