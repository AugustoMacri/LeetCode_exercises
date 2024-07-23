import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    
    #Trocar o tipo de dado de grade de float para int 

    students["grade"] = students["grade"].astype(int)


    return students

