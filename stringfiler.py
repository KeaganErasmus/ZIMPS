class StringFiler:

    def __init__(self):
        self.value = "file text initial"
        self.filename = "string.txt"
        self.file = open(str(self.filename), 'w')

    def close_file(self):
        self.file.close()
        self.value = "nothing"

    def load_file(self):
        with open(self.filename) as file:
            self.value = file.readline()

    def save_file(self):
        with open(self.filename, "w") as file:
            file.write(self.value)

    def change_value(self, new_str):
        self.value = new_str

    def change_filename(self, new_name):
        self.filename = new_name

    def print_value(self):
        print(self.value)


if __name__ == "__main__":
    # initial text
    sf = StringFiler()
    # print value
    sf.print_value()
    # save value to file
    sf.save_file()
    # close file
    sf.close_file()
    # print value
    sf.print_value()

    sf.load_file()
    # print value
    sf.print_value()

    sf.change_value("yeet")
    sf.print_value()
    sf.save_file()

    sf.close_file()

    sf.load_file()

    sf.print_value()

    sf.close_file()
