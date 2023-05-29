'''li=[1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
n=len(li)
for i in range (n):
    if li[i]
    '''
def find_pattern(lst):
    length = len(lst)
    
    for pattern_length in range(1, length // 2 + 1):
        num_patterns = length // pattern_length
        
        for i in range(pattern_length):
            pattern = lst[i:i+pattern_length]
            repeated = True
            
            for j in range(1, num_patterns):
                if lst[i+j*pattern_length:i+(j+1)*pattern_length] != pattern:
                    repeated = False
                    break
            
            if repeated:
                return pattern, num_patterns
    
    return None, 0

# Example usage:
input_string = input("Enter a string with list elements: ")
lst = eval(input_string)  

pattern, num_patterns = find_pattern(lst)

if pattern:
    print("Pattern Found:", pattern)
    print("Number of times pattern repeats:", num_patterns)
else:
    print("Pattern Not Found")
