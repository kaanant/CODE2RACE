from collections import Counter

nInputs = int(input(''))
for n in range(nInputs):
    N = int(input(''))
    arr = list(input('').split())
    count = Counter(arr)
    freq = 0
    for i in range(N):
        if int(arr[i])%2==0:
            freq+=count[arr[i]]
    print(freq)
