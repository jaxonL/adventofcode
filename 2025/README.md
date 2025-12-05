# Advent of Code (2025)

Code used for the challenges for 2025's [AoC](https://adventofcode.com/2025/).

## Why I'm back

- I want to refresh my Python. My work experience has been mainly in Javascript/Typescript land with Node.js for both frontend and backend work.
- I want to tackle bite-sized coding challenges. This is probably a better use of my time and brainpower than ~~doomscrolling~~ LinkedIn's daily puzzle games.
- 12 days with 24 puzzles -- I'll see how many I can do, as life gets busier around the end of this year. (I'm already starting late...)

A small voice in the back of my mind is shouting, "Why not just use AI?", as AI as proliferated and permeated the programming world. I want to tease my brain, the same way I would use my dying braincells to attack a logic puzzle instead of asking someone else for the answer. Sure, if I get stuck, Perplexity'll be there to hopefully guide me, but why forego trying it in the first place?

## Day 1: Secret Entrance (Dec 4)

### Pre-code

Part 1:
- looks like a `%` question, more specifically `n % 100`
- count the times we get `0`

Seems simple enough, good to use as a re-introduction to Python. Time to stop yappin' and to get with it.

### Coding

Ended up doing a bit of chore work (setting up a Makefile, looking into how Python uses modules) and spending time on confirming how to import files from the right paths. I'm sure there's a more elegant math solution for part 2 but... we're trying to catch up, so let's leave it at that.

Note to future self: since the `helpers` folder can be re-used, it's located as a sibling folder to the yearly advent directories. Thus, code needs to be run at the root-level to avoid `ModuleNotFoundError`. The location of [`Makefile`](../Makefile) reflects that.

## Day 2: Gift Shop (Dec 4)

### Reqs
Part 1 Goal: sum of invalid IDs
- Invalid IDs:
    - Part of the provided range
    - Sequence of digits repeating **twice** (e.g.: `11`, `22`, `6464`, `123123`)
        - => means that we can check if the length of the string is even (# of digits in the number) and check for all variations in the first half
    - Starts with a **leading** `0`
- Parse input:
    - Single line; entries separated by `,`
    - Ranges are inclusive
    - Min ID and max ID separated by a `-`

### Coding

Ended up using string manipulation + integers. We only need to check for the numbers constructed following the patterns (instead of if every number in the range matches the pattern).

Maybe part 2 I brute force instead...

## Day 3: Lobby (Dec 4)

Going to do just the first part for these questions. Day 4 seems like a graph question.

