import os

root = "/home/kevinstevens/Documents/Development/My_Python_Journey"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            file_details = f.split(" - ")
            print(file_details)
        print("*" * 40)

    # print(directories)
    # print(files)
    # input()
    # for f in files:
    #     print("\t{}".format(f))
