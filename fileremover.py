import os

cwd = os.getcwd()

print('current working dir is ' + cwd)
print("please provide new path: ")
newcwd = input()

if cwd != newcwd:
    os.chdir(newcwd)
    print("direcotry changed to: " + newcwd)

for filename in os.listdir():
    if filename.endswith('.txt'):
        print(filename)


print('Please approve listed file removal ')
x = input()
if x == 'yes':
    for filename in os.listdir():
        if filename.endswith('.txt'):
            os.unlink(filename) 
else:
    print('Files were not removed')
    

