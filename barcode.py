from PIL import Image, ImageColor
from tables import b_codes
import re

TYPE = 'B'
START_SYMBOL = '11010010000'
STOP_SYMBOL = '1100011101011'
EMPTY = '00000000000'

HEIGHT = 50
PADDING = 0

MODULE_WIDTH = 1

def gen(bits_flow, check_symbol):
    width = get_canvas_width(len(bits_flow)) + PADDING * 2 
    height = HEIGHT + PADDING * 2
    br = Image.new('P',(width,height), 'white')
    
    total_data  = EMPTY + START_SYMBOL + bits_flow
    blocks = re.findall('...........',total_data)
    blocks.append(b_codes[check_symbol])
    blocks.append(STOP_SYMBOL)
    blocks.append(EMPTY)

    draw(br, blocks)

    br.save('Barcode.png')


def get_canvas_width(flow_len):
    return len(STOP_SYMBOL) + len(START_SYMBOL) + len(EMPTY*2) + flow_len + 11

def draw(canvas:Image, data_blocks):
    x_counter = PADDING

    for block in data_blocks:
        for char in block:
            for y in range(PADDING, PADDING+HEIGHT):
                if char == '0':
                    canvas.putpixel((x_counter,y), ImageColor.getcolor('white', 'P'))
                else:
                    canvas.putpixel((x_counter,y), ImageColor.getcolor('black', 'P'))
            x_counter += 1

