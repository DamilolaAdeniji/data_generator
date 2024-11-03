from dam_mockdata_genrator import get_country_level_df

df = get_country_level_df(3,2023,6,1120000,'linear',3)

df.to_csv('TZ_data.csv',index=False)