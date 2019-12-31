# Air_Quality_Check


-------------------------------------------------------------------
checks air quality from airnow.gov (currently set to sacramento,ca)
if air quality is 101(unsafe for sensitive groups) or above
sends email to user.
-------------------------------------------------------------------
CONFIG- if you wish to use this.
-------------------------------------------------------------------
delete or add file named emailconfig

currently uses gmail
less secure app access must be on for your email account.
can be found under Security in Account Settings.


if you delete the import emailconfig besure to change emailconfig.email_user and emailconfig.email_pass to email_user and email_pass down on line 42

in the email function 

add to line 26 or above
gmail_user = 'your email'
gmail_pass = 'your password'


