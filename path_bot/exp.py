import sys
from pathlib import Path
# mov ='E:\\Movies'
steam = 'C:\\Users\\box7\\Documents'
for i in Path(steam).iterdir():
    print(i.name)
# s_mov =set()
# s_steam =set()
# for i in Path(mov).iterdir():
#     for k in i.name:
#         s_mov.add(k)
#
# for i in Path(steam).iterdir():
#     for k in i.name:
#         s_steam.add(k)
# print(s_mov)
# print(s_mov-s_steam)
import random
s =''
import string
vars = list(string.ascii_letters+string.digits+'!#$%&()+,-.;=@[]^_`{}~')
for _ in range(70):
    s+=random.choice(vars)
print(s)