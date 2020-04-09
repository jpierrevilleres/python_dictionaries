alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic","subdermatoglyphics"]
test_miss = ["zzz","subdermatoglyphic","the quick brown fox jumps over the lazy dog"]

def histogram(s):   #source code copied from Section 11.2 of Think Python
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
#Part1
def has_duplicates(s):  #function that checks if the string has repeatead characters.
    for a in histogram(s).values(): #calls the histogram function and checks respective values
        if len(set(s)) < len(s) > 1: 
            return True #returns boolean output True
        else:
            return False #returns boolean output False

def checker_test_dups(): #function using for loop that checks test_dups list for duplicates.
    for s in test_dups:
        if has_duplicates(s) == True: #calls has_duplicate function and check if return value is True
            print(s + " has duplicates")
        else:
            print(s + " has no duplicates")

#Part2
def missing_letters(s): #takes string argument and checks all the alphabets not in the string
    glbl_alph = list(alphabet) #calls the global variable alphabet and makes a list out of it
    for c in histogram(s): #for loop that checks if the alphabet letters are in the string
        if c in glbl_alph:
            glbl_alph.remove(c)  #removes the letter if found in the string
    return ''.join(glbl_alph) #joins the missing letters in one string
    
def checker_test_miss():  #function using for loop that checks test_miss list for missing letters.
    for s in test_miss:
        if missing_letters(s) == '': #calls missing_letters function to check if letters were used for the string or not.
            print(s + " uses all the letters")
        else:
            print(s + " is missing letters", missing_letters(s))

checker_test_dups()
checker_test_miss()
