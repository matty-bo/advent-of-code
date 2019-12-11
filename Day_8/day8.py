def get_layers(filename, picture_size):
    with open(filename) as file:
        data = file.read()
    layer_strings = []
    for i in range(0, len(data), picture_size):
        layer_strings.append(data[i:i + picture_size])
    return layer_strings

def ones_by_twos(layers):
    zero_layer = ''
    min_zero_count = -1
    for layer in layers:
        zero_count = 0
        for pixel in layer:
            if pixel == '0':
                zero_count += 1
        if zero_count <= min_zero_count or min_zero_count == -1:
            min_zero_count = zero_count
            zero_layer = layer
    count_ones = 0
    count_twos = 0
    for digit in zero_layer:
        if digit == '1':
            count_ones += 1
        if digit == '2':
            count_twos += 1
    return count_ones*count_twos

def image_bwt_pixels(layers, picture_size):
    pixels = []
    for j in range(0, picture_size):
        pixel = ""
        for i in range(0, len(layers)):
            pixel += layers[i][j]
        pixels.append(pixel)
    return pixels

def get_pixel_color(pixel):
    i = 0
    while pixel[i] not in ['0', '1'] and i < len(pixel):
        i += 1
    return pixel[i]

def part_rows_cols(image_string, width):
    image = []
    for i in range(0, len(image_string), width):
        image.append(image_string[i:i + width])
    return image

def print_decoded_image(layers, width, height):
    pic_size = width * height
    bwt_pixels = image_bwt_pixels(layers, pic_size)
    image = []
    for pixel in bwt_pixels:
        image.append(get_pixel_color(pixel))
    image = part_rows_cols(image, width)
    for row in image:
        print(' '.join(row))

width = 25
height = 6
pic_size = width * height
layers = get_layers("day8_data.txt", pic_size)
print(ones_by_twos(layers))
print_decoded_image(layers, width, height)