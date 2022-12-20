from utils.Logger import Logger
import pickle

class Persistance():
    @classmethod
    def save(cls, obj, file_path):
        with open(file_path, 'wb') as buffer:
            pickle.dump(obj, buffer)
        Logger.log_message(f"[Saved: [{type(obj)}]]")
          
    @classmethod  
    def load(cls, file_path):
        with open(file_path, 'rb') as buffer:
            load = pickle.load(buffer)
            Logger.log_message(f"[Loaded: [{type(load)}]]")
            