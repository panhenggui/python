with open("test.txt","wt") as outfile:
    outfile.write("该文本会写入到文件中\n看到我了吧！")

with open("test.txt","rt") as infile:
    text = infile.read()
print(text)