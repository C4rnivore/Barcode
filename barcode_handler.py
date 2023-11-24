from tables import b_codes, control_sum
from barcode import gen

def handle_input(input):
    check_symbol = get_check_symbol()
    bits_flow = to_bits(input)
    gen(bits_flow, check_symbol)

def to_bits(input:str):
    flow =''
    chars = list(input)
    for char in chars:
        flow += b_codes[char]
    return flow

def get_check_symbol():
    sum = 104 # Start Code B
    counter = 1
    chars = list(input)

    for char in chars:
        sum+=control_sum[char] * counter
        counter += 1

    index = sum % 103
    res = ''
    for k,v in control_sum.items():
        if v == index:
            res = k
    print(res)
    return res

if __name__ == '__main__':

    input = "Hello, world!"
    handle_input(input)