import shelve

class Shelving:
    def create_file(self, filename: str):
        new_file = shelve.open(filename + ".db")
        new_file.close()
    
    def load_file_content(self, filename: str):
        try:
            with shelve.open(filename) as db:
                items = db.items()
                for item in items:
                    print(item)
        except:
            print("Shelve file does not exist does not exist")

    def save_object(self, object: object, filename):
        file = shelve.open(filename)
        object_values = object
        file['health'] = object_values.get_health()
        file['location'] = object_values.get_location()
        file['items'] = object_values.get_items()



def main():
    shelver = Shelving()

    shelver.create_file("shelve_test")
    try:
        shelver.load_file_content("shelve_test.db")
    except FileNotFoundError as err:
        print(err)


if __name__ == "__main__":
    main()