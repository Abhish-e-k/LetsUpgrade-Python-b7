#armstrong no. between 1042000 to 702648265

for num in range(1042000,702648265):
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**3
      temp=temp//10
      if sum==num:
           print (num)