import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    
    report = report.melt(id_vars='product', var_name='quarter', value_name='sales')

    return report


data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

df = pd.DataFrame(data)

print(meltTable(df))