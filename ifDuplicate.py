'''
Created on Feb 17, 2013

@author: Paradox
'''

#no with additional data structure using sort
def ifDuplicate2(s):
    if(len(s) <= 1):
        return False
    
    charArray = sorted(list(s))
    
    for i in range(len(s) - 1): # no need to check the very last one
        if(charArray[i] == charArray[i + 1]):
            return True
    
    return False
        

#with additional data structure
def ifDuplicate1 (s):
    if(len(s) <= 1):
        return False
    
    map = [0] * 256
    charArray = list(s)
    for char in charArray:
        map[ord(char)] += 1
    
    for charCount in map:
        if (charCount > 1):
            return True
    
    return False
       

def main():
    print "ifDuplicate check if a string has duplicate characters"
    test = "apple"
    test2 = "cuteboy"
    print ifDuplicate1(test)
    print ifDuplicate2(test)
    print ifDuplicate1(test2)
    print ifDuplicate2(test2)

if __name__ == '__main__': main()