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

## Day 4: Printing Department (Dec 5)

First part I was able to brute force. Need to think of a more optimal solution. Second part looks for sure tho like a graph question (BFS)? I'll likely need a queue to add nodes to check to.

### Second part logic ruminations
Let's say we start at (0, 0). Steps to take:
- if current node is a `.`
    - add all adjacent nodes that are not "seen" to the queue
    - mark self as seen (`*`)
- if current node is a `@`
    - add all adjacent nodes that are not "seen" to the queue
    - check adjacent nodes to see if we can remove.
    - if the roll can be removed, mark it as `*`
    - else, keep the `@` and continue
- if current node is `*`, continue

(or just run the algorithm for p1 again and again until there has been no rolls removed)

## Day 5: Cafeteria (Dec 5)

### Reqs

Input parsing:
- fresh ingredient ID range (`d-d\n`).
    - ranges are inclusive.
    - ranges may overlap
- blank line (`\n \n`)
- available ingredient IDs (`\n`)

Logic:
- merge ranges together to form distinct ranges
  - sort by lowest boundary first
- iterate through available ingredient IDs and check if it's in a range

Response:
- number of fresh ingredients

### Coding
Ran into a bit of an issue in the initial submission for checking ingredient freshness -- I was doing an outer loop with each ingredient, and then incrementing the window if the ingredient did not fit in the window, except I forgot to check if the ingredient fit in the new window. The example file ran properly, but the actual input did not. Ended up rubber-ducking with AI to check what I could've missed. After 2-3 prompts (Perplexity kept showing me "gotchas" that weren't actually the issue), we were able to pinpoint the issue of skipping the check. Instead of continuing with the ingredient list as an outer loop, I swapped to using the windows as an outer loop -- change windows only when ingredient is actually not part of it, otherwise increment ingredient until exhausted.

Part 2 was a lot easier since I had deduped the initial ranges for part 1 -- simple math to resolve the questions.

Complexity analysis... I think it falls under `O(n + m)` where `n` is the number of ID ranges and `m` the number of ingredients?

Breakdown:
- parsing the file: read `n` + `m` lines => `O(n + m)`
- deduping the ranges: go through each range once => `O(n)`
- checking the ingredients: `O((min(n, m)))`, since we break out of the loop as soon as one list is exhausted, and it's at most `O(n + m)`

Adding that together it's `O(n + m)` right?

