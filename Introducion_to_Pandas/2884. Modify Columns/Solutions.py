import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    employees["salary"] = employees["salary"] * 2

    return employees

data = {
    'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
    'salary': [25, 30, None, 40],
    'Cidade': ['New York', 'San Francisco', 'Los Angeles', None]
}

df = pd.DataFrame(data)

print(modifySalaryColumn(df))