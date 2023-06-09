from pathlib import Path
mov ='E:\\Movies'
steam = "D:\\Steam"
s_mov =set()
s_steam =set()
for i in Path(mov).iterdir():
    for k in i.name:
        s_mov.add(k)

for i in Path(steam).iterdir():
    for k in i.name:
        s_steam.add(k)
print(s_mov)
print(s_mov-s_steam)
