#23 Write a program to compute the frequency of the words from the input.
#Enrollment no:92400527202
text = input("enter sentence: ")

words = text.split()
freq = {}

for w in words:
    w = w.strip(".,").capitalize()
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
for key in sorted(freq):
    print(key, ":", freq[key])
