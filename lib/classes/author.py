class Author:
    def __init__(self, name):
        self.name = name
        self.articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) >0 :
            self._name = new_name
        else:
            raise ValueError("Invalid name")


    def get_magazines(self):
        return set ([a.magazine for a in self.articles])
        

    def has_written_for_magazine(self, magazine):
        return magazine in self.get_magazines()
