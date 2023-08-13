# README
This is a simple set of functions to compute probabilities for Risus: The
Anything RPG.

Risus was designed by S. John Ross and is currently published by Big Dice
games: https://www.risusrpg.com/

# Basic API Calls
See the documentation for the module for an overview of possible
calls. In short, there are functions to compute win/loss chances for
combat, team combat (including inappropriate clichés), single-action
conflicts, and target number rolls. All the calls return floats, and
take a boolean argument `percent` to indicate whether the returned
value should be scaled 0 to 100 or 0 to 1.

The internal functions (for `combat` and `team_combat`) that handle
the Die objects are prefixed with `_`. These implement the
computations recursively and so must return Die objects. The
front-facing versions simply wrap these and clean up the data before
returning it.

# Tables
The function `make_victory_table` can compute a table like the following, where
each entry is the probability (as a percentage) that a cliché of the
left-column potency will eventually beat a cliché of the top-row potency in
combat. For example, a cliché of potency (7) has a 15.8% chance of beating a
cliché of potency (8) in head-to-head combat.

## Combat:
```
       1      2      3      4      5      6     7     8     9     10
1    50.0    5.0    0.1    0.0    0.0    0.0   0.0   0.0   0.0   0.0
2    95.0   50.0    8.2    0.3    0.0    0.0   0.0   0.0   0.0   0.0
3    99.9   91.8   50.0   10.5    0.7    0.0   0.0   0.0   0.0   0.0
4   100.0   99.7   89.5   50.0   12.2    1.1   0.0   0.0   0.0   0.0
5   100.0  100.0   99.3   87.8   50.0   13.7   1.5   0.1   0.0   0.0
6   100.0  100.0  100.0   98.9   86.3   50.0  14.8   1.9   0.1   0.0
7   100.0  100.0  100.0  100.0   98.5   85.2  50.0  15.8   2.3   0.1
8   100.0  100.0  100.0  100.0   99.9   98.1  84.2  50.0  16.7   2.7
9   100.0  100.0  100.0  100.0  100.0   99.9  97.7  83.3  50.0  17.5
10  100.0  100.0  100.0  100.0  100.0  100.0  99.9  97.3  82.5  50.0
```
Team combat is also possible, but this one goes into three dimensions!

## Single-action conflict:
```
       1      2      3      4     5     6     7     8     9     10
1    50.0   10.0    1.2    0.1   0.0   0.0   0.0   0.0   0.0   0.0
2    90.0   50.0   16.3    3.7   0.6   0.1   0.0   0.0   0.0   0.0
3    98.8   83.7   50.0   20.5   6.3   1.5   0.3   0.0   0.0   0.0
4    99.9   96.3   79.5   50.0  23.5   8.6   2.6   0.6   0.1   0.0
5   100.0   99.4   93.7   76.5  50.0  25.7  10.7   3.7   1.1   0.3
6   100.0   99.9   98.5   91.4  74.3  50.0  27.5  12.6   4.9   1.6
7   100.0  100.0   99.7   97.4  89.3  72.5  50.0  28.9  14.2   6.0
8   100.0  100.0  100.0   99.4  96.3  87.4  71.1  50.0  30.1  15.7
9   100.0  100.0  100.0   99.9  98.9  95.1  85.8  69.9  50.0  31.2
10  100.0  100.0  100.0  100.0  99.7  98.4  94.0  84.3  68.8  50.0
```
## Target number:
```
        1      2      3      4      5      6
1   100.0  100.0  100.0  100.0  100.0  100.0
2    83.3  100.0  100.0  100.0  100.0  100.0
3    66.7   97.2  100.0  100.0  100.0  100.0
4    50.0   91.7   99.5  100.0  100.0  100.0
5    33.3   83.3   98.1   99.9  100.0  100.0
6    16.7   72.2   95.4   99.6  100.0  100.0
7     0.0   58.3   90.7   98.8   99.9  100.0
8     0.0   41.7   83.8   97.3   99.7  100.0
9     0.0   27.8   74.1   94.6   99.3   99.9
10    0.0   16.7   62.5   90.3   98.4   99.8
11    0.0    8.3   50.0   84.1   96.8   99.5
12    0.0    2.8   37.5   76.1   94.1   99.0
13    0.0    0.0   25.9   66.4   90.2   98.0
14    0.0    0.0   16.2   55.6   84.8   96.4
15    0.0    0.0    9.3   44.4   77.9   93.9
16    0.0    0.0    4.6   33.6   69.5   90.4
17    0.0    0.0    1.9   23.9   60.0   85.5
18    0.0    0.0    0.5   15.9   50.0   79.4
19    0.0    0.0    0.0    9.7   40.0   72.1
20    0.0    0.0    0.0    5.4   30.5   63.7
21    0.0    0.0    0.0    2.7   22.1   54.6
22    0.0    0.0    0.0    1.2   15.2   45.4
23    0.0    0.0    0.0    0.4    9.8   36.3
24    0.0    0.0    0.0    0.1    5.9   27.9
25    0.0    0.0    0.0    0.0    3.2   20.6
26    0.0    0.0    0.0    0.0    1.6   14.5
27    0.0    0.0    0.0    0.0    0.7    9.6
28    0.0    0.0    0.0    0.0    0.3    6.1
29    0.0    0.0    0.0    0.0    0.1    3.6
30    0.0    0.0    0.0    0.0    0.0    2.0
31    0.0    0.0    0.0    0.0    0.0    1.0
32    0.0    0.0    0.0    0.0    0.0    0.5
33    0.0    0.0    0.0    0.0    0.0    0.2
34    0.0    0.0    0.0    0.0    0.0    0.1
35    0.0    0.0    0.0    0.0    0.0    0.0
36    0.0    0.0    0.0    0.0    0.0    0.0
```
