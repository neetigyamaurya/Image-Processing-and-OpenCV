import easyocr

reader = easyocr.Reader(["en"])
result = reader.readtext(
    "W5G2.png",
    detail=0,
    decoder="wordbeamsearch",
)
print(result)
with open("files.txt", "w") as f:
    f.writelines(result)
for index, item in enumerate(result):
    print(f"{index}---->{item}")
