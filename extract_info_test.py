from PIL import Image

image = Image.open('out.png')
pixel_map = image.load()

width = image.size[0]
height = image.size[1]

n_lsb = 2
count = 0
text_len = 16
binary_stream_length = text_len * 8
binary_stream = ""

def extract_information(r, g, b, count):
    global binary_stream
    # Storing binary values of R, G, B values in a list
    binary_value = [bin(item).replace("0b", "") for item in (r, g, b)]
    for bits in binary_value:
        binary_stream += bits[-n_lsb:]

def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

for i in range(width):
    for j in range(height):
        if count >= binary_stream_length / (3*n_lsb):
            break
        red, green, blue = pixel_map[i, j]
        extract_information(red, green, blue, count)
        count += 1


print(decode_binary_string(binary_stream))