import sys
import random
import timeit

numIter=int(sys.argv[1])
sizeofSets=int(sys.argv[2])

arrA=[]
arrB=[]

print("Creating sets")
start=timeit.default_timer()
for i in range(numIter):
    a=set()
    b=set()

    for i in range(sizeofSets):
        num=random.randint(0,10 * sizeofSets)
        a.add(num)
        num=random.randint(0,10 * sizeofSets)
        b.add(num)
    
    arrA.append(a)
    arrB.append(b)
stop=timeit.default_timer()

print("Done. Took " + str(stop-start))
print("Starting trial")
start=timeit.default_timer()
for i in range(numIter):
    arrA[i]&=arrB[i]
stop=timeit.default_timer()

print(stop-start)