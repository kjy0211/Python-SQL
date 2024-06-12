def solution(n):
    if n % 2 == 1:
        result = sum(i for i in range(1, n+1, 2))
        return(result)
    else:
        result = sum(i**2 for i in range(2, n+2, 2))
        return(result)
    
    