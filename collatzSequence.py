def collatzSequence():
 print('input a number')
 num = int(input())
 while num != 1:
  if num % 2 == 0:
   num = num // 2
   print(num)
   continue
  elif num % 2 != 0:
   num = num * 3 + 1
   print(num)
   continue
 print(1)

collatzSequence()

