"""
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the secon number: "))
for i in range(firstNumber,secondNumber+1):
    if(i%2==0):
        print(i)
"""
'''
MyFile=open('kttekst.txt','r')
words={}
for word in file.read(
'''


def main():
    with open(r'C:\Users\opilane\AppData\Local\Programs\Python\Python37\pythonkt2\kttekst.txt') as f:
        words = [word for line in f for word in line.split()]
        print ("The total word count is:", len(words))
main()
#        words1 = [word for word in f for word in len(words) <=4]
#       print ("The total word count for words with less than 5 letters is: ", len(words1))



