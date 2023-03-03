def solution(number):
    
    if number < 0:
        return 0
    else:
        multiples = set()
        for i in range(3, number):
            if i % 3 == 0 or i % 5 == 0:
                multiples.add(i)
        return sum(multiples)
    