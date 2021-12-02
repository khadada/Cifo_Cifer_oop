class Alphabet:
    def __init__(self):
        self.lower_letters_list = []
        self.upper_letters_list = []
        self.number_list = []
        self.all_characters = []

    def lower_case_letters(self):
        self.lower_letters_list.extend([chr(i) for i in range(ord("a"), ord("z"))])
        return self.lower_letters_list

    def upper_case_letters(self):
        self.upper_letters_list.extend([chr(i) for i in range(ord("A"), ord("Z"))])
        return self.upper_letters_list

    def numbers(self,start=0,end=10):
        self.number_list.extend([i for i in range(start,end)])
        return self.number_list

    def chars_nums(self):
        self.lower_case_letters()
        self.upper_case_letters()
        self.numbers()
        self.all_characters.extend(self.lower_letters_list)
        self.all_characters.extend(self.upper_letters_list)
        self.all_characters.extend(self.number_list)
        return self.all_characters
