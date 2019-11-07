import json, sys, os

Path = input('Enter the folder path: ')
BaseName = input('Enter the Input File Base Name Of The File: ')
RetrievalName = input('Enter the Output File Base Name Of The File: ')
maxSize = int(input('Enter the Maximum File Size: '))
files = [i for i in os.listdir(Path) if os.path.isfile(os.path.join(Path,i)) and \
         BaseName in i]
Final = {}
for i in files:
    with open(Path + i, 'r') as json_file:
        obj = dict(json.load(json_file))
        if not Final.items():
            Final = obj.copy()
        else:
            Final[list(Final.keys())[0]].extend(obj[list(obj.keys())[0]])
           
rootkey = str(list(Final.keys())[0])
itr = 1
lstSize = len(Final[rootkey])
template = "{\"" + str(rootkey) + "\": []" + "}"

with open(RetrievalName + str(itr) + '.json', 'w+') as fp:
    fp.write(template)

for i in range(lstSize):
    temp = ''
    fsize = os.stat(RetrievalName + str(itr) + '.json').st_size 
    isize = len(str(Final[rootkey][i]).encode('utf-8')) 
    if not (fsize + isize) < maxSize:
        itr += 1
        with open(RetrievalName + str(itr) + '.json', 'w+') as fp:
            fptr.write(template)

    with open(RetrievalName + str(itr) + '.json', 'r') as fp:
        temp = fp.read()

    with open(RetrievalName + str(itr) + '.json', 'w+') as fp:
        temp = json.loads(temp)
        temp[rootkey].append(Final[rootkey][i])
        json.dump(temp, fp)
