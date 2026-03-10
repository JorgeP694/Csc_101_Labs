from group import *
from data import *

'''
input: filename
output: header object and a pixel list
purpose: read a file and then split to take a header and a list of pixels
'''
def read_ppm_file(filename: str) -> tuple[Header, list[Pixel]]:
    with open(filename, 'r') as f:
        file_text = f.read()
        newfile = file_text.split()

        # newfile looks like: ['P3', width, height, max_color, r, g, b, r, g, b, ...]
        header_parts = newfile[1:4]
        width = int(header_parts[0])
        height = int(header_parts[1])
        max_color = int(header_parts[2])
        header_obj = Header(width, height, max_color)

        data = [int(x) for x in newfile[4:]]
        pixel_list: list[Pixel] = []


        for sublist in group_of_3(data):
            red = sublist[0]
            green = sublist[1]
            blue = sublist[2]
            pixel_list.append(Pixel(red, green, blue))

        return header_obj, pixel_list


'''
input: list of pixels
output: new list of pixels objects
purpose: multiply red by 10, then clamp to 255, then set green/blue to same value
'''
def process_data(pixel_list: list[Pixel]) -> list[Pixel]:
    new_list: list[Pixel] = []
    for px in pixel_list:
        new_val = px.red * 10
        if new_val > 255:
            new_val = 255
        new_list.append(Pixel(new_val, new_val, new_val))
    return new_list


'''
input: header object and list of pixels
output: writes a new ppm file
purpose: create a new file that has the header and the new list of pixels
'''
def create_ppm_file(header: Header, pixels: list[Pixel], out_filename: str = 'discovered.ppm') -> None:
    with open(out_filename, 'w') as f:
        f.write("P3\n")
        f.write(f"{header.width} {header.height}\n")
        f.write(f"{header.max_color}\n")


        for px in pixels:
            f.write(f"{px.red} {px.green} {px.blue}\n")


if __name__ == '__main__':
    header, pixels = read_ppm_file('hidden.ppm')
    print(header)
    print(pixels[:4])

    processed_pixels = process_data(pixels)
    create_ppm_file(header, processed_pixels)

