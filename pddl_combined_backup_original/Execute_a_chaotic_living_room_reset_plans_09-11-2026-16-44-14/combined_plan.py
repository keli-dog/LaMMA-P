```pddl
0.000: (gotoobject robot1 floorlamp) [1.000]
0.000: (gotoobject robot2 book) [1.000]
0.000: (gotoobject robot3 cabinet) [1.000]
0.000: (gotoobject robot4 pillow) [1.000]

1.000: (switchoff robot1 floorlamp) [1.000]
1.000: (pickupobject robot2 book) [1.000]
1.000: (closeobject robot3 cabinet) [1.000]
1.000: (pickupobject robot4 pillow) [1.000]

2.000: (gotoobject robot1 laptop) [1.000]
2.000: (gotoobject robot2 shelf) [1.000]
2.000: (gotoobject robot3 drawer) [1.000]
2.000: (gotoobject robot4 couch) [1.000]

3.000: (switchoff robot1 laptop) [1.000]
3.000: (putobject robot2 book shelf) [1.000]
3.000: (closeobject robot3 drawer) [1.000]
3.000: (putobject robot4 pillow couch) [1.000]

4.000: (gotoobject robot1 lightswitch) [1.000]
4.000: (gotoobject robot2 remotecontrol) [1.000]
4.000: (gotoobject robot3 fridge) [1.000]
4.000: (gotoobject robot4 blanket) [1.000]

5.000: (switchoff robot1 lightswitch) [1.000]
5.000: (pickupobject robot2 remotecontrol) [1.000]
5.000: (closefridge robot3 fridge) [1.000]
5.000: (pickupobject robot4 blanket) [1.000]

6.000: (gotoobject robot1 television) [1.000]
6.000: (gotoobject robot2 coffeetable) [1.000]
6.000: (gotoobject robot4 couch) [1.000]

7.000: (switchoff robot1 television) [1.000]
7.000: (putobject robot2 remotecontrol coffeetable) [1.000]
7.000: (putobject robot4 blanket couch) [1.000]

8.000: (gotoobject robot2 vase) [1.000]

9.000: (pickupobject robot2 vase) [1.000]

10.000: (gotoobject robot2 sidetable) [1.000]

11.000: (putobject robot2 vase sidetable) [1.000]
```