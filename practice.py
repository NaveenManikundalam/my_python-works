from PIL import Image

image = Image.open("RCB.jpg")

print(f"Current size : {image.size}")

resize_image = image.resize((500,500))

resize_image.save("RCB_resized.jpg")

image2 = Image.open("RCB_resized.jpg")
print(f"Size of resized image is {image2.size}")