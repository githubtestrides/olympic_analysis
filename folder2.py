import numpy as np

def medals(df):

    new_df1 = df.drop_duplicates(
        subset=['NOC', 'region', 'Team', 'Games', 'Sport', 'Event', 'Medal', 'region', 'Year'])
    medals_tally=new_df1.groupby('region').sum()[['Bronze','Gold','Silver']].sort_values('Gold',ascending=False).astype(int)
    medals_tally['Total'] = medals_tally['Bronze'] + medals_tally['Gold'] + medals_tally['Silver']

    return medals_tally




def country_year(df):
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    year = df['Year'].unique().tolist()
    year.sort()
    year.insert(0,'Overall')
    return country,year


def detail(df,country,year):
    df= df.drop_duplicates(
        subset=['NOC', 'region', 'Team', 'Games', 'Sport', 'Event', 'Medal', 'region', 'Year'])
    temp_df = df
    if country == 'Overall' and year == 'Overall':
        temp_df = df
    if country == 'Overall' and year != 'Overall':
        temp_df = df[df['Year'] == int(year)]
    if country != 'Overall' and year == 'Overall':
        temp_df = df[df['region'] == country]
    if country != 'Overall' and year != 'Overall':
        temp_df=df[(df['region'] == country) & (df['Year'] == int(year))]
    medals = temp_df.groupby('region').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Gold',
                                                                                    ascending=False).astype(int).reset_index()
    return medals

def athlete(df,athlete):
    df= df.drop_duplicates(
        subset=['NOC', 'region', 'Team', 'Games', 'Sport', 'Event', 'Medal', 'region', 'Year'])
    temp_df = df
    if athlete == 'Overall':
        temp_df = df
    if athlete != 'Overall':
        temp_df = temp_df[temp_df['Name'] == athlete]
    x = temp_df.groupby('region').sum()[['Bronze', 'Gold', 'Silver']].sort_values('Gold',
                                                                                      ascending=False).astype(int).reset_index()

    return x


def name(df):
    athlete = df['Name'].unique().tolist()
    athlete.insert(0, 'Overall')

    return athlete




