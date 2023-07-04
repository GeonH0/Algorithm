
def solution(number):
    
    
    
    answer =[]
    for i in range(0,len(number)):
        for j in range(1,len(number)):
            if i == j :
                continue
            answer.append(number[i]+number[j])
            
    answer = list(set(answer))
    answer.sort()
            
            
    
        
    
    
    return answer