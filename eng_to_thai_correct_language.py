def correct_language(input_string):
  char_map = {
    'q': 'ๆ',
    'w': 'ไ',
    'e': 'ำ',
    'r': 'พ',
    't': 'ะ',
    'y': 'ั',
    'u': 'ี',
    'i': 'ร',
    'o': 'น',
    'p': 'ย',
    '[': 'บ',
    ']': 'ล',
    'a': 'ฟ',
    's': 'ห',
    'd': 'ก',
    'f': 'ด',
    'g': 'เ',
    'h': '้',
    'j': '่',
    'k': 'า',
    'l': 'ส',
    ';': 'ว',
    "'": 'ง',
    "\\": 'ฃ',
    'z': 'ผ',
    'x': 'ป',
    'c': 'แ',
    'v': 'อ',
    'b': 'ิ',
    'n': 'ื',
    'm': 'ท',
    ',': 'ม',
    '.': 'ใ',
    '/': 'ฝ',
    '1': 'ๅ',
    '2': '/',
    '3': '-',
    '4': 'ภ',
    '5': 'ถ',
    '6': 'ุ',
    '7': 'ึ',
    '8': 'ค',
    '9': 'ต',
    '0': 'จ',
    '-': 'ข',
    '=': 'ช'
  }

  output_string = ""

  for char in input_string:
    output_string += char_map.get(char, char)

  return output_string

prompt = input("prompt: ")
print(correct_language(prompt))  
