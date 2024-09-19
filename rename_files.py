import os


for file in os.listdir("."):
    if file.endswith(".gif"):
        print(file)

