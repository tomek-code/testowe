numbers = ["Nick", 2, 3, 4, "test"]

for item in numbers:
    print("the person name is ", item)


run = True
current = 1

while run:
    if current == 100:
        run = False

    else:
        print(current)
        current += 1    
