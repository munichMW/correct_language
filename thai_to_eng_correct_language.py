prompt = input("prompt: ")
print(correct_language(prompt)) 


def correct_language(input_string):
  char_map = {
    'ๆ': 'q',
    'ไ': 'w',
    'ำ': 'e',
    'พ': 'r',
    'ะ': 't',
    'ั': 'y',
    'ี': 'u',
    'ร': 'i',
    'น': 'o',
    'ย': 'p',
    'บ': '[',
    'ล': ']',
    'ฟ': 'a',
    'ห': 's',
    'ก': 'd',
    'ด': 'f',
    'เ': 'g',
    '้': 'h',
    '่': 'j',
    'า': 'k',
    'ส': 'l',
    'ว': ';',
    'ง': "'",
    'ฃ': "\\",
    'ผ': 'z',
    'ป': 'x',
    'แ': 'c',
    'อ': 'v',
    'ิ': 'b',
    'ื': 'n',
    'ท': 'm',
    'ม': ',',
    'ใ': '.',
    'ฝ': '/',
    'ๅ': '1',
    '/': '2',
    '-': '3',
    'ภ': '4',
    'ถ': '5',
    'ุ': '6',
    'ึ': '7',
    'ค': '8',
    'ต': '9',
    'จ': '0',
    'ข': '-',
    'ช': '='
  }

  output_string = ""

  for char in input_string:
    output_string += char_map.get(char, char)

  return output_string

prompt = input("prompt: ")
print(correct_language(prompt))
