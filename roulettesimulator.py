##red strategy
##10 seconds per spin
##5million total spins
##doubling strategy
import random
totalsum = 0
wincounter = 0
losscounter = 0
number = 0
doubler = 0.01
averagesum=0
totaltime=0
fivemilsum=0
time=0
for x in range(10):
    liquidity=100000
    for x in range(100):
        time=time+wincounter+losscounter
        wincounter = 0
        losscounter = 0
        for x in range(5000):
            number=random.randint(0,36)
            if number%2==1:
                wincounter=wincounter+1
                totalsum = totalsum+doubler
                liquidity = liquidity+doubler
                doubler=0.01
            else:
                losscounter=losscounter+1
                totalsum = totalsum-doubler
                liquidity = liquidity - doubler
                doubler=(doubler*2)
            if liquidity<0:
                break
        if liquidity<0:
            break
    fivemilsum=fivemilsum+totalsum

    print("Wins:", wincounter)
    print("Losses:", losscounter)
    print("Total sum:", totalsum)
    print("Liquidity:", liquidity)
print("\nTotal net gain/loss:", fivemilsum)
print("Total:", (time/(60*12*24)), "days")
            


        
      
  
