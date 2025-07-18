# remove duplicates from string 

def removeDuplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result+=char
    
    return result

s = "programing"
print(removeDuplicates(s))