# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

str_in = []

def camel(i):
    name = i.split(';')
    
    if name[0] == 'C':
        name[2] = name[2].title()
        name[2] = name[2].replace(' ', '')
        
        if name[1] == 'V' or name[1] == 'M':
            name[2] = name[2][0].lower() + name[2][1:]
        if name[1] == 'M':
            name[2] += '()'
    
    elif name[0] == 'S':
        if name[1] == 'M':
            name[2] = name[2].replace('()', '')
            
        for i in range(len(name[2])):
            if name[2][i].isupper() and name[2][i-1].isalpha():
                name[2] = name[2][:i] + ' ' + name[2][i:]
        
        if name[1] == 'C':
            name[2] = name[2][1:]
                
        name[2] = name[2].lower()
        
    print(name[2])

s = 'a'
try:
    while s != '':
        s = input().strip()
        str_in.append(s)
except EOFError:
    pass    
for i in str_in:
    camel(i)
