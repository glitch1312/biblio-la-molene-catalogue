#!/usr/bin/expect
spawn git push
expect "Username for 'https://github.com':"
send -- "glitch1312\r"
expect "Password for 'https://glitch1312@github.com':"
send -- "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\r"
expect eof
#token="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"
#{ echo "$token" ; echo "glitch1312" ;} | git push https://github.com/glitch1312/biblio-la-molene-catalogue
