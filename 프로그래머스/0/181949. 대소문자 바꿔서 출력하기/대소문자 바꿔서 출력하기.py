str = input()

result = ''

for i in str:
    if i.isupper():
        result += i.lower()
    elif i.lower():
        result += i.upper()
    else:
        result += i
        
print(result)



# print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
