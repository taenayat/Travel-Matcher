import matplotlib.pyplot as plt
import pandas as pd

def isNaN(num):
    return num != num

def price_corrector(column: pd.Series):
    df = column.to_frame('price')
    # df['euro_sign'] = df['price'].apply(lambda p: p[:1] if not isNaN(p) else None)
    df['price_float'] = df['price'].apply(lambda p: p[1:].replace(',','.') if not isNaN(p) else None)
    return df['price_float']

def moving_avg(column: pd.Series):
    pass

price_df = pd.read_csv('MAD_TSF_20240226_20241230.csv')
price_df['price'] = price_corrector(price_df['price'])
price_df['price'] = price_df['price'].astype(float)
price_df['date'] = pd.to_datetime(price_df['date'])


plt.figure()
plt.scatter(price_df['date'], price_df['price'])
plt.xticks(rotation=45, ha='right')
plt.show()


