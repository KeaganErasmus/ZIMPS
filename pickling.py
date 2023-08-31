import pickle


class Pickling:

    def __init__(self, filename="initial.pickle"):
        """Initialize the Pickling class with a filename."""
        self.value = "initial value"
        self.filename = filename

    def save(self, *data, filename=None):
        """
        Save the data to a pickle file.
        If a filename is provided, it will update the class attribute.
        Keagan, Christian
        """
        if filename:
            self.filename = filename

        with open(self.filename, 'wb') as file:
            pickle.dump(data, file)

    def load(self, filename=None):
        """
        Load data from a pickle file and store it in self.value.
        If a filename is provided, it will update the class attribute.
        Sam, Christian
        """
        if filename:
            self.filename = filename

        with open(self.filename, 'rb') as file:
            self.value = pickle.load(file)
        return self.value

    def change_filename(self, new_name):
        """
        Update the filename for future operations.
        Christian
        """
        self.filename = new_name

    def print_value(self):
        """
        Print the current value.
        Sam
        """
        print(self.value)


if __name__ == "__main__":
    p = Pickling()

    # Print initial value
    p.print_value()

    # Save initial value
    p.save(p.value)

    # Load saved data
    loaded_data = p.load()
    p.print_value()

    # Change value and save again
    p.value = "changed text"
    p.save(p.value)

    # Load new data
    new_loaded_data = p.load()
    p.print_value()
