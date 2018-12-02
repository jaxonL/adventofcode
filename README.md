# Advent of Code
Code used for the challenges for 2018's [AoC](https://adventofcode.com/2018/) with my experience logged here.

## Preface
I only discovered the existence of Advent of Code through work. I had known about month-long events for writing ([NaNoWriMo](https://nanowrimo.org/)) or for drawing ([Inktober](https://inktober.com/)) before I met AoC. I got to know about it through the `programming` channel of our company-wide messaging software. My goals are to complete the challenges daily (at least to the best of my abilities) and  to learn some python in the process.

## Day 1: Chronal Calibration
The first part of the challenge was straightforward: parse the input file and sum it all together. Wanting to revisit my first programming language crush, I verified the existence of `java` and `javac` on my machine and created a `ChronoCalibrator` class file. I thought it was going to be easy; just read in each line of the file as an integer, push them into an array, iterate over the array, and return the final sum.

It wasn't hard, persay, but I realised I had chosen too *heavy* of a language for the task. I didn't *need* to write a class. I didn't *need* to do OOP. I didn't *need* multiple functions. But separating code into smaller, independent modules had become a habit. So, I trudged on.

First pass of the code through the compiler: it complains that I may run into a `FileNotFoundException`, so I needed to somehow handle that (error handling in Java was something that I hadn't learned in CEGEP, 'cause I'd left for uni too early and broke up with Java). Using my JavaScript knowledge of try/catch blocks, I quickly wrapped the whole main function in it and recompiled the code. The `printf`s are there mostly for myself and to see if what I'm doing (and what I remember of Java) is correct. After a successful run, I earned my star and proceeded to part two.

A cursory glance at what was asked was enough to convince me to use a scripting language instead. I'm still not sure if it was the best way, but I knew that using a map/dictionary data structure would be efficient* for this problem. I originally wanted to use TypeScript for the second part, however I had not setup my coding environment and was not at home at the time (I also for some reason did not think I had python installed). I rewrote the first part in js (with some tweaks to parsing, because Atom automatically adds a newline to files on save) and ran it using node.

Since I was used to coding using TypeScript at work and that it was basically just js with syntactic sugar, naive me was pelted with `Unexpected token` errors. I had declared my class like this:

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

I didn't like not seeing an indication of running code (apart from a hanging terminal), especially when loops were involved. Thus, I resorted to logging each change to the frequency of my Temporal Anomaly Detection Instrument. At first, I thought I was stuck in an infinite loop because the logs on the screen would flicker, indicating change, but wasn't stopping. I killed the window in which it was running, added a counter (`times`) for the number of times I ran through the array completely, and slowly incremented that as a safety blanket. I could then know for sure that my code would stop. I ran it three times (increasing my counter range by 10). In less than 1000 repeats, I had found the correct frequency to set my machine.

I was curious as to how long the other ~~elves~~ programmers' solution took, so I dropped by the [subreddit](https://www.reddit.com/r/adventofcode/) to see if there were people discussing it (all the while trying to avoid seeing explicit solutions, because I hadn't gotten my star yet). As my code had already run for 5 s with no indication of ending and others were talking about fractions of milliseconds, I had to be doing something wrong, right? I set up some timers with `console.time` and commented out my debug logs. Turns out, sending information to an output stream was what slowed down the code.

![Screenshot of timing results][timingResults]

\* Turns out (unsurprisingly) that my code is inefficient (since there is no need to save and check the number of times a frequency is visited, we just need to save the visited frequency down and check if it is in our list). I did have a hunch that there would be a mathematical way to determine the frequency. Instead of grabbing a pen and paper and trying to find a pattern though, I opted to just brute force it. [This post here](https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eaukxu5/) sums it up pretty neatly. Congruence and modular arithmetic -- of course! Ah, the good, warm, fuzzy memories of Math 135 are coming back...

[timingResults]: https://github.com/jaxonL/adventofcode/raw/master/days/1/timing.png
