import pandas as pd

people = {
    "first": ["joe", "Lau", "john"],
    "last": ["carter", "silv", "tovar"],
    "email": ["joe@gmail.com", "lau@gmai.com", "tovar@gmail.com"]
}

print(f'{"="*10} data frame {"="*10}')
df = pd.DataFrame(people)
print(df)


print(f'{"="*10} email info {"="*10}')
print(df["email"])


print(f'{"="*10} display two columns {"="*10}')
print(df[["last", "email"]])


print(f'{"="*10} print all columns {"="*10}')
print(df.columns)

print(f'{"="*10} print an specific row{"="*10}')
print(df.iloc[0])

print(df.shape)