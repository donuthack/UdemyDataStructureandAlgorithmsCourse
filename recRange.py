def recRange(num):
   return 1 if num <= 1 else num + recRange(num - 1)

#print(recRange(6))
