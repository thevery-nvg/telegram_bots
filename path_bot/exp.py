import sys
from pathlib import Path
o='D:\\Steam'

for i in Path(o).iterdir():

    print(i.suffix)