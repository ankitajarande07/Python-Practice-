username = 'admin'
password = '0000'

userid = input('Enter USERID:')
passw = input('enter PASSWORD:')

if(username == userid and password == passw):
    print('Logged in successful.')
else:
    print('Invalid credentials.')    