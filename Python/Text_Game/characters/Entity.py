from data.Stats import Stats

class Entity:
    
        def __init__(self) -> None:
             self.stats = Stats()
    
        def create(self):
            print("[Creating Entity ...]")
            return self

        def get_stats(self) -> Stats:
            return self.stats
        
