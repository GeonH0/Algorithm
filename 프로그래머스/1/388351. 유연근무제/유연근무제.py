def solution(schedules, timelogs, startday):
    answer = 0
    T = len(timelogs)
    
    
    nocnt = []
    for j in range(T):
        if schedules[j] % 100 >= 50:
            schedules[j] = (schedules[j] //100 + 1) * 100 + (schedules[j] % 100 + 10) - 60
        else:
            schedules[j] += 10
    
    
    for i in range(7):
        if (i + startday) % 7 == 0 or (i + startday) % 7 == 6: # 토,일은 넘어감
            continue
        else:
            for j in range(T):
                if j in nocnt:                    
                    continue
                elif timelogs[j][i] <= schedules[j]:
                    continue
                else:                    
                    nocnt.append(j)
    
    
    answer =  T - len(nocnt)
                    
                            
                
            
    return answer