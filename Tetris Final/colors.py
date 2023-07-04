class Colors:
    dark_grey=(26, 31, 40)
    light_grey=(211, 211, 211)
    violet=(143, 0, 255)
    indigo=(75, 0, 130)
    blue=(0, 0, 255)
    green=(0, 255, 0)
    yellow=(255, 255, 0)
    orange=(255, 165, 0)
    red=(255, 0, 0)
    light_blue=(173, 216, 230)
    white=(255,255,255)
    black=(0,0,0)
    @classmethod
    def get_cell_colors(cls):
        return[cls.dark_grey,cls.violet,cls.indigo,cls.blue,cls.green,cls.yellow,cls.orange,cls.red]
    
