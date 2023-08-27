import shelve

class Shelving:
    def create_file(self, filename="player_data"):
        new_file = shelve.open(filename)
        new_file.close()
    
    def load_file_content(self, filename="player_data"):
        try:
            with shelve.open(filename) as db:
                items = db.items()
                for item in items:
                    print(item)
        except:
            print("Shelve file does not exist does not exist")

    def save_object(self, object: object, filename="player_data"):
        file = shelve.open(filename)
        object_values = object
        file['health'] = object_values.get_health()
        file['location'] = object_values.get_location()
        file['items'] = object_values.get_items()
