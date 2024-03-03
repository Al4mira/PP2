import os
#Ex1
def the_directories(path):
    directories = []
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            directories.append(i)
    return directories


def the_files(path):
    files = []
    for j in os.listdir(path):
        if os.path.isfile(os.path.join(path,j)):
            files.append(j)
    return files


def print_all(path):
    all = []
    for k in os.listdir(path):
        all.append(k)
    return all
        

path = " "

print("\n\tAll:")
print(*print_all(path),sep='\n')

print("\tDirectories:")
print(*the_directories(path),sep='\n')

print("\n\tFiles:")
print(*the_files(path),sep='\n')



#Ex2

def path_checking(path):
    if os.path.exists(path):
        print("Path exists")
    else:
        print("This path doesn't exists")


    if os.access(path, os.R_OK):
        print("This path is readable")
    else:
        print("This path is not readable") 


    if os.access(path, os.W_OK):
        print("This path is writable")
    else:
        print("This path is not writable")

    
    if os.access(path, os.X_OK):
        print("Thin path is executable")
    else:
        print("This path is not executable")

path = "C:\\"
path_checking(path)


#Ex3

def path_existance(path):
    if not os.path.exists(path):
        print("This path doesn't exists")
    else:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)

path = "C:\\"
path_existance(path)


#Ex4
def count_the_lines(myfile):
    count=0
    with open(myfile, "r") as file:
        for i in file:
            count+=1
    print("Number of lines in the file: ", count)


#Ex5
def unloved(mylist):
    with open("my.txt", "w") as file:
        for i in mylist:
            file.write(str(i)+"\n ")
   
songs = ["strange affect", "When a woman is around", "lee", "bill"]  
unloved(songs)

#Ex6
def txt_generator():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
    for i in alphabet:
        filename= i + ".txt"
        with open(filename, "w") as file:
            file.write(i)
        print("The file been created: ")

txt_generator()


#Ex7
def copycat():
    take_out = "first.txt"
    trans_to = "copy.txt"
    with open(take_out, "r") as file:
        content = file.read()
    with open(trans_to, "w") as file:
        file.write(content)

copycat()


#Ex8
def file_delete(path):
    if os.access(path, os.F_OK):
        if os.access(path, os.W_OK):
            os_remove(path)
            print("Your path is deleted")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")
        
path = "lyrics.txt"
file_delete(path)





