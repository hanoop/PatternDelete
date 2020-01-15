import os, sys
import tqdm

if len (sys.argv) != 3 :
    print ("Usage: python deleteFile.py <root_dir> <keyword>")
    sys.exit (1)
file_list=[]
path = str(sys.argv[1])
keyword = str(sys.argv[2])

for r,d,f in os.walk(path):
    for file in f:
        if(keyword in file):
            file_list.append(os.path.join(r,file))

for i in file_list:
    print(i)


if(str.lower(input("Press Y to delete identified files: "))=='y'):
    for i in tqdm(file_list):
          try:
            os.remove(i)
            print("Deleted ",i)
        except Exception as e:
            print(e)
        