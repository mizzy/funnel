from .runner import *

class Funnel():
    def __init__(self):
        pass

    @classmethod
    def run(self):
        context = self()
        Runner(context).run()
        
