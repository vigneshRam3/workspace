import json, os, sys

filepath = input('Folder Path: ')
prefix = input('Input File Base Name: ')
final_name = input('Output File Base Name: ')
max_size = int(input('Max File Size: '))
final = {}

files = [i for i in os.listdir(filepath) if os.path.isfile(os.path.join(filepath,i)) and \
         prefix in i]
for i in files:
    with open(filepath + i, 'r') as json_file:
        obj = dict(json.load(json_file))
        if not final.items():
            final = obj.copy()
        else:
            final[list(final.keys())[0]].extend(obj[list(obj.keys())[0]])
            # for finding the rootkey of the list of objects dynamically
rootkey = str(list(final.keys())[0])

#writes the obtained objects in a single file
# json.dump(final, open('all_objects_merged.json', 'w+'))

#to write the objects into seperate files with max_size
file_iter = 1
list_size = len(final[rootkey])
template = "{\"" + str(rootkey) + "\": []" + "}"

with open(final_name + str(file_iter) + '.json', 'w+') as fp:
    fp.write(template)

for i in range(list_size):
    temp = ''
    fsize = os.stat(final_name + str(file_iter) + '.json').st_size #current file's size
    isize = len(str(final[rootkey][i]).encode('utf-8')) #size of the text to be written (current list item)
    if not (fsize + isize) < max_size:
        file_iter += 1
        with open(final_name + str(file_iter) + '.json', 'w+') as fp:
            fp.write(template)

    with open(final_name + str(file_iter) + '.json', 'r') as fp:
        temp = fp.read()

    with open(final_name + str(file_iter) + '.json', 'w+') as fp:
        temp = json.loads(temp)
        temp[rootkey].append(final[rootkey][i])
        json.dump(temp, fp)
