import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    #Precisa apagar apenas o que tem None em uma específica
    students = students.dropna(subset="name")
    return students

data = {
    'Nome': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Idade': [25, 30, 25, 35, 30],
    'Cidade': ['New York', 'San Francisco', None, 'Los Angeles', 'San Francisco']
}

df = pd.DataFrame(data)

print(dropMissingData(df))