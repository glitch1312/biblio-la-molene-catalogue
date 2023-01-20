#!/bin/sh

# call the python script to update the folders with .md file for each book
python update_books.py

# push the new .md files in the github repository

token="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"
git push https://github.com/glitch1312/biblio-la-molene-catalogue


git push https://glitch1312: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@github.com/glitch1312/biblio-la-molene-catalogue --all
