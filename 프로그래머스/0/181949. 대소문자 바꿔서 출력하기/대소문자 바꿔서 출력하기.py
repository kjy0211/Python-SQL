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