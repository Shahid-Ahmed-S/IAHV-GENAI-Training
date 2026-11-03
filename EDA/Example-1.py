import pandas as pd

marks = [98,97,56,87,99,65]

pmarks = pd.Series(marks)
print("Declared..")
pmarks.to_csv('marks.csv')

newmarks = pd.read_csv('marks.csv')
print("Read File")
print(newmarks)
