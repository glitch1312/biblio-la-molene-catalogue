'''
Header
Auteur : Amina Matt
Date de création : 16.01.2023
Date de dernière modification: 16.01.2023
Version : Python 3.8
Description: Créer les objects d'une collection (books) en format  .md avec le format requis. Une boucle sur les objets pour remplir un tableau ([Datatable](https://www.datatables.net))
'''

# import
import os
import pandas as pd


# initialization
PATH = '/Users/aminamatt/Desktop/biblio-la-molene-catalogue/'
GENERATED_DATA = PATH+'_books/'
CATALOG = PATH+'catalogue_en_ligne.csv'
print('Initialization done')
# load
raw_data = pd.read_csv(CATALOG, encoding = 'utf8')
print('---------------')
print('Raw data loaded')
print(raw_data.head())


column_list = raw_data.columns
dataframe = raw_data.rename(columns={
    column_list[0]: 'Nom',
    column_list[1]: 'Prenom',
    column_list[2]: 'Titre',
    column_list[3]: 'Categorie'})

print('---------------')
print('Clean dataframe head')
print(dataframe.head())

# clean
dataframe = dataframe.drop(columns = [column_list[4],column_list[6],column_list[7],column_list[8]])
nan_value = float("NaN")
dataframe.replace( nan_value, "", inplace=True)
# lower case
dataframe['Nom'] = dataframe['Nom'].apply(lambda x: x.lower())
dataframe['Nom'] = dataframe['Nom'].apply(lambda x: x.title())

dataframe['Prenom'] = dataframe['Prenom'].apply(lambda x: x.lower())
dataframe['Prenom'] = dataframe['Prenom'].apply(lambda x: x.title())

# writing
print('Writing markdown files')
n = len(dataframe)
for i in range(n) :

    filename = str(i)+'.md'
    try :
        f = open(GENERATED_DATA+filename, "x", encoding='utf8')
    except IOError:
        f = open(GENERATED_DATA+filename, "w", encoding='utf8')

        #row of interest
    df = dataframe.iloc[i]

    # front matter markdown with
    f.write('---\n')
    f.write('Nom:  \''+df['Nom']+'\'\n')
    f.write('Prenom: \''+ df['Prenom']+'\'\n')
    f.write('Titre: \''+ df['Titre']+'\'\n')
    f.write('Categorie: \''+df['Categorie']+'\'\n')
    f.write('---')

    f.close()
