string=input("Enter a color")
colors = ["red", "green", "blue", "purple"]
for i in range(len(colors)):
    if (string==colors[i]):
        print("Matched")
        break
    else:
        print("Not Matched")


