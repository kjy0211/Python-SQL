def solution(a, b):
    comb = int(f'{a}{b}')
    multi = 2 * a * b
    
    return (max(comb, multi))
    