# Build Status
master: [![Build Status](https://travis-ci.org/triplepoint/anagram.svg?branch=master)](https://travis-ci.org/triplepoint/anagram)

# Challenge Description
An anagram is a word formed by rearranging the letters of another, like "topside" and "deposit". In some cases, there might be as many (or more) anagrams than there are characters, like "post", "spot", "stop" and "tops".

Write a program to find all of the anagrams in a dictionary in which there are at least 4 letters in the word and at least as many anagrams as there are letters.

The dictionary will be a file on disk with one line per word. Your operating system likely already has such a file in /usr/dict/words or /usr/share/dict/words.

The output produced by your code should be in this format:

emit, item, mite, time
merit, miter, mitre, remit, timer
reins, resin, rinse, risen, serin, siren
inert, inter, niter, retin, trine
inset, neist, snite, stein, stine, tsine

_______________________

Ps: We request that the solution be in Python, and you may submit your solution as a github repo or gist. Please let me know if you have any questions or concerns.

# Additional Notes
- To execute the code do:
 - cd <project_root>
 - python ./anagram/anagram.py

- to run the tests do:
 - cd <project_root>
 - python -m tests.anagram_tests
