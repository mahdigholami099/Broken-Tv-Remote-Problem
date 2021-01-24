# The Problem of Broken TV remote

In this problem we are going to calculate the cost of switching from one channel to the other by a broken remote.

[![License](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://github.com/mahdigholami099/Broken-Tv-Remote-Problem/blob/master/LICENSE)[![Build Status](https://api.travis-ci.com/mahdigholami099/Broken-Tv-Remote-Problem.svg?branch=master)](https://travis-ci.com/github/mahdigholami099/Broken-Tv-Remote-Problem)
&nbsp;

## Rules Explanation

We have a broken TV remote. Some buttons on the remote are unfunctional.
Changing between TV channels will have a cost.
And the right answer to the problem will be the way which will cost us the least.
To change between channels we have these buttons:

* channel 0 to 9 buttons
* up button for switching to the next channel
* down button for switching to the last channel
* \- button for selection double digit channel

### Number button usages

for switching into a single digit channel we can use the number buttons.
For switching into double digit channels we must use double digit channel selection button then the number buttons.

example :

* switching to channel 8: pressing the button 8 on the remote
* switching to channel 13: pressing double digit channel-pressing button 1-pressing button 3

### Direction Button’s usages

For switching to the next channel we use the “up button” and for switching to the previous channel we use “down button”. However, these buttons will have a rotation. For example, if we are on channel 99 and we press the up button, TV will switch to channel 0.
And if we are on channel 0 and press down button we switch to channel 99.

### Combining the direction buttons and number buttons

For more cost efficiency we can use both number buttons and direction buttons combined.

&nbsp;

## Cost Calculation

The cost of switching between channels will be calculated according to the formula bellow:

```
Cost of original (the channel we’re on right now) +
cost of goal channel (the channel we want to switch into) +
cost of the channels we have traveled +
cost of each pushed button
```

```
Each button cost: 1 
Each channel cost: will be calculated according to the input
```

if there is no way of reaching the goal channel the program returns -1

 &nbsp;

## Input/Output Format

The format will be displayed in 13 lines.

```
First line: number buttons
Second line: direction buttons
Third to twelfth lines: cost of each channel
Thirteenth channel: origin and goal channel
```

First and second lines are 0 and 1’s in which 0 indicates button being broken and 1 being the functional button.

### sample input

```
1 0 1 0 0 1 1 1 1 1
1 1 1
736 994 106 631 657 803 689 706 734 656
554 673 364 371 700 795 489 473 877 274
637 898 342 558 184 597 11 910 761 647
916 338 342 863 623 796 819 39 670 513
764 119 989 224 187 518 830 29 758 877
578 395 141 918 479 882 673 247 82 716
334 824 429 354 89 43 674 914 292 865
538 64 525 758 824 317 146 593 866 988
47 69 387 59 763 431 958 233 749 813
972 153 629 957 641 743 581 804 425 614
26 94
```

In this input 1,3,4 are broken buttons.

### sample output

```
1399
```

First we switch to channel 95 then 94. In this process we use the number buttons 9 and 5. Then we use down button to reach channel 94 so the cost is:

4 + (11+743+641) = 1399
