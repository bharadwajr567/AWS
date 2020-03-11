"""def solution1(a, i, j):
    if not len(a):
        raise ValueError('Array is empty...')   
    first_part = a[:i]
    last_part = a[j+1:]
    
    middle_part = a[i:j+1]
    result = []
    
    for n in middle_part:
        
        result = [n] + result
        
    return first_part + result + last_part


a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print  ("Actual result of is:" , a)
print("expected result is:", (solution1(a, 2, 5)))


def holidaybush(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '*' * x + ' ' * z)
        x+=2
        z-=1
holidaybush(5)

def Sentence(s):
    '''input: str
    rtype:str'''
    words = s.split(" ") #
    print(words)
    newWords = [word[::-1] for word in words] 
    print(newWords)
    newSentence = " ".join(newWords) 
    return newSentence[::-1] 
    for i in range(ln): 
        if str[i] >= 'a' and str[i] <= 'z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) - 32) 
  
        elif str[i] >= 'A' and str[i] <= 'Z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) + 32) 
# Driver's Code  
S = "BhAradwaj iS a GOod bOy"
print(Sentence(S)) 
#eBoY good is a BhARadwAj

def convertOpposite(str): 
    ln = len(str) 
  
    # Conversion according to ASCII values 
    for i in range(ln): 
        if str[i] >= 'a' and str[i] <= 'z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) - 32) 
  
        elif str[i] >= 'A' and str[i] <= 'Z': 
  
            # Convert lowercase to uppercase 
            str[i] = chr(ord(str[i]) + 32) 
  
# Driver code 
if __name__ == "__main__": 
    str = "BhAradwaj iS a GOod bOy"
    str = list(str[::-1]) 
  
    # Calling the Function 
    #print(convertOpposite(''.join(str)))
  
    str = ''.join(str)
    print(str)
   
def changeCase(word):
    newword = ""                     # Create a blank string
    for i in range(0, len(word)):
        character = word[i]          # For each letter in a word, make as individual viarable
        if character.islower()== False: # Check if a letter in a string is already in upper case
            character = character.lower()  # Make a letter lower case
            newword += character           # Add a modified letter in a new string
        else:
            character = character.upper()  # Make a letter upper case
            newword += character           # Add a modified letter in a new string

    return newword                         # Return a new string

if __name__ == "__main__":
    w = 'bharadwaj'
    w = list(w[::-1])
    print(changeCase(w))


def num_ways(s,memo):
    if s.startswith('0'):
        return 0
    elif len(s)<=1:
        return 1
    if memo[len(s)] != None:
        return memo[len(s)]
    result = num_ways(s[1:],memo)
    if int(s[:2]) <= 26:
        result += num_ways(s[2:],memo)
    memo[len(s)]=result
    return result
num_ways(s,[None]*(len(s)+1))

def fibonacci_recursion(num):
    '''Return a fibonacci sequence value of num'''
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1

    return fibonacci_recursion(num - 2) + fibonacci_recursion(num - 1)
  
# Driver Program 
  
print(fibonacci_recursion(9))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board) 
        rows = {i: [] for i in range(n)}
        cols = {i: [] for i in range(n)}
        box = {i: [] for i in range(n)}
        
        
        
        for i in range(n):
            for j in range(n):
                
                if board[i][j] == ".": continue
                
                num = board[i][j]
                
                box_index = (i // 3) * 3 + j // 3
                
                if num in rows[i] or num in cols[j] or num in box[box_index]:
                    return False
                
                rows[i].append(num)
                cols[j].append(num)
                box[box_index].append(num)
       
    
        return True

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(7))

class C:
    count = 0
    def __init__(self,a):
        self.count+=1
        #print (a)
        self.a = a
        #print (a)
ins = [C(i) for i in range(10)]
print(C.count)

x , y = '12'
y, z = '34'

print("Value of x,y:", x, y)
print("Value of y,z:", y, z)
print(x + y +z)



def kWay( A, k, overlap ) :
    
    #A = list of meeting IDs, k = number of rooms, 
    #overlap[ meeting ID m ] = set of meetings overlapping with m 
    
    if k == 1 : # only 1 room: all meetings go there
        yield [ A[:] ]
    elif k == len(A) : # n rooms and n meetings: put 1 meeting per room
        yield [ [a] for a in A ]
    else :
        for partition in kWay( A[1:], k, overlap ) : # add new meeting to one existing room
            for i, ci in enumerate( partition ) :
                isCompatible = all( A[0] not in overlap[x] for x in ci ) # avoid 2 overlapping meetings in the same room
                res = partition[:i] + [ ci + [ A[0] ] ] + partition[ i+1: ]
                if isCompatible :
                    yield res
        for partition in kWay( A[1:], k-1, overlap ) : # add new meeting to a new room
            isValid = ( set(A[1:]) & set.union( * ( overlap[a] for a in A[ 1: ] ) ) == set() ) # avoid 2 overlapping meetings in the same room
            if (k-1>1) or ( k-1==1 and isValid ) :
                yield partition + [ [ A[0] ] ]
#The above example is a bit tricky l
# lets take an example and try to understand the problem in detail 

import collections
from collections import defaultdict

n = 5
k = 2
#
A = range(n)
# prepare overlap dictionary
pairs = [ (0,1), (1,2), (2,3), (3,4) ] # overlapping meetings
size = dict( ( (0,10), (1,8), (2,6) , (3,10), (4,8) ) )

overlap = collections.defaultdict(set)
for (i,j) in pairs :
    overlap[i].add(j)
    overlap[j].add(i)

defaultdict(set, {0: set([1]), 1: set([0, 2]), 2: set([1, 3]), 3: set([2, 4]), 4: set([3])}
for partition in kWay( A, k, overlap ) :
    print (partition, [ max( size[x] for x in c ) for c in partition ])
[[3, 1], [4, 2, 0]] [10, 10]

#Example 2: 

import collections

n = 6
k = 3
#
A = range(n)
pairs = [ (0,1), (1,2), (2,3), (3,4), (5,2), (5,3) ] # overlapping meetings
size = dict( ( (0,10), (1,8), (2,6) , (3,10), (4,8), (5,2) ) )

overlap = collections.defaultdict(set)
for (i,j) in pairs :
    overlap[i].add(j)
    overlap[j].add(i)

collections.defaultdict(set, {0: set([1]), 1: set([0, 2]), 2: set([1, 3, 5]), 3: set([2, 4, 5]), 4: set([3]), 5: set([2, 3])})
{0: 10, 1: 8, 2: 6, 3: 10, 4: 8, 5: 2}
for partition in kWay( A, k, overlap ) :
    print (partition, [ max( size[x] for x in c ) for c in partition ])
[[3, 1], [4, 2, 0], [5]] [10, 10, 2]
[[3, 1], [4, 2], [5, 0]] [10, 8, 10]
[[3, 0], [4, 2], [5, 1]] [10, 8, 8]
[[3], [4, 2, 0], [5, 1]] [10, 10, 8]
[[4, 5, 1], [3, 0], [2]] [8, 10, 6]
[[4, 5, 1], [3], [2, 0]] [8, 10, 10]
[[4, 5, 0], [3, 1], [2]] [10, 10, 6]
[[4, 5], [3, 1], [2, 0]] [8, 10, 10]
min( sum( [ max( size[x] for x in c ) for c in partition ] ) for partition in kWay( A, k, overlap ))

class Solution(object):
    def productExceptSelf(self, nums):
    
        #:type nums: List[int]
        #:rtype: List[int]
    
        size = len(nums)
        output = [1] * size
        left = 1
        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left
        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output

n = int(input("Enter a number: "))
target = int(input("Enter a target variable: ")) 
def count_zeros(n,target):
    return str(target).count('0')"""

def anagram_difference(w1, w2):
    return helper(w1, w2) + helper(w2, w1)


def helper(a, b):
    num = 0
    visited = []
    for l in a:
        if l not in b:
            num += 1
        else:
            if l not in visited:
                if a.count(l) > b.count(l):
                    num += a.count(l) - b.count(l)
                    visited.append(l)
    return num


# example
print(anagram_difference('codewars', 'hackerrank'))
print(anagram_difference('ab', 'ba'))
print(anagram_difference('pwslhderflpybdjhdwxtyeigbeppnun', 'nwpqwickfpgnazzuqkmrlyrrdizvoxxgniazqvv'))