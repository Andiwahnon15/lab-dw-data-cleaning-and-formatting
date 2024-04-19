def load_data(url='https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv'):
    import pandas as pd
    df = pd.read_csv(url)

    df.columns = df.columns.str.lower().str.replace(" ","_")

    df=df.rename(columns = {
    "st": "state"
    })
    return df