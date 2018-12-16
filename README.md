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

I'm back (on day 10, because well... graphic stuff is confusing). I'm thinking about other ways to solve it (because the sleigh code wasn't working; wasn't considering edge cases, etc.). I have to keep track of what comes after (or before) a character in case I need to move it around a string. Enter an inelegant solution:

For each character...
* ... keep track of the letters that come before the character
* ... keep track of how many (quantity) letters come after the character (counter 'x')

We can then build the string up *backwards*:

1. find the characters that have 0 as their value for 'x'
2. order them in alphabetical order then append in front of the instruction string
3. subtract 1 from the `x` values of all the letters that come before all the appended character(s)
5. remove the character(s) from the set
4. repeat until no characters are left

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

## Day 11 (Chronal Charge)

I'm sure there's a way to plot these variations and to maximise it, if calculus has taught me anything. Trying to wrap my mind around the problem, I can get these equations (with `C` as the serial input):

* `rackId` = `x` + 10 (there are 300 of these, ranging from 11 to 310)
* `initialPowerLvl` = `y` * `rackId` = `y` * (`x` + 10) = `xy` + 10`y`
* `increasedPowerLvl` = `initialPowerLvl` + `C` = `xy` + 10`y` + `C`
* `setPowerLvl` = `increasedPowerLvl` * `rackId` = (`xy` + 10`y` + `C`)(`x` + 10) = `xxy` + 10`xy` + `Cx` + 10`xy` + 100`y` + 10`C` = `xxy` + 20`xy` + `Cx` + 100`y` + 10`C`
* `finalPowerLvl` = getTensDigit(`setPowerLvl`) - 5 = getTensDigit(`xxy` + 20`xy` + `Cx` + 100`y` + 10`C`) - 5

Getting the tens' digit of a sum is ignoring everything before the tens' unit, summing the digits in the tens' unit % 10, then summing all the digits in the ones' units and only keeping the tens' digit of that. This comes down to modulo-ing `setPowerLvl` by 100, summing it up, then (computer) dividing by 10.

As the only possible tens' digits are { 0, 1, 2, ..., 8, 9 }, the `finalPowerLvl` must be an element of { -5, -4, -3, ..., 4, 5 }. My serial number is `3463`. Thus:

> `xxy` + 20`xy` + 3463`x` + 100`y` + 34630

A few handy modular arithmetic rules:
i. `a`^2 mod `m` = (`a` mod `m`)^2 mod `m`
ii. `bc` mod `m` = ((`b` mod `m`)(`c` mod `m`)) mod `m`
iii. `d` + `f` mod `m` = `d` mod `m` + `f` mod `m`
We can ignore anything equal or greater than 100, as well as numbers ending with a 0 in the units (won't affect summation of units), so 100`y` is reduced to 0 and the tens' digit can be calculated by

> (`xxy` % 100) + (20 * (`xy` % 10)) % 100 + (63 * (`x` % 100)) % 100 (by simplifying to less than 100s to sum)
> ((`x`^2 * `y`) % 100) + (20 * (`x` % 10 * `y` % 10)) % 100 + (63 * (`x` % 100)) % 100 (using ii.)
> ((`x`^2 % 100) * (`y` % 100)) % 100 + ((20 * (`x` % 10 * `y` % 10)) % 100) + (63 * (`x` % 100)) % 100 (using ii.)
> ((`x` % 100) * (`x` % 100) * (`y` % 100) % 100) + (20 * (`x` % 10 * `y` % 10)) % 100 + (63 * (`x` % 100)) % 100 (using i.)

And then adding 3 and the units of 2`xy` after getting the tens' digit.

Let `X` = (`x` % 100) and `Y` = (`y` % 100); `a` = (`x` % 10), `b` = (`y` % 10). We get:

> (`X` * `X` * `Y`) % 100 + (63 * `X`) % 100 + (2 * `a` * `b`) % 10 + 3
> (`X` * `X` * `Y` * 63 * `X`) % 100 + (2 * `a` * `b` + 3) % 10 + 3

That gets a number under 100 that we can (computer) divide by 10 to get the tens' unit.

We then have to find the largest power value sums within a 3 x 3 square. This means:

We have `x`, `x` + 1, and `x` + 2; `y`, `y` + 1, and `y` + 2.

((Too much math; I may have messed up the top part too. I tried to attempt it in excel.))

![Zoomed out table of battery values](https://github.com/jaxonL/adventofcode/raw/master/days/11/batteryGraph.png)

![Full screen-ish table of battery values](https://github.com/jaxonL/adventofcode/raw/master/days/11/batteryGraph2.png)

You can see a repeating pattern; these don't quite look right, but at least they look pretty.

## Day 12 (Subterranean Sustainability)

After 3 days of no-solves, this challenge looks do-able? I think I may be trying too hard to get an optimal solution before I even get a solution orz.

As the usual, here are the important points:
* There are infinite pots to my left and my right
* we want the number of plants that have grown in pots after 20 generations (so sum of all plants that are alive in a generation, for 20 generations)
* the patterns that don't result in a plant at the centre position doesn't matter (?)
* when determining whether a plant will be there in the next generation, always consider two plants to its left and right. This means that the length of the string to parse may increase as the generations go on. Edge cases are the following: the first two pots in the string and the last two pots in the string
* Edited to add: I misread! We require the sum of the indices at which the plants are. We would then of course need to keep track of the index 0.

When considering what kind of data structure to use to simulate the plants, I opt for the ever-so-reliable list because of it's O(1) index accessing (that's what we'll be using most in my opinion). The downside is, unless I mark the 'starting element' as position 0, I will lose the index of the plant in front of me. As for the patterns, we can filter out those that don't resolve in a plant (it's either there will be a plant or there will not be a plant in the next generation, so if it doesn't follow the pattern, then there will be no plant). (It would also be extremely troll if we had the pattern `.... => #`; just sayin'.) We can then store all patterns in a dictionary where the key would be the 3 last characters of the pattern. This key points to a second dictionary of possible 2 character prefixes that yield a plant at the current position.

Ended up adding an offset counter to keep track of how much to the left I am extending the string. Despite passing the test case, I can't seem to get the right answer. My answer is too high. I doubt it has to do with the offset counter (should be a constant of -40 for 20 generations), so it means I messed up during generating the 20th element.

Found my error... As python is very dependent on its indents, I found that in my parsing I indented too little. At work, I'm used to 2 space indents, but somehow Atom forced everything to 4 spaces, so I tried to fix it, but gave up afterwards and tried to reset everything to 4 spaces. I missed that part...

## Day 14 (Chocolate Charts)

Hot chocolate recipe scores are a fun premise for algorithmic calculations. I tackled this one on the metro (busy week, busier weekends): by breaking down how to calculate the indices and then the values, the first part becomes a simple while loop. The only thing to look out for was adding the digits of the result (which could not go over 18, as the max score of a recipe was 9) one at a time to the resulting list. Part 2 took a bit more thinking; we could go with a forward-scanning match algorithm as we build the list, but that would involve re-evaluating the match in case we have repeating digits in our given input. Another possible implementation is the bad character heuristic, where we scan backwards, then shift when a mismatch is given, however that involves knowing the entire resulting string beforehand (all recipe values). I didn't want to build up the list of recipe scores by increments of 100, then searching, so no implementing the Boyer-Moore algorithm here. I settled instead for a simple backward-scanning search, as by the time we reach the last index, we can see if the previous indices match our give pattern, and if yes, we only have to subtract the length of the target string from the list length to get the number of recipes required by the elves before reaching the target score sequence.

Unsure why my second part got me a memory error, as shown below. Maybe I never reach the combination of recipe scores? I even looked through the solutions and tried with their line of code (which led to the error).

![Part 2 memory error](https://github.com/jaxonL/adventofcode/raw/master/days/14/part2_memErr.png)
