import random

line_starters = []
line_enders = []
word_combos = {}

def buildDictionaryFromFile():
    file = open("lines.txt", "r")
    for line in file:
        line = line.rstrip("\n")
        wordsInLine = line.split(" ")
        line_starters.append(wordsInLine[0])
        line_enders.append(wordsInLine[-1])
        index = 0
        for word in wordsInLine:
            word_combos.setdefault(word, [])
            if index != len(wordsInLine)-1:
                word_combos[word].append(wordsInLine[index+1])
            index+=1
    return

def generateRandomSentence():
    min_length = 15
    first_word = line_starters[random.randint(0, len(line_starters)-1)]
    sequence = first_word
    choice = word_combos[first_word][random.randint(0, len(word_combos[first_word])-1)]
    while choice not in line_enders:
        sequence+= " " + choice
        choice = word_combos[sequence.split(" ")[-1]][random.randint(0, len(word_combos[sequence.split(" ")[-1]])-1)]
    return sequence

buildDictionaryFromFile()
print generateRandomSentence()



