class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError('Invalid magazine name')

    def get_authors(self): #for every article in self.articles, put article author inside this list
        return set([a.author for a in self.articles])

    def get_article_titles(self):
        return [a.title for a in self.articles]

    def get_longest_article(self):
        longest_article = self.articles [-1]
        for article in self.articles:
            if article.word_count > longest_article.word_count:
                longest_article = article
        return longest_article

    def get_average_word_count(self):
        total = 0
        count = 0
        for article in self.articles:
            total += article.word_count
            count += 1
        return total / count
        

    def get_top_contributor(self):
        """Note this method is an optional stretch goal"""
        pass
