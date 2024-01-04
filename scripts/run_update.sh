#!/usr/bin/expect
#read file with token
set f [open ./token-push.txt r]
set token [read -nonewline $f]
close $f

set f [open ./path.txt r]
set path [read -nonewline $f]
close $f

spawn python3 update_books.py $path 
spawn git add -A ../_books/*
spawn git commit -m 'catalogue update'
spawn git status
spawn git push
expect "Username for 'https://github.com':"
send -- "glitch1312\r"
expect "Password for 'https://glitch1312@github.com':"
send -- "$token\r"
expect eof
spawn echo "Mise à jour effectuée"