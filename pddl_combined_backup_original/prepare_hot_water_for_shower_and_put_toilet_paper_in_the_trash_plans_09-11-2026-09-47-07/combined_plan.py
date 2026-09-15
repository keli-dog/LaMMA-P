```pddl
0.000: (gotoobject robot2 faucet) [0.000, 1.000]
0.000: (gotoobject robot3 countertop) [0.000, 1.000]
1.000: (switchon robot2 faucet) [1.000, 2.000]
1.000: (pickupobject robot3 toiletpaper) [1.000, 2.000]
2.000: (gotoobject robot2 lightswitch) [2.000, 3.000]
2.000: (gotoobject robot3 garbagecan) [2.000, 3.000]
3.000: (switchon robot2 lightswitch) [3.000, 4.000]
3.000: (putobject robot3 toiletpaper garbagecan) [3.000, 4.000]
```