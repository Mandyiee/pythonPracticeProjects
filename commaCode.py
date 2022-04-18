def commaCode(array):
 stringlist = ''
 for i in range(len(array)):
  stringlist += array[i] + ','
 print(stringlist)

commaCode(['apples', 'bananas', 'tofu', 'cats'])
