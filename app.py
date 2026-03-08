from functions import soundToMedianFrequency, possibleRange, soundToSustainedFrequency, possibleRangeForMedian, recording



# RECORD NOTE 

print("Hum your highest note: ")
highestSound = recording()

print("Hum your lowest note: ")
lowestSound = recording()

print("Shout 'Hey' 3 times as if you were calling a person from afar: ")
sustainedSound = recording()

print("Analyzing your vocal range ... ")

highestNote = soundToMedianFrequency(highestSound)
lowestNote = soundToMedianFrequency(lowestSound)

possibilities = possibleRange(highestNote, lowestNote)

sustainedNote = soundToSustainedFrequency(sustainedSound)
print("Your vocal range is likely: ")
print(possibleRangeForMedian(possibilities, sustainedNote))




