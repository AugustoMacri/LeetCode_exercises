import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:

    return customers.drop_duplicates(subset=['email'])



data = {
    'Nome': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Idade': [25, 30, 25, 35, 30],
    'email': ['New York', 'San Francisco', 'New York', 'Los Angeles', 'San Francisco']
}

df = pd.DataFrame(data)

print(dropDuplicateEmails(df))