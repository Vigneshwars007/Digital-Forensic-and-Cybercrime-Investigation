jpeg_signature = b"\xff\xd8\xff"
image = "disk.img"

with open(image, "rb") as f:
    data = f.read()

index = data.find(jpeg_signature)

if index != -1:
    with open("recovered_image.jpg", "wb") as out:
        out.write(data[index:])
    print("JPEG signature found at byte:", index)
    print("Recovered file saved as recovered_image.jpg")
else:
    print("No JPEG signature found.")
