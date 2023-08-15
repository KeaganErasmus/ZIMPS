from pickle import dump, load


class Pickling:

    def __init__(self):
        self.value = "file text initial"
        self.filename = "initial"
        self.file = open(str(self.filename), 'wb')

    def open_file(self):
        self.file = open(str(self.filename), 'rb')
        self.load()

    def close_file(self):
        self.file.close()
        self.value = "nothing"

    def load(self):
        self.value = load(self.file)

    def dump(self):
        self.file = open(str(self.filename), 'wb')
        dump(self.value, self.file)

    def change_value(self, new_str):
        self.value = new_str

    def print_value(self):
        print(self.value)

    def write_new_file(self, fn):
        # close current file
        self.close_file()
        self.filename = fn
        # set current file to be new file we just wrote
        # with inputted filename fn
        self.file = open(str(self.filename), 'wb')


if __name__ == "__main__":
    # pickle has initial file created
    p = Pickling()
    # print value
    p.print_value()
    # save value to file
    p.dump()
    # close file
    p.close_file()

    # print
    p.print_value()

    # open file
    p.open_file()
    # print
    p.print_value()

    # change value
    p.change_value("changed text")
    # dump new value
    p.dump()
    # print value
    p.print_value()
    # close file again
    p.close_file()

    # open file
    p.open_file()
    # print
    p.print_value()
    # close file again
    p.close_file()

