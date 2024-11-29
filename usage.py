from dam_mockdata_genrator import get_country_level_df

df = get_country_level_df(no_of_countries=10,start_year=2023,no_of_years=8,total_achieved=100000,
                          distribution_type='linear',no_of_sub_categories=4)

df.to_csv('data.csv',index=False) 