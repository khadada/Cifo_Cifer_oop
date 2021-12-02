class Alphabet:
    def __init__(self):
        self.lower_letters_list = []
        self.upper_letters_list = []
        self.number_list = []
        self.all_characters = []

    def lower_case_letters(self):
        self.lower_letters_list.extend([chr(i) for i in range(ord("a"), ord("z"))])

    def upper_case_letters(self):
        self.upper_letters_list.extend([chr(i) for i in range(ord("A"), ord("Z"))])

    def numbers(self):
        self.number_list.extend([i for i in range(0,9)])

    def chars_nums(self):
        self.lower_case_letters()
        self.upper_case_letters()
        self.numbers()
        self.all_characters.extend(self.lower_letters_list)
        self.all_characters.extend(self.upper_letters_list)
        self.all_characters.extend(self.number_list)
