#0-поле
#1-Дерево
#2-Река

class Map:
    #def generate_rivers():

    #def generate_forest():
    
    def print_map():
        for row in self.celss:
            for cell in row:
                if cell == 0:
                    print()



    def __init__(self, w, h):
        self.cells = [[0 for i in range(w)]for j in range(h)]