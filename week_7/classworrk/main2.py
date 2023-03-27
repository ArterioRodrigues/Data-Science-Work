from sklearn import datasets

digits = datasets.load_digits()
df = []

for index, val in enumerate(digits.data):
    if digits.target[index] == 0 or digits.target[index] == 1:
        df.append(val)

print(df)


