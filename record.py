class Record:
    def __init__(self, title, content, date_recorded):
        self.title = title
        self.content = content
        self.date_recorded = date_recorded
        
    def __str__(self):
        return f'{self.title}, {self.content}, {self.date_recorded}'
    
        
