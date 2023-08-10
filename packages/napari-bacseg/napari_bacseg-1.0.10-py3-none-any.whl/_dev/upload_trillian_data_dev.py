


import pandas as pd
from csv import Sniffer

user_metadata_path = r"C:\Users\turnerp\Desktop\BacSeg_Database\Images\PT\PT_file_metadata.txt"


sniffer = Sniffer()

print(user_metadata_path)

# checks the delimiter of the metadata file

with open(user_metadata_path) as f:
    line = next(f).strip()
    delim = sniffer.sniff(line)
    print(delim)

    

# df = pd.read_csv(user_metadata_path, sep=",")