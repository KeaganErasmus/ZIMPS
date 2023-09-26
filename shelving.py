import shelve

class Shelving:
    def __init__(self):
        self.filename = ""

    def create_file(self, filename):
        self.filename = filename
        new_file = shelve.open(filename)
        new_file.close()
    
    def load_file_content(self, filename):
        try:
            db = shelve.open(self.filename)
            items = db.items()
            for item in items:
                print(item)
        except:
            print("Shelve file does not exist does not exist")

    def save_object(self, object: object, filename):
        try:
            file = shelve.open(filename)
            object_values = object
            file['health'] = object_values.get_health()
            file['location'] = object_values.get_location()
            file['items'] = object_values.get_items()
        except:
            print(f'Cannot save to file {filename}')
