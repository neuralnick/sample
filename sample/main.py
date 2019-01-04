import sys
import ast

_author_= 'efisher'

def flatten(x):
    flatlist = []
    for n in x:
        if isinstance(n,list):
            flatlist += flatten(n)
        else :
            flatlist.append(n)

    return flatlist

if __name__ == '__main__':

    print("Enter an array: ")
    for line in sys.stdin:
        try:
            result= flatten(ast.literal_eval(line))
            print("Result : ",result)
        except (ValueError, SyntaxError):
            print("Sorry - not a readable array (strings may need quotes).")
        print("Enter an array: ")


