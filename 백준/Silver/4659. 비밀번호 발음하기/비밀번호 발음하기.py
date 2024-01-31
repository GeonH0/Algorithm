


arr = {"a","e","i","o","u"}



while True:

    n = input().rstrip()

    ans = list(n)
    v_flag = 0 # 모음 존재
    v_cnt = 0 
    c_cnt =0
    err =0

    if n == "end":
        break

    for i in range(len(ans)):
        if i>0:
            if ans[i] == ans[i-1]:
                if ans[i] != "e" and ans[i] != "o":
                    err = 1
                    break
        if ans[i] in arr:
            v_flag =1
            v_cnt +=1
            c_cnt =0
            if v_cnt ==3:
                err =1 
                break
        else:
            v_cnt =0
            c_cnt +=1
            if c_cnt == 3:
                err =1
                break

    if (err != 1) and (v_flag ==1):
        print("<"+ n +"> is acceptable.")
    else:
        print("<"+ n +"> is not acceptable.")
		
