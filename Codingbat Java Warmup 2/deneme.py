a= [1,2,3,4,5,6,6]
if len(a) < 3:
    count = 0
elif len(a) > 2:
    count = 0
    for x in range(len(a)-1):
        if a[x] == 6 and (a[x+1] == 6 or a[x+1] == 7):
            count += 1
print(count)