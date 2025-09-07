def solution(n, m, section):
    answer = 0
    paint_until = 0
    
    for s in section:
        if s > paint_until:
            answer +=1
            paint_until = s + m-1
    return answer