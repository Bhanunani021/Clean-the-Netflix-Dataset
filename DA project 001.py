import pandas as pd
doc = pd.read_csv("netflix_titles.csv")
#print(doc.info)
#print(doc.describe(include= "all"))

doc[['director', 'cast', 'country']] = doc[['director', 'cast', 'country']].fillna('Unknown')
doc[['rating']] = doc[['rating']].fillna('Unknown')
doc['duration'] = doc['duration'].replace('Unknown', pd.NA)
doc['date_added'] = doc['date_added'].replace('Unknown', pd.NA)

doc['duration_value'] = doc['duration'].str.extract(r'(\d+)').astype(float)
doc['duration_unit'] = doc['duration'].str.extract(r'([a-zA-Z]+)')

doc['date_added'] = pd.to_datetime(doc['date_added'], errors='coerce')

doc = doc.drop(columns=['duration'])

doc.to_csv('netflix_titles_cleaned.csv', index=False)

print(doc.isnull().sum())

print(doc.info)