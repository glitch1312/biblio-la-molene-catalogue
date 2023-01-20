#!/bin/sh

# call the python script to update the folders with .md file for each book
python update_books.py

# push the new .md files in the github repository 
token = "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"
$token | glitch1312 | git push https://github.com/glitch1312/biblio-la-molene-catalogue 
#Username: <my-username>
#Password: <my-personal-access-token>

