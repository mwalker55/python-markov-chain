#Markov Chain Text Generator
##Introduction
Using a rudimentary "Markov chain" implementation, this program will generate random sentences based on a corpus of input sentences.
##Running
This program requires a file named "lines.txt", where every line is a sentence.  The program will then "learn" from these sentences and generate a random sentence.  This works best with a very large corpus; with a small one, the sentences may not make much of any sense or appear often.  

Assuming the lines.txt file is in the same directory as markov.py, simply run:
python markov.py

Running it will cause the output of a randomly generated sentence.