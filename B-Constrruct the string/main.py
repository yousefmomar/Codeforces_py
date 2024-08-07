tests=int(input())

arr_str=[]

for i in range (0,tests):
    arr_in=list(map(int, input().strip().split()))
    c=['a']
    
    for j in range(1,arr_in[2]):
        c.append(chr(ord(c[j-1])+1))

    jj=0
    str1=" "
    for j in range(arr_in[0]):
        str1+=c[jj]
        jj+=1
        if jj==arr_in[2]:
            jj=0

    arr_str.append(str1.strip())

for str2 in arr_str:
    print(str2)