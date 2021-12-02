from alphabet import Alphabet
OPERATIONS = ['encode', 'decode']
class CifoCifer:
    def __init__(self):
        self.range_crypt_chars = []
        self.new_text = ''
        self.origin_text = ''

    def action(self,need_to='encode', text='demo', shift=0):
        self.clear_all()
        self.origin_text = text
        if need_to.lower() in OPERATIONS:
            alphabet = Alphabet()
            self.range_crypt_chars = alphabet.chars_nums()
            shift_amount = int(shift) % len(self.range_crypt_chars)
            if need_to == 'decode':
                shift_amount *= (-1)
            #print(f'lengh of list {len(self.range_crypt_chars)}')   # for debugging
            #print(f'shift : {shift_amount}')    # for debugging
            for letter in text:
                if letter in self.range_crypt_chars:
                    position = self.range_crypt_chars.index(letter)
                    new_position = position + shift_amount
                    while new_position > len(self.range_crypt_chars):
                        new_position %= len(self.range_crypt_chars)
                    new_letter = self.range_crypt_chars[new_position]
                    self.new_text += new_letter
                else:
                    self.new_text += letter
            print(self.new_text)
        else:
            print(f'Sorry {need_to} is in valid value for action')

    def get_origin(self):
        print(f'The original text is: [{self.origin_text}]')
        return self.origin_text

    def clear_all(self):
        self.new_text = ''
        self.origin_text = ''

    def export(self, file_name):
        if file_name:
            with open(f'{file_name}.txt', mode='w') as f_output:
                f_output.write(self.new_text)






