import hashlib # used to be md5 in python2

flag = 0 # zero value means no password found yet

# replace password with any password to get the md5 hash
#print(hashlib.md5("password".encode('utf-8')).hexdigest())

pass_hash = raw_input('Enter md5 hash: ')
word_list = raw_input('File name: ')

try:
    pass_file = open(word_list, 'r')
except:
    print('No file found')
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    print(word)
    print(digest)
    print(pass_hash)

    if digest == pass_hash:
        print('Password has been found')
        print('password is ' + word)
        flag = 1
        break

if flag == 0:
    print('password is not in the list')