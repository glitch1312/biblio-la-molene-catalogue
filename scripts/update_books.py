
'''
Header
Auteur : Amina Matt
Date de creation : 16.01.2023
Date de derniere modification: 13.12.2023
Version : Python 3.8
Description: Creer les objects d'une collection (books) en format  .md avec le format requis. Une boucle sur les objets pour remplir un tableau ([Datatable](https://www.datatables.net))
'''

# import

import os
import pandas as pd
import sys
import io

# initialization
PATH = sys.argv[1]
GENERATED_DATA = PATH+'_books/'
CATALOG = PATH+'data/catalogue_molene.csv'
print('Initialization done')
# load
raw_data = pd.read_csv(CATALOG, encoding = 'utf8')
print('---------------')
print('Raw data loaded')
print(raw_data.head())


column_list = raw_data.columns
dataframe = raw_data.rename(columns={
    column_list[0]: 'Titre',
    column_list[1]: 'Prenom',
    column_list[2]: u'Catégorie',
    column_list[3]: u'Nouvelles catégories',
    column_list[4]: 'Langues',
    column_list[5]: 'ID',
    column_list[6]: u'Créé le',
    column_list[7]: u'Modifié le',
    column_list[8]: 'Nom'})

print('---------------')
print('Clean dataframe head')
print(dataframe.head())

# clean
dataframe = dataframe.drop(columns = [column_list[3],column_list[4],column_list[5],column_list[6],column_list[7]])
nan_value = float("NaN")
dataframe.replace( nan_value, "", inplace=True)

# lower case
dataframe['Nom'] = dataframe['Nom'].apply(lambda x: x.title())

dataframe['Prenom'] = dataframe['Prenom'].apply(lambda x: x.lower())
dataframe['Prenom'] = dataframe['Prenom'].apply(lambda x: x.title())

# #escape special character
# dataframe['Prenom'] = dataframe['Prenom'].apply(lambda x: x.replace('\'', '\\\''))
# dataframe['Nom'] = dataframe['Nom'].apply(lambda x: x.replace('\'', '\\\''))
# dataframe['Titre'] = dataframe['Titre'].apply(lambda x: x.replace('\'', ' "\\\'" '))
# dataframe['Categorie'] = dataframe['Categorie'].apply(lambda x: x.replace('\'', '\\\''))

# writing
print('Writing markdown files in $f')
n = len(dataframe)
for i in range(n) :

    filename = str(i)+'.md'
    try :
        f = io.open(GENERATED_DATA+filename, "w", encoding='utf8')
    except IOError:
        f = io.open(GENERATED_DATA+filename, "w", encoding='utf8')

        #row of interest
    df = dataframe.iloc[i]

    # front matter markdown with
    f.write(u'---\n')
    f.write(u'Nom:  \"'+df['Nom']+'\"\n')
    f.write(u'Prenom: \"'+ df['Prenom']+'\"\n')
    f.write(u'Titre: \"'+ df['Titre']+'\"\n')
    f.write(u'Catégorie: \"'+df[u'Catégorie']+'\"\n')
    f.write(u'---')

    f.close()
