import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    
    #Na quantity, substituir o que falta por 0

    products['quantity'] = products['quantity'].fillna(0)
    
    return products