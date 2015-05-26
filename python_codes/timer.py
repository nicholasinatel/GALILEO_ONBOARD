import time

s=0
m=0
while s<=60:
     print m, 'Minutes', s, 'Seconds'
     time.sleep(1) #program stops for 1 second
     s+=1
     if s == 60:
          m+=1
          s=0
     elif m == 60:
         m=0
         s=0