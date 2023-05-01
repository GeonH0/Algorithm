def solution(name, yearning, photo):
    cnt =0
    answer = []
    for i in photo:
        for j in range(len(i)):
            for k in name:
                if i[j]==k:
                    cnt +=yearning[name.index(k)]
        answer.append(cnt)
        cnt =0
        
        
        
    
    return answer