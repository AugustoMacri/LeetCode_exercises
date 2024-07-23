import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
    # Deve ser criado uma nova coluna nomeada bonus, essa coluna deve ser o dobro do valor existente em salary

    employees['bonus'] = employees['salary']* 2

    return employees