import matplotlib.pyplot as plt
import pandas as pd

def isNaN(num):
    return num != num

def price_corrector(column: pd.Series):
    df = column.to_frame('price')
    # df['euro_sign'] = df['price'].apply(lambda p: p[:1] if not isNaN(p) else None)
    df['price_float'] = df['price'].apply(lambda p: p[1:].replace(',','.') if not isNaN(p) else None)
    return df['price_float'].astype(float)

def moving_avg(column: pd.Series):
    pass

price_df = pd.read_csv('AGP_TSF_20240527_20241230.csv')
price_df['price'] = price_corrector(price_df['price'])
# price_df['price'] = price_df['price']
price_df['date'] = pd.to_datetime(price_df['date'])


plt.figure()
plt.scatter(price_df['date'], price_df['price'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

price_nextday_df = pd.read_csv('AGP_TSF_20240528_20241230.csv')
price_nextday_df['price'] = price_corrector(price_nextday_df['price'])
price_nextday_df['date'] = pd.to_datetime(price_nextday_df['date'])
price_nextday_df.rename(columns=dict([(col,col+'2') for col in price_nextday_df.columns if col != 'date']), inplace=True)

join_df = price_df.join(price_nextday_df.set_index('date'), on='date')[['date','price','price2']]
join_df.drop_duplicates(inplace=True).dropna(inplace=True)
join_df['price_diff'] = join_df['price2'] - join_df['price']

# plot_df = join_df[join_df.price_diff < 50]
plot_df = join_df
plt.figure()
plt.scatter(plot_df['date'], plot_df['price_diff'])
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

