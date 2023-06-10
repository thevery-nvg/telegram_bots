import sys
from pathlib import Path
# mov ='E:\\Movies'
steam = "D:\\Steam\\crashhandler.dll"
s= "К"
print(sys.getsizeof(Path(steam).name))
print(sys.getsizeof(s))
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


