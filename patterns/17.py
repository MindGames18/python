n=int(input("number of rows: "))
for i in range(n,0,-1):
   for j in range(n,0,-1):
     if j>=i:
       print(j,end='')
     else:
       print(i,end='')
   print()

'''
output-

55555
54444
54333
54322
54321
'''
