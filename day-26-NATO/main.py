import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv")
data2={row.letter:row.code for index,row in data.iterrows()}
word=input("What is your word?: ")
output=[]
for char in word:
    output.append(data2[char.upper()])
print(output)