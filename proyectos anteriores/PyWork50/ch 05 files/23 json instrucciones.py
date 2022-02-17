"""
In this exercise, you’re analyzing test data in a high school.
There’s a scores' directory on the filesystem containing a number of files in JSON format.
Each file represents the scores for one class.

Write a function, print_scores, that takes a directory name as an argument
and prints a summary of the student scores it finds.

If you’re trying to analyze the scores from class 9a, they’d be in a file called 9a.json
that looks like this:

[{"math" : 90, "literature" : 98, "science" : 97},
{"math" : 65, "literature" : 79, "science" : 85},92 CHAPTER 5 Files
{"math" : 78, "literature" : 83, "science" : 75},
{"math" : 92, "literature" : 78, "science" : 85},
{"math" : 100, "literature" : 80, "science" : 90}
]

The directory may also contain files for 10th grade (10a.json, 10b.json, and 10c.json)
and other grades and classes in the high school.

Each file contains the JSON equivalent of a list of dicts,
with each dict containing scores for several different school subjects.

NOTE Valid JSON uses double quotes ("), not single quotes (').
This can be surprising and frustrating for Python developers to discover.
Your function should print the highest, lowest, and average test scores for each subject in each class.

Given two files (9a.json and 9b.json) in the scores' directory, we would see the following output:

scores/9a.json
science: min 75, max 97, average 86.4
literature: min 78, max 98, average 83.6
math: min 65, max 100, average 85.0

scores/9b.json
science: min 35, max 95, average 82.0
literature: min 38, max 98, average 72.0
math: min 38, max 100, average 77.0

You can download a zipfile with these JSON files from http://mng.bz/Vg1x
"""