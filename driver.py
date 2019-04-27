from svm import testSVM, runSVM

if __name__ == "__main__":

    # SVM Test on msgs dataset
    print("Running SVM on SMS dataset from UCI.")
    print("Accuracy: ")
    testSVM()
    
    # SVM test on custom inputted messagE
    message1 = "HEY HEY HEY YOU JUST WON $500000. WINNER WINNER. PLEASE REPLY AT 189274981724"
    message2 = "Hey What's up?  Want to grab a drink tonight at Polyesther on Sixth?"
 
    print("Accuracy of message1: ")
    runSVM(message1)
    print("Accuracy of message2: ")
    runSVM(message2)
