# On the try and except block: You run some codes/statements and if it is successful the try block will get executed other than the except block will there is an anticipated error


try:
    number = 100

    answer = number / 10

    print("The answer is :  ", answer)
except Exception as e:
    print("There is an error: ", e)