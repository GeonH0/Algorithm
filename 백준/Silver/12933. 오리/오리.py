
cnt = 0
s = input().strip()
sound = "quack"
duck_states = []

for i in s:
    found = False
    for j in range(len(duck_states)):
        if sound[duck_states[j]] == i:
            duck_states[j] += 1
            if duck_states[j] == len(sound):
                duck_states[j] = 0
            found = True
            break
    if not found:
        if i == "q":            
            duck_states.append(1)
            cnt = max(cnt, len(duck_states))
        else:
            
            cnt = -1
            break

if any(state != 0 for state in duck_states):
    cnt = -1

print(cnt)