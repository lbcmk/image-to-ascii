from PIL import Image

brightness_values = "`.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

input_file = input("File Name (not path): ")
width = int(input("Width: "))
height = int(input("Height: "))

im = Image.open(f"./{input_file}")
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))
rgb_im = rgb_im.resize((width, height))

for i in range(height):
    for j in range(width):
        average = (rgb_im.getpixel((j, i))[0] + rgb_im.getpixel((j, i))[1] + rgb_im.getpixel((j, i))[2])/3
        print(brightness_values[(int(average*len(brightness_values)/256))], end="")
    print("")