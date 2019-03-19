import numpy as np
def sum_array(array):
    
    '''Returns a sum of all items in an array'''
    
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])
        '''
    nparray = np.array(array) #convert array to a numPy array
    return nparray.sum() #return a sum of all array items
'''

def fibonacci(n):
    
    '''Returns the nth term in a fibonacci sequence
    
        Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    '''
    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    

def factorial(n):
    
    '''Returns n!
       
       Args:
           n (int): calculates n times previous terms
           
       Returns:
           int : n nth term multiplied by the product of
           the previous terms
           
       Examples:
           >> factorial(1)
           1
           >> factorial(3)
           6
           >> factorial(5)
           120
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def reverse(wordList):
    
    '''Returns the word in reverse'''
    
    #wordList = list(word) # convert word to a list
    wordList = wordList[-1::-1] # reverse the list
    result = ''.join(wordList) # join the reversed letters to for a word
        
    return result
    
print(reverse(['this is a longer sentence that you will need to reverse']))
