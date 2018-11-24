import time 

time.time() 

newtime = time.time() + 60*60
newdurt = 60
exttime = time.time() + 90*60
extdurt = 120 

if (newtime + 60*newdurt) > exttime:
    print("Reservation invalid!")
else:
    print("Reservation available!")



