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
