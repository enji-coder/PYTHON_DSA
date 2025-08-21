result = list(range(1,250000)) # list works slow in big data 

print(120000 in result)  # slow executation 

hash_result = set(result)
print(120000 in hash_result) # fast executation 