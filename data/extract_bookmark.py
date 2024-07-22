file = "./bookmarks.html"


with open(file, "r") as f:
    content = f.read()


pattern = '<DT><A HREF="'
lines = content.split(pattern)


lines = lines[1:]

lines = [txt.split('"')[0] for txt in lines]


find = (
    lambda i: ("boitea" in i)
    or ("ultimate" in i)
    or ("chordify" in i)
    or ("chordu" in i)
)

lines = list(filter(find, lines))


for i in lines[:10]:
    print(i)


with open("bookmarks.csv", "w") as f:

    lines = ["web,"] + lines
    f.writelines("\n".join(lines))
