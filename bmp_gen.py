import binascii


def main():
    with open('file.bmp', 'wb') as opened_file:
        write_bmp_header(opened_file)
        write_dib_header(opened_file)
        write_pixel_data(opened_file)


def write_bmp_header(file):
    file_type = ['42', '4D']
    file_size = ['4E', '00', '00', '00']
    reserved_bytes = ['00', '00', '00', '00']
    pixel_data_offset = ['36', '00', '00', '00']

    bmp_header = [file_type, file_size, reserved_bytes, pixel_data_offset]

    for item in bmp_header:
        write_hex_data(file, item)


def write_dib_header(file):
    header_size = ['28', '00', '00', '00']
    image_width = ['04', '00', '00', '00']
    image_height = ['02', '00', '00', '00']
    color_planes = ['01', '00']
    bits_per_pixel = ['18', '00']
    compression = ['00', '00', '00', '00']
    image_size = ['18', '00', '00', '00']
    x_pixels_per_m = ['00', '00', '00', '00']
    y_pixels_per_m = ['00', '00', '00', '00']
    total_colors = ['00', '00', '00', '00']
    important_colors = ['00', '00', '00', '00']

    dib_header = [header_size, image_width, image_height, color_planes,
                  bits_per_pixel, compression, image_size, x_pixels_per_m,
                  y_pixels_per_m, total_colors, important_colors]

    for item in dib_header:
        write_hex_data(file, item)


def write_pixel_data(file):
    pixel_array = ['FF', 'FF', '00', 'FF', '00', 'FF', '00', 'FF', 'FF',
                   '00', '00', '00', '00', '00', 'FF', 'FF', '00', '00',
                   'FF', 'FF', 'FF']
    write_hex_data(file, pixel_array)


def write_hex_data(file, hexlist):
    for item in hexlist:
        file.write(binascii.unhexlify(item))


if __name__ == "__main__":
    main()
