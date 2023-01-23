import pandas as pd



def sort_df():
    df = pd.read_csv('athlete_events.csv')
    region = pd.read_csv('noc_regions (1).csv')

    df = region.merge(df, on='NOC')
    df = df[df['Season'] == 'Summer']
    pd.get_dummies(df['Medal'])
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df
def fig(df):
    top5 = df['region'].value_counts().reset_index().head()
    top5.rename(columns={'index': 'country', 'region': 'count'}, inplace=True)
    return top5





