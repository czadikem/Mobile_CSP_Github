
Sign up for an account at 

https://dashboard.ngrok.com/user/signup

Download and install you auth token

./ngrok authtoken XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Run a ngrok server

 ~/bin/ngrok http 80

If you go for a paid subscription you can then use a named subdomain

 ~/bin/ngrok -subdomain=XXXXXXXXXX http 80

