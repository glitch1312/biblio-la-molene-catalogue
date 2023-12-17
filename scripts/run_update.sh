#!/usr/bin/expect
#read file with token
set f [open ./token-push.txt r]
set token [read -nonewline $f]
close $f

spawn git push
expect "Username for 'https://github.com':"
send -- "glitch1312\r"
expect "Password for 'https://glitch1312@github.com':"
send -- "$token\r"
expect eof
