import random
from passlib.hash import pbkdf2_sha256 as hasher

mylist = ['cordoba', 'riad', 'madrid', 'sharma', 1970, 2003, 2006, '#', '_', '@',]

password_list = random.choices(mylist, k=8)

print(password_list)

password = ''

for i in range(len(password_list)):
    password = password + str(password_list[i])

p1 = 'sharma_@sharma@2003sharma2003'
p2 = '197020032006cordobasharmariad#2006'
p3 = 'madrid_@#2006@cordoba_'
p4 = '_2006@sharma1970riad#2006'
p5 = 'sharma#20031970##madridsharma'

p = [p1, p2, p3, p4, p5]
"""
>>> from passlib.hash import pbkdf2_sha256 as hasher
>>> password = "marmota_0"
>>> hashed = hasher.hash(password)
>>> hashed
'$pbkdf2-sha256$29000$4xxjrNW619o7RyhFSImRMg$SpjTdfULtKtAek7STRgoW0zoZcYHcVTyBdhWx8dx7MQ'
>>> exit()

"""
hashed = hasher.hash(p5)
print(hashed)
    

