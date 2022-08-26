while True:
    print("Please enter your image links, comma seperated!\n")
    images = input()
    images = images.split(",")

    for i in range(len(images)):
        link = "<img src=\"" + images[i] + "\" alt=\" \">"
        print(link)
