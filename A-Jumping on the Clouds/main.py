n = int(input())

clouds = input()
clouds = clouds.strip().split()

i=0
jmp = 0
while i < n:
    if i+2 < n and clouds[i+2] == "0":
        i = i+2
        jmp = jmp +1
        continue
    if i+1 < n and clouds[i+1] == "0":
        i = i+1
        jmp = jmp + 1
    else:
        break
    
print(jmp)