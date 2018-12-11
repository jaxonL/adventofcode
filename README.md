# Advent of Code
Code used for the challenges for 2018's [AoC](https://adventofcode.com/2018/) with my experience logged here.

## Preface
I only discovered the existence of Advent of Code through work. I had known about month-long events for writing ([NaNoWriMo](https://nanowrimo.org/)) or for drawing ([Inktober](https://inktober.com/)) before I met AoC. I got to know about it through the `programming` channel of our company-wide messaging software. My goals are to complete the challenges daily (at least to the best of my abilities) and  to learn some python in the process.

## Day 1: Chronal Calibration
The first part of the challenge was straightforward: parse the input file and sum it all together. Wanting to revisit my first programming language crush, I verified the existence of `java` and `javac` on my machine and created a `ChronoCalibrator` class file. I thought it was going to be easy; just read in each line of the file as an integer, push them into an array, iterate over the array, and return the final sum.

It wasn't hard, persay, but I realised I had chosen too *heavy* of a language for the task. I didn't *need* to write a class. I didn't *need* to do OOP. I didn't *need* multiple functions. But separating code into smaller, independent modules had become a habit. So, I trudged on.

First pass of the code through the compiler: it complains that I may run into a `FileNotFoundException`, so I needed to somehow handle that (error handling in Java was something that I hadn't learned in CEGEP, 'cause I'd left for uni too early and broke up with Java). Using my JavaScript knowledge of try/catch blocks, I quickly wrapped the whole main function in it and recompiled the code. The `printf`s are there mostly for myself and to see if what I'm doing (and what I remember of Java) is correct. After a successful run, I earned my star and proceeded to part two.

A cursory glance at what was asked was enough to convince me to use a scripting language instead. I'm still not sure if it was the best way, but I knew that using a map/dictionary data structure would be efficient* for this problem. I originally wanted to use TypeScript for the second part, however I had not setup my coding environment and was not at home at the time (I also for some reason did not think I had python installed). I rewrote the first part in js (with some tweaks to parsing, because Atom automatically adds a newline to files on save) and ran it using node.

Since I was used to coding with TypeScript at work and that it was basically just js with syntactic sugar, naive me was pelted with `Unexpected token` errors. I had declared my class like this:

```javascript
class ChronoCalibrator {
  currentFrequency = 0;
  timesCalibrated = { 0: 1 };

  calibrateFrequency = (calibrateBy) => { /* ... */ }
  calibrateFromArray = (calibrationArr) => { /* ... */ }
  // ...
}
```

Stupid mistakes, I know. I thought that by just removing the `private` keyword and the type definitions it would compile. A Google search later, I had restructured my class syntax and got my code to run. (It was also at this point that I thought about writing a test suite and promptly dismissed that idea as that was ***definitely*** overkill.)

I didn't like not seeing any indication of running code (apart from a hanging terminal), especially when loops were involved. Thus, I resorted to logging each change to the frequency of my Temporal Anomaly Detection Instrument. At first, I thought I was stuck in an infinite loop because the logs on the screen would flicker, indicating change, but wasn't stopping. I killed the window in which it was running, added a counter (`times`) for the number of times I ran through the array completely, and slowly incremented that as a safety blanket. I could then know for sure that my code would stop. I ran it three times (increasing my counter range by 10). In less than 1000 repeats, I had found the correct frequency to set my machine.

I was curious as to how long the other ~~elves~~ programmers' solution took, so I dropped by the [subreddit](https://www.reddit.com/r/adventofcode/) to see if there were people discussing it (all the while trying to avoid seeing explicit solutions, because I hadn't gotten my star yet). As my code had already run for 5 s with no indication of ending and others were talking about fractions of milliseconds, I had to be doing something wrong, right? I set up some timers with `console.time` and commented out my debug logs. Turns out, sending information to an output stream was what slowed down the code.

![Screenshot of timing results](https://github.com/jaxonL/adventofcode/raw/master/days/1/timing.png)

\* As it is, my code is (unsurprisingly) inefficient (since there is no need to save and check the number of times a frequency is visited, we just need to save the visited frequency down and check if it is in our list). I did have a hunch that there would be a mathematical way to determine the frequency. Instead of grabbing a pen and paper and trying to find a pattern though, I opted to just brute force it. [This post here](https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eaukxu5/) sums it up pretty neatly. Congruence and modular arithmetic -- of course! Ah, the good, warm, fuzzy memories of Math 135 are coming back...

All in all, I'd say day one wasn't bad. It was definitely an easy problem at first glance. I consider myself lucky to have received the input I did, because if it were, for example, just \[+10000000, -9999999\], it would have been a completely different runtime. Upon revisiting the solutions, I became aware of my unnecessary antics and non-optimal implementation. I'll try to keep in mind optimisation and minimise brute-forcing for the upcoming challenges. I don't think I'll be tackling day 2's challenge at midnight though; my nest of blankets seems very cosy as of right now.

## Day 2 and Day 3 (Inventory Management System and Prototype Fabric)
I started both of these days very late in the day. I also decided to try my hand at python (not great). To me, these two days were levels above the first day. I did attempt to code something somewhat efficient (but not space efficient) in the first part of day 2. Not sure how that compares, but it did the job. I read a bit on how to approach the second part; sadly my tiny, tired brain couldn't think of anything. Despite my thoughts wandering through the concepts of compressed tries and Levenshtein distances, I ended up not reaching for the second star.

Determined to figure out day 3, I jumped in as soon as I got back from work. I decided to brute force my way first (solve it, then refine/read about it). I made sure to work on a small scale first, then work my way up with the given input. 2D ~~arrays~~ lists in python was something new for me. The following took me quite a while to figure out what was wrong:

```python
oneColumn = [ 0 for x in range(squareLength + 1)]
squareFabric = [oneColumn for x in range(squareLength + 1)]

squareFabric[0][0] = 1
```

The above code results in the entire 'first column' (so for `squareFabric[x][0]`) to equal 1. Visually:

```python
# expected:
# [1, 0, 0, ...]
# [0, 0, 0, ...]
# [0, 0, 0, ...]
# [...]

# actual:
[1, 0, 0, ...]
[1, 0, 0, ...]
[1, 0, 0, ...]
[...]
```

Interestingly enough, finding the overlapping square inches of fabric reminded me of the coding challenge I had to complete during the group interview phase at my current internship. Furthermore, during the actual interview, I remember my interviewers asking about possible optimisations for that similar question. Unfortunately for me, I don't quite remember my answers...

In the end, because I wanted to complete the challenge before midnight, I went with a subpar algorithm that first builds an array of overlapped points, then one by one compares whether a specified rectangle contains that point. As soon as it did, I stopped checking for other points and passed onto the next rectangle. I had a total of 118322 points to check over a maximum enclosing square of 999 x 999. Not efficient at all :')

(I also don't quite know why my commented code didn't work... oh well.)

## Day 4 (Repose Record)

As I wrapped up day 3 with 20 minutes to spare, I stayed awake long enough to peek at the first part of day 4. And man, was that a bad idea. I ended up having it simmering in the back of mind for the whole day before I got the chance to sit in front of my laptop and flesh a solution out. I wanted to try something new: detail my thought process as I code the solution (instead of revisiting it or leaving random, achronological comments).

The problem at hand:
* find the id of the guard who slept the most
  * meaning that we have to sum up the times they were asleep
* find the minute where the guard was asleep the most
  * meaning that we have to also store the times the guard was asleep

How my brain wants to tackle it:
* maybe having a library to parse the dates out of the first segment of the string would help
* we know there is only one guard per night (that may start their shift @ 23:xx instead of 00:xx)
* only the minutes matter for the asleep/awake events
* we only care about the first character of the event (*f* for 'falls asleep', *w* for 'wakes up', and *G* for 'Guard #xxx begins shift')
* we shouldn't even care about the year (1518) as it ~~shouldn't~~ doesn't change
  * but is 1518 a leap year? (Google says no, phew. No need to consider February edge cases)

Before writing down these points, I wanted to have some sort of map/~~array~~list/dictionary where the id of the guard and the date would be some sort of primary and secondary keys (was working on DynamoDB tables today, so maybe that had to do with it) and storing time intervals. Having the outline in front of me though prompted me to think: what about just storing the numbers from 0 to 59 (for the minutes of a shift) and each having a counter in them (for how many times the guard has slept on that minute). I'll take a shot at it and report back on my results. (I have a feeling that most, if not all, of my solutions are going to be not great on time and space cost.)

Personal goals of the day:
* get more comfortable with list
* start putting code into functions

Stuff I ran into:
* Apparently, python doesn't have switches? That's... new.
* The cases I have to pay attention to are the 'guard x begins shift' ones, as the day value can be that of the "previous" day (right before midnight). The wake/sleep events happen for sure during 00:00 and 00:59, so the date does not need to be manipulated.
* Waking up and falling asleep are only the extremities of a range. I need to extract that information so that I can counterise the minutes
  * Easiest way would be to sort the array by date and minute
  * I know that w/f events are toggles; maybe I can use that to my advantage...
* somehow, I thought that I was shallow copying some ints but ended up being my own sortkey algorithm mistake (I multiplied the date by 1000 instead of 10000, which had some overlap with the time)

Part 1 is done at this point (after much debugging). Luckily, I can re-use most of my code for part 2 for an inefficient solution. After spending 10 minutes on not comprehending why I wasn't printing the right result (hint: because I was still printing 'sleepiest' instead of 'mostTimesAsleep'), I finally got my answer and submitted it.

I think I've gotten to that point in a relationship with a new language where you're frustrated at it and questioning why you still want to continue investing in that relationship (to be fair though, most of the onus is still on programming errors...).

### Bonus -- Complete day 2 part 2

Day 2 part 2, for the O(n!) solution I had, did not require that much time to implement. Maybe I was just trying to optimise too much that I scared myself into not solving it until I could conceive of the perfect solution (and we all know that perfect code does not exist). I went with a simple letter-double checking algorithm that could short-circuit as soon as the two package ids differed in letters at two different positions. It ran fairly fast (no benchmarking), even with print statements.

## Day 5 (Alchemical Reduction)
I'm not asleep at 12, so I open my advent challenge. This time, it's parsing! Or, something of the sort. Part 1 at least doesn't look that complicated, and I have two ideas of what I can do:

a. iteratively:
  1. have a base string/buffer to which we add chars
  2. read in the input, 1 char at a time
  3. if the difference in ascii code between the two chars are ['A' - 'a'] (off the top of my head that's 97 - 64? (edited to add: actually no; A = 65 and a = 97)) (absolute value that), do not append to the string AND remove last appended char
  4. repeat step 3 with the last char in the buffer until we don't match
  5. in case of a no-match, append the char and repeat

b. recursively:
  1. read in entire string
  2. do passes on the string until we can't reduce it anymore

Visibly, I have thought out the iterative process a lot more than the recursive one. (This problem just seems like it would do well in recursion, which is why I even mention it. However, after typing out my thoughts, I see that loops just might do the trick (in linear time probably too!).) Now to wrestle with python and getting the results I want...

I ended up spending an hour on the problem. Sleep deprivation while trying to code is not good, as demonstrated by me trying to obtain a polymer of length 10 -- somehow, I had read that the resulting polymer would have 10 units and the question was asking for the string obtained. When I jumped onto the project again after being away from it for 17 hours, I still had that belief until I went and re-read the question. My first answer was too high. A nagging feeling told me that I was probably off by one. Sure enough, I waited out the 60 seconds (ready to restart the problem if needed), submitted the length I obtained - 1, and unlocked part 2.

Edited to add: my off-by-one error comes from an extra whitespace appended to the end of my string buffer. Weird, but fixed with some stripping on input read.

[First reaction upon reading part 2 (censored version because I want to appear professional).](https://youtu.be/M1LpvApZtQ8)

But then, I let my mind wander and think of other possible ways to solve this:

For every possible letter, remove the set of it, reduce the polymer, then count its length.
  * I don't need to tell you why that's a bad idea. For reference, this is originally why I was so er, repulsed, at first.

... (thinking) ...

The polymer reacting condition reminds me of that one coding question where you had to match up brackets. The solution involved using a stack to keep track of what was being parsed.

... (more thinking) ...

Continuing on with the stack idea, we can find the character we want to remove by going through the string and "counterising" every 'possible removal' per character removed (case not-withstanding). (Also note that it didn't matter whether we removed the characters first then reduced or reduced then removed, so, for time's sake, I work with the already reduced version.) Enter my O(n^2) `getFoldOccurences` that estimate the number of reactions (which I call fold) that occur when a character is removed. Once that was found, we just needed to remove the character that invoked the most folds and pass the result through our polymer reduction algorithm again. (I had to output stuff into another file and then read the code from there; a lazy layman's way to approach the issue at hand. Forgive the countless `print`s scattered throughout the code.)

I checked by reddit to browse some answers before the next problem. There is one person who [solved the problem in Vim](https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4iki6)! The next two comments on the solutions megathread are all in python (very little code too :')) (see [here](https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4cvto) and [here](https://www.reddit.com/r/adventofcode/comments/a3912m/2018_day_5_solutions/eb4ff0j)). I don't completely understand how these snippets do what they do (I think I see a semblance of switch in there somewhere), so I'll be off doing some research before peaking at day 6.

## Day 6 and Day 7 (Chronal Coordinates and The Sum of Its Parts)

Going from the year 1518 to a new one apparently means new terms ([Manhatten distance/Taxicab geometry what?](https://en.wikipedia.org/wiki/Taxicab_geometry)) and (subjectively) harder problems. It's another visual/spatial enigma involving coordinates, so the first data structure to cross my mind is a 2D array. But this time, it's not that simple (self-imposed time constraints on my end as well because I was out 'til now). Luckily for me, I had a refresher on my data structure course on day 3 and day 4 when I considered using a range tree or a compressed trie respectively. As we are dealing with 2D points, a tree used to represent a range of them is certainly a plausible solution. For reference, [this](https://www.student.cs.uwaterloo.ca/~cs240/s18/modules/module08.pdf) is the document I'm skimming through for my refresher. I decide to separate part 1 into 3 parts:

1. determining the coordinates that have a finite "territory"
2. finding the area of said territory
3. getting the max of possible territory areas

I can easily find a bounding box in O(n) for my coordinates, and from there determine that any point that has a coordinate on the bounding box has an infinite area of closest points. I deduced that in order for a point to have a finite area, it needs to be bounded by the perpendicular lines of the medians between said point and at least 3 others (to form some kind of triangular boundary).

While I am still gauging out day 6, day 7 became available. And wow, it definitely looks easier than day 6 so...

Very quickly, I list a todo list for the sleigh-assembly-instruction-order-determining algorithm:

1. Parse out the 2nd (2) and 8th (8) token (2 must be done before 8)
2. Store the order as we parse.

I have decided to put a rain check on day 6 (and possibly day 7, due to events) and will come back another time to unwrap my advent stars.
<!-- Day 7: trees and linked lists may have helped but... -->

## Day 8 (Memory Maneuver)

Day 8's hard part, before I even start to attack the question, is to parse the input and to construct the tree. Part 1 doesn't seem so hard; we could technically not even create a tree (which may or may not be used in part 2) and solve the summing of metadata. I suspect it to be very easy to mess up the parsing and then getting the wrong sum though. An outline for the algorithm:

1. Read in two integers, `childrenCount` and `metadataCount` respectively (if there is no data to read (finished parsing the last node), go to step 4)
2. If `childrenCount` > 0, push `childrenCount` into `childrenStack` and `metadataCount` `metadataStack` and repeat steps 1-2
3. (Previously parsed `childrenCount` is 0) Read in `metadataCount` integers from the file and sum them
4. Pop an element from `childrenStack` and subtract 1 from it.
5. If the resulting count is 0, repeat steps 3-4; else, push it back into the stack and go to step 1.

Good thing (not usually, but for my uses) python passes parameters by reference.

What's not a good thing is that my wanting to be lazy with part 1 comes back to bite me in part 2.

I mean, building a tree for a problem concerning a tree is probably the way to go, especially if the whole concept is related to trees and nodes. /s

A possible way to do it is to build a tree out of the input, save a "node value" property in the node, and get the node value of the first node. (Note that it's already past midnight, and day 9 is up by now.)

Important stuff for part 2:

* I need to keep track of the values of immediate children nodes and the order (`x`th child)
* a node with 0 children's value is the sum of its metadata
* the metadata refers to the indices of the node's children whose values we want to consider. If that child node is mentioned twice, its value is counted for twice

Recursion is also a good friend, especially when it comes to trees. The recursive solution for part 2 seemed a lot more cleaner than the linear/iterative approach in part 1.

## Day 9 (Marble Mania)

How do I even start? Let's list down what we know:

* the number of points the last marble is worth indicates how many marbles are placed (eg: if the last marble is worth 25 points, then the elves are playing with 26 marbles (including marble #0), but only placing 25 (because the 0th marble is placed in the centre))
  * this is also the number of turns the game takes
* every marble that has a value that is dividable ([divisible](https://english.stackexchange.com/questions/85111/when-to-use-divisible-vs-dividable)? Had to google this to make sure the usage was right.) by 23 is not placed in the circle; instead, it is added to the points earned by the elf playing that turn
* at the same time as the above, the marble that is 7 marbles ccw of the current marble is removed; its points added to the same elf; and the marble immediately after it becomes the current marble in play ( <- hard part right here)

Based on this, letting `x` be their position of play (the first player is numbered `1`) and `y` be the total number of players, we can determine an elf's score to be the sum of the values of the following:
1. all the marbles with a value of a multiple of 23 the elf was supposed to play and
2. the marbles that were 7 marbles ccw of the 'current marble' during that turn

1 can be calculated as such:
* the first player to get that marble is the one that plays on turn 23. Thus, `23 % y` gives the position of the player who earns the 1st 23 + 9 \[according to the example\] points (if the result of the modulo = 0, then the `y`th elf to play gets the marble).
* the second player to not play a marble is the one who plays marble 46, so `46 % y`th player
* the third one would then be `(3 * 23) % y`, and so on

Thus, `x = (n * 23) % y` with `n` in { 1, 2, 3, ..., `floor(total num of marbles / 23)`}.

2 is the harder part. Would I have to keep track of everything in order to calculate a high score? I then remembered something I read about yesterday, when looking into deques and how they were double-ended. Deques in python had a rotate function. The marbles in our game were placed in a circle. I can leverage the clockwise and counter-clockwise insertions by just rotating a deque n times, and appending to the end/beginning of it. That way, I didn't need to keep track of the index of my 'current marble' -- it would always be the last (or the first, depending on how I implement it) element in the deque. Data structures to the rescue! For inserts, I decide to rotate my deque by 1 index counter-clockwise (to the left, so by -1), then append my next marble to the end of it. For each 23rd marble, I would have to save the value to the numbered elf player, rotate to the right (clockwise) 7 times, pop the last element and add that to the score, then rotate cw another time to set the 'current marble' to the marble immediately clockwise of the popped marble. I could also just rotate cw 6 times and remove the second to last element, but I didn't find an integrated function to do so (or just not enough research), so I'll stick to the former solution.

Part 2 involved me passing in a value 100 times larger. Performance did take a hit (maybe a few seconds), but I got the right answer. I'm now on my way to browse reddit for day 9 solutions (leaving day 6 and day 7 in my back log for now).

## Day 10

Flabbergasted. Dumbfounded. Unsure how to solve this. My weaknesses are graphical problems, I suppose. Part 1 asks for the message that the stars will spell out, after a certain amount (`x`) of seconds have elapsed. The problem here is to determine *when* (what `x` is) our stars are aligned, then to parse out the message that is given.

A greedy approach is to visually place every point and its trajectory onto a graph and, second-by-second, move it until we reach a message. This involves iterating over all `n` points for `x` times -- as `x` is fixed, the overall solution would take `O(n)` time. Space-wise however it depends on the max distance between all the points at the beginning (because they should be moving at least towards each other).

Brainstorming points:
* given the x-y coordinates and the velocity of a star, we can trace a line
* all points should be moving towards a same direction (around the area where the message should finally appear)
* assuming that letters are formed by continuous lines, at time `x`, all stars should be adjacent to at least one other star
