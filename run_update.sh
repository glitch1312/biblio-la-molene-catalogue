#!/usr/bin/expect
#{ echo "git add _books/*";}
#{ echo "git commit -m \"Updating the catalogue\"";}
spawn git push
expect "Username for 'https://github.com':"
send -- "glitch1312\r"
expect "Password for 'https://glitch1312@github.com':"
send -- "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\r"
expect eof
#token="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"
#{ echo "$token" ; echo "glitch1312" ;} | git push https://github.com/glitch1312/biblio-la-molene-catalogue
