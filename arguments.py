import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write('new file created')

else:
    print(f"ERROR the file {filename} already exists")
    sys.exit(1)
