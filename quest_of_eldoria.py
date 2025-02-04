import random, time


class Game:
    def __init__(self, trainer='Unknown', monster=-1, level=1):
        self.trainer = trainer
        self.level = level
        self.health = random.randint(10 * level, 20 * level)
        self.attack = random.randint(10 * level / 2, 20 * level / 2)
        self.type = monster
        self.exp = 0
        self.evil_hp = random.randint(10 * level, 20 * level)
        self.evil_atk = random.randint(10 * level / 2, 20 * level / 2)
        self.evil_type = random.randint(1, 3)
        self.evil = [
            """
    ⠀⠀⠀⠀⢶⡆⠀⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⣾⣿⣦⣤⣭⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣰⠏⠀⢹⣻⣭⣭⡧⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢠⠏⠀⠴⠚⣷⣿⣿⠀⠀⢀⡤⠖⠛⠹⠶⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡏⠀⠀⠀⡼⠉⠉⠁⢀⡴⠋⠀⠀⠤⢄⡀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡇⠀⠀⠀⢧⡀⠀⢠⠎⠀⢠⣤⡞⠒⠲⡌⠃⠀⠀⠀⠱⢤⡀⠀⢀⣀⣀⣀⠀⠀
    ⠀⣧⠀⠀⠀⠀⠙⠲⠏⠀⢀⡀⠙⣇⠀⠀⢘⡶⠆⣤⠤⠔⢲⣯⡖⠉⠀⠀⠈⢧⠀
    ⠀⢺⣦⡀⠀⠂⠀⠀⠀⠀⠀⢠⣄⠼⣗⠒⠋⠀⠀⠹⣄⣠⣿⡋⡀⢠⣤⡆⠀⢸⠀
    ⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⠦⣠⠴⣄⢀⣠⣄⣸⠇⠀⣳⣿⣧⠈⢹⠁
    ⠀⠀⠀⠘⠶⡆⠀⠆⢶⣴⠀⢾⠀⠀⠀⠀⠀⠀⠈⠉⡼⡭⣭⡴⠖⠼⠛⣿⣿⠏⠀
    ⠀⠀⠀⠀⠀⢻⠀⠀⠀⠁⠀⠘⡄⠀⣠⢤⣀⡤⡄⢸⣿⣿⠋⠀⠀⠀⠀⠙⠁⠀⠀
    ⠀⠀⠀⠀⠀⣏⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠘⠛⢱⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⠁⠀⠀⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠃⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⣷⣄⢠⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⠃⠀⡄⠀⠀⠺⠾⠃⠀⠀⠀⠀⠾⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣀⣀⡴⠋⠀⠛⠁⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⠁⠀⠀⠀⠀⣤⡄⠀⠀⠀⡴⠛⠲⡄⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⡇⠀⠀⠀⣀⠀⠘⠀⠀⣠⠞⠁⠀⠀⢣⠀⠀⠀⠀⠠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠘⠒⠒⠶⠁⠉⠉⠉⠉⠁⠀⠀⠀⠀⡞⠀⠀⠰⠇⠐⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣼⠁⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠷⠤⠤⠤⠤⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⣤⣤⣀⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⢸⣄⠉⠁⠉⢉⡲⢤
    ⠀⠀⠀⢀⡠⠴⠊⣭⠃⠀⣀⣀⡤⠴⢶⠤⠤⢤⣀⠀⢸⠸⠈⠣⡀⢠⠃⠀⠀
    ⠀⢀⢔⡉⢀⣀⠐⠐⢧⣾⣴⣿⡿⠀⠀⡏⡄⠀⠀⢱⡧⢀⡠⠤⠬⣎⣧⠀⠀
    ⠐⠋⠁⠀⠀⢸⠔⢢⣿⣿⣿⡿⠃⠀⢠⠃⠀⠠⢚⣉⣠⢯⠀⠀⠀⠈⠛⠀⠀
    ⠀⠀⠀⠀⠀⠈⠀⣼⠙⠛⠉⠀⢀⣠⢊⠆⠀⠀⠈⣴⠃⣼⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡌⢦⣀⣀⠬⡺⠕⠁⠀⠀⠀⢀⠟⠸⡟⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡇⣀⠀⡦⢄⣠⣾⣿⣾⣦⠀⢀⠼⢱⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠳⡏⠉⠁⣀⠈⠻⣿⣿⠉⠀⠈⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡏⠁⠈⠙⣿⢟⡀⢀⠄⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⡤⠀⡤⠃⠫⡉⠙⠃⠁⠀⠈⠠⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠰⠐⡀⠀⠀⠀⠀⣨⠆⠀⣀⠤⠒⠀⠙⠣⠤⠐⠒⠒⠄⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠊⡉⠀⠀⡜⠄⠀⠘⣏⡄⠀⣀⡠⠤⠠⢄⠘⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⠀⡔⣳⠒⠒⠚⣿⠀⠰⢎⠀⠈⠁⠀⠀⠀⠀⢠⠇⡼⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠳⢌⡘⢄⡀⠀⠘⠦⣀⣉⣉⣁⠒⣄⠀⠀⠀⣸⢼⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡧⣸⠀⠀⠀⠀⢠⠔⠋⢀⡼⠀⠀⠀⠉⠉⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠊⠁⠀⠀⠀⠀⠈⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠠⠤⠠⠤⠴⠠⠠⠠⠤⠤⠀⠠⠲⠀⠆⠤⠦⠴⠰⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⠀⡴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣧⠀⣾⠀⣰⠾⡇⠀⠀⢀⣶⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⡾⠤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢻⣾⠀⠸⣿⠋⣿⠃⢀⣷⣶⣴⠋⢹⠀⠀⠀⠀⠀⠀⠀⠀⢻⠳⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡿⠦⠤⠿⢤⣀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠻⣀⣤⣻⣄⣀⣀⡉⠉⠹⠇⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⣸⠖⠚⣆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣇⣀⣀⠤⠊⠈⢹⠶⣄⣀⣀⡤⠶⠚⠛⠉⠉⠉⠀⠀⠀⠉⠉⠙⠓⠲⠤⣾⣀⠀⠀⠀⢀⣠⡴⢾⠓⢤⣄⣸⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢻⡅⠀⠀⣠⠔⠁⡤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣞⠋⢇⠀⠈⠳⣄⣀⣸⠃⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠻⣖⠋⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡌⠳⢤⣀⣀⢠⠏⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⢦⣤⢟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⢀⡽⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⠀⠀⣼⡧⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣤⠤⢴⠖⠘⡟⣃⣀⡀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⢰⡚⠛⡆⢠⡏⢉⢉⣿⡉⠉⣹⣏⠉⠉⣿⣉⠉⢹⣯⣁⣀⡿⣦⣶⣾⠆⠀⠘⢷⣤⠟⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠹⡆⠉⠉⠀⠀⠓⠖⠋⠈⠉⠉⠁⠙⠛⠛⠉⠙⠒⠛⠉⠉⠉⠀⠀⠉⠁⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠴⠚⢿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢺⡏⠙⠓⠶⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⠖⠁⠀⣾⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠈⠲⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⠞⠁⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠁⠀⠀⠀⠈⠉⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀
    ⠀⠀⢀⠞⠁⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠹⡄⠀⠀⠀
    ⠀⢠⠏⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠘⣆⠀⠀
    ⢀⡏⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠈⣇⠀
    ⠸⡇⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢸⡆
    ⠀⠹⢄⡀⠀⠀⣀⢾⡇⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⢸⠃
    ⠀⠀⠀⠉⠛⠛⠁⢸⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⡏⠳⣄⣀⣀⣀⠴⠃⠀
    ⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⡇⠀⠀⠉⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠜⠉⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠈⠙⠓⠶⠤⣤⣀⣀⣀⣀⣀⣀⣀⡤⠴⠒⠋⠁⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠈⠙⠓⠶⠤⣤⣤⣤⣤⣤⣤⣤⠤⣴⠖⠚⠋⠁⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⡀⠀⠀⠀⢀⣀⡼⠁⠀⠀⠀⠀⠀⠀⠘⢦⣤⣀⣀⣀⣀⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⢀⣤⣔⠲⢤⡖⢶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⣴⠢⣄⡀⠀
    ⠀⢀⣤⣤⠤⣜⡿⠭⡤⠈⢳⣤⣀⡈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⢶⣿⡀⣠⣿⣴⣻⡇⠀
    ⠀⠘⠓⠓⢶⠈⢹⢀⡟⠀⣼⣡⠏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⣇⣻⣾⢻⠁⣨⣿⣭⣀⠀
    ⠀⠀⠀⢠⡿⠒⠋⠉⣉⣛⡻⠄⢀⡴⠋⠀⠀⠀⢀⣠⡶⠟⠉⠉⠉⠉⠛⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣀⣨⣇⣀⣸⣟⢁⣴⣻⣼⣷
    ⠀⢀⡶⠋⠐⠒⠒⠒⣏⠨⠭⠗⢯⡀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⢀⣠⠖⠻⠽⢩⡏⠀⠀⠉⢹⡟⠛⠋⠁
    ⠀⣼⣄⠀⠀⣰⠖⠑⠺⣗⠲⠆⢠⠇⠀⠀⢠⡏⠀⠀⠀⠀⣴⣻⣷⡆⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⢸⠁⠐⢶⣶⠯⠿⣕⠚⠁⠈⠻⡆⠀⠀
    ⢰⡟⡏⠒⠲⣄⠀⠀⠀⠈⢂⣠⠟⠀⠀⢀⣼⡇⠀⠀⠀⠀⠻⣿⡿⠃⠀⠀⠀⠀⠀⡏⠓⢦⣄⠀⠀⠀⠸⣆⠀⠈⠁⠀⠀⠼⠀⡀⠀⣠⣇⠀⠀
    ⢸⡿⣷⠀⠀⠈⠓⠲⣶⠞⠉⠁⠀⢀⣴⠟⠉⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠇⠀⠀⠈⢳⡀⠀⠀⠙⠷⣄⣀⣀⣀⡠⠞⠉⠉⣿⣼⠀⠀
    ⣿⣇⠈⠃⠀⠀⠀⢰⣇⣄⠀⠀⠀⡜⠁⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⣹⠉⠉⠀⠀⠀⢸⠟⡝⠀⠀
    ⡏⠛⠀⠀⠀⠀⠀⢸⣿⣗⠀⠀⣼⡥⠖⠒⠀⠀⠀⠈⠙⠻⠶⠶⠶⠶⠾⢛⠁⠀⠀⠀⠀⡀⠈⠉⠲⣇⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⣰⣳⡄⠀
    ⢹⡄⠀⠀⠀⠀⠀⠀⠙⢿⣇⢰⠏⠀⢠⣶⢶⣦⣄⡀⠀⠀⠉⠒⠒⠒⠋⠁⠀⠀⣀⣴⣿⣿⣿⣦⠀⠘⡇⢀⣿⠟⠁⠀⠀⠀⠀⠀⠰⠋⢸⡇⠀
    ⠸⣷⠀⠀⠀⠀⠀⠀⠀⠘⠻⣾⠀⠀⢸⣿⣿⣧⣈⣿⣷⣤⣀⠀⠀⠀⠀⣀⣠⣾⣯⣼⣿⠛⣿⠏⠀⠀⢸⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀
    ⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠈⠻⣿⡿⢿⣿⣿⠀⠉⢻⣿⣿⣿⣿⣿⠛⠻⣿⣿⠟⠋⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀
    ⠀⠀⠈⣷⡄⠀⠀⠀⠀⠀⠀⠸⣧⡄⠀⠀⠈⠙⠶⠼⣿⣿⣶⣿⣿⣿⣿⣀⣿⠶⠖⠋⠁⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⡴⡿⠃⠀⠀⠀
    ⠀⠀⠀⠈⢿⡳⠀⠀⠀⠀⠀⠀⠹⣽⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⢦⠀⠀⠀⠀⠀⠀⠙⢯⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣟⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⡼⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠷⣄⠀⠀⠀⠀⠀⠀⠀⠁⠘⠳⣤⢢⣄⠀⠀⠀⠀⠀⠀⣀⡀⢀⡴⠋⣰⠟⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⡀⠀⠀⠀⠀⠉⠻⠿⠲⢬⣆⣠⣞⣿⡵⢫⠖⠁⠀⠀⠀⠀⠀⡾⠁⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⢹⡀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠘⠈⡴⠃⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠻⡿⣄⡀⣦⡀⠀⠀⠀⠀⠀⠀⠚⠁⠀⣀⡀⢀⣠⣾⡟⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⠤⠄⠀⠹⠌⠓⣿⠙⠷⣄⠀⠀⠀⡄⠀⣠⡴⣿⡵⠟⠹⠋⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠱⣄⣼⣿⠞⠋⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣠⡀⠀⠀⠀⡟⠳⠤⣄⣀⣀⠀⠀⠀⢀⣀⣀⣠⠤⠴⠚⡄⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠹⡷⣄⠀⠀⣷⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⣀⡇⠀⠀⢀⣴⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⢞⣁⣀⣀⣀⣈⣓⣤⣀⠙⣆⡀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣿⠁⣠⠴⢯⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⡟⡏⠁⠀⣀⣀⡽⠿⢿⣿⣷⢯⡩⠗⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣟⠋⢹⣁⣀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠘⢧⢷⡖⠿⠟⢛⣏⠙⠲⡌⢻⣷⣷⢤⣀⠚⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⢻⡘⣆⣨⠵⠚⠛⠛⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠛⢿⣆⡘⢉⣈⡉⠉⠙⠉⣁⣬⠟⡺⢵⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠳⣼⣉⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠒⠛⠿⢾⣵⣞⠁⠀⠒⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⣀⠉⠉⠙⠛⢛⣛⡫⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣖⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄⠀⢰⣀⡼⡇⠀⠘⡆⠀⣀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⠿⠿⠛⣛⡿⠷⠶⣟⢷⡴⣧⣤⣰⡓⠉⡃⢀⣠⠄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠟⠋⠀⠀⢀⠞⠁⠀⠀⠀⠈⢳⣿⡟⠒⢿⣿⠢⡭⡝⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⣠⠤⠤⠼⣄⠀⠀⠿⠟⠀⡞⡿⢆⠀⠀⢻⣧⠙⢟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣿⣿⠋⠀⠀⢠⠎⠀⢀⣀⠀⠈⢳⡀⠀⠀⣼⡾⣧⠀⠀⠀⠀⢏⠏⠈⢧⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣴⣿⡿⢁⡠⠔⠒⡞⠀⠀⠘⠿⠃⠀⢠⡿⢛⣿⡟⠓⠄⠀⠀⠀⠀⢸⢸⠀⠈⢆⠀⠀⠀⠀
    ⠀⠀⠀⠀⠰⢿⣿⣷⠋⠀⢀⣀⡙⢄⡀⠀⠀⠀⣠⣾⣷⣿⠋⠛⠀⠀⠀⠀⠀⠀⠈⡇⡧⢦⣼⡀⠀⠀⠀
    ⠀⠀⠀⠀⠘⣖⢺⣿⡀⠀⠘⠿⠃⠀⣹⢛⣿⠟⣋⠽⣾⡉⠃⠀⠀⠀⠀⠀⠀⠀⣀⡇⢡⠐⠂⡇⠀⠀⠀
    ⠀⢀⡆⢰⠺⣡⢋⣳⣵⣦⣤⣤⣤⣶⣿⣭⠶⡏⠙⠀⠈⠀⠀⠀⠀⢀⡤⠒⠉⢙⡢⡇⡘⠀⠀⢹⠀⠀⠀
    ⢀⡎⠣⠠⢧⠁⢸⢻⠹⡟⡇⠙⠇⠻⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⢀⣠⣬⠟⡱⠁⠀⠀⠸⡄⠀⠀
    ⠈⠧⣀⣀⠸⡄⠈⢆⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⡇⣤⣰⠾⢋⡥⠊⠀⠀⠀⠀⢤⡇⠀⠀
    ⠀⠀⢠⡿⡎⣧⢲⡈⢦⠳⡀⠀⠀⠀⠀⢀⡀⠀⢰⡄⢠⣜⣷⠼⠛⣩⠤⠚⠁⠀⠀⠀⠀⠀⠰⠚⡇⠀⠀
    ⠀⠀⠀⡠⢛⣿⠠⠍⠂⠑⢍⡢⠼⣦⣷⣼⡷⠼⡖⣛⣩⠥⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
    ⠀⠀⣴⡁⠾⢼⣀⣀⣀⣀⣀⣉⣑⣒⣒⣒⡓⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠠⠤⠤⠧⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠐⠒⠒⠤⠤⠤⠄⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⠉⠉⠒⠒⠒⠈⠉
            """,
        ]
        self.type_list = ['fire', 'water', 'earth']
        self.boss = False

    def stats_update(self):
        # To level up, it needs 100 exp.
        if self.exp // 100 == 1:
            self.level += 1
            # print(self.level)
            print("Thy partner leveled up!")
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.exp -= 100
            self.health = random.randint(10 * self.level, 20 * self.level)
            self.attack = random.randint(10 * self.level / 2, 20 * self.level / 2)
            if self.level == 3:
                self.boss = True
        self.evil_hp = random.randint(10 * self.level, 20 * self.level)
        self.evil_atk = random.randint(10 * self.level / 2, 20 * self.level / 2)
        self.evil_type = random.randint(1, 3)

    def status(self):
        print(
            f"{self.trainer}'s partner is {self.level} level, has {self.health} health, {self.attack} attack, {self.type_list[self.type - 1]} type, and {self.exp} / 100 exp.")

    def opening(self):
        trainer = input("What is thou nameth?\n")
        self.trainer = trainer
        if self.trainer == "unlimited":
            self.unlim()
        prepared = 'n'
        print("""

                             ▄█     █▄     ▄████████  ▄█        ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████
                            ███     ███   ███    ███ ███       ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███
                            ███     ███   ███    █▀  ███       ███    █▀  ███    ███ ███   ███   ███   ███    █▀
                            ███     ███  ▄███▄▄▄     ███       ███        ███    ███ ███   ███   ███  ▄███▄▄▄
                            ███     ███ ▀▀███▀▀▀     ███       ███        ███    ███ ███   ███   ███ ▀▀███▀▀▀
                            ███     ███   ███    █▄  ███       ███    █▄  ███    ███ ███   ███   ███   ███    █▄
                            ███ ▄█▄ ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███   ███   ███   ███    ███
                             ▀███▀███▀    ██████████ █████▄▄██ ████████▀   ▀██████▀   ▀█   ███   █▀    ██████████
        """)  # https://www.asciiart.eu/text-to-ascii-art
        opening_script = f"""
        ======================================================================================================================================

        Welcome to the Quest of Eldoria!

        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Hark, noble tamer {self.trainer}!

        In the land of Eldoria, where shadows doth grow long and despair whispers on the wind, a dark force hath taken hold.
        The wicked King Maldrak hath seized Princess Aria, and with her, the hope of the realm.

        Thou art a tamer of monsters, a soul bound to creatures both fierce and noble.
        But nay, thou art not alone in thy quest.

        A creature of great power, loyal to thee, doth accompany thy journey.
        This beast, tamed by thy hand, shall aid thee in the coming trials, for thou must face mighty foes and treacherous lands.

        Thy Quest:

        1. Venture forth to the dark fortress where the princess is held.
        2. With thy companion, battle foes most fearsome, deciding whether to strike, heal, or weaken the enemy.
        3. Prove thy strength and wit, for the fate of the kingdom rests in thy hands.

        Be thou wise, for thine choices shall determine the kingdom's fate.
        Only those with valor and bravery shall succeed.

        Prepare thyself, and let the journey begin.
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        self.script_timer(opening_script)
        t = 0
        while prepared != 'y':
            text = "Art thee ready" + " now" * t + "? (y/n)\n"
            prepared = input(text)
            t += 1
        print(
            "======================================================================================================================================")
        print("Choose thy partner type!")
        type_explanation = """
            Explanation about Types:
            There are Fire, Water, and Earth types.
            Water fights Fire, and when Fire fights Water, it deals 0.8 times the damage.
            When Water fights Fire, it deals 1.2 times more damage.
            The type advantage follows the cycle: Fire < Water < Earth < Fire.
            """
        self.script_timer(type_explanation)
        print(self.type_list)

        # number denotes the type.

        monster = -1
        t = 0
        while monster not in range(1, 4):
            monster = input("Choose wisely" + " again" * t + ": (1/2/3)\n")
            monster = int(monster) if monster.isnumeric() else -1
            t += 1
        print("Great choice! Godspeed noble tamer!")
        self.type = monster
        # self.status()

    def chapters(self):
        if self.level == 1:
            print("""
                   █████████  █████                           █████                          ████
                  ███░░░░░███░░███                           ░░███                          ░░███
                 ███     ░░░  ░███████    ██████   ████████  ███████    ██████  ████████     ░███
                ░███          ░███░░███  ░░░░░███ ░░███░░███░░░███░    ███░░███░░███░░███    ░███
                ░███          ░███ ░███   ███████  ░███ ░███  ░███    ░███████  ░███ ░░░     ░███
                ░░███     ███ ░███ ░███  ███░░███  ░███ ░███  ░███ ███░███░░░   ░███         ░███
                 ░░█████████  ████ █████░░████████ ░███████   ░░█████ ░░██████  █████        █████
                  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░░        ░░░░░
                                                   ░███
                                                   █████
                                                  ░░░░░
            """)  # https://www.asciiart.eu/text-to-ascii-art
            print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢠⢤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠒⠒⠲⠎⠀⠀⢹⡃⢀⣀⠀⠑⠃⠀⠈⢀⠔⠒⢢⠀⠀⠀⡖⠉⠉⠉⠒⢤⡀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠚⠙⠒⠒⠒⠤⡎⠀⠀⠀⠀⢀⣠⣴⣦⠀⠈⠘⣦⠑⠢⡀⠀⢰⠁⠀⠀⠀⠑⠰⠋⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⢰⠃⠀⣀⣀⡠⣞⣉⡀⡜⡟⣷⢟⠟⡀⣀⡸⠀⡎⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀
        ⢰⠂⠀⠀⠀⠀⠀⠀⠀⣗⠀⠀⢀⣀⣀⣀⣀⣀⣓⡞⢽⡚⣑⣛⡇⢸⣷⠓⢻⣟⡿⠻⣝⢢⠀⢇⣀⡀⠀⠀⠀⢈⠗⠒⢶⣶⣶⡾⠋⠉⠀⠀⠀⠀⠀
        ⠈⠉⠀⠀⠀⠀⠀⢀⠀⠈⠒⠊⠻⣷⣿⣚⡽⠃⠉⠀⠀⠙⠿⣌⠳⣼⡇⠀⣸⣟⡑⢄⠘⢸⢀⣾⠾⠥⣀⠤⠖⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠀⠀
        ⠀⠀⠀⢰⢆⠀⢀⠏⡇⠀⡀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⣸⡇⢐⡟⠀⠙⢎⢣⣿⣾⡷⠊⠉⠙⠢⠀⠀⠀⠀⠀⢸⡇⢀⠀⠀⠀⠀⠈⠣⡀
        ⠀⠀⠀⠘⡌⢣⣸⠀⣧⢺⢃⡤⢶⠆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠋⢀⠔⣒⣚⡋⠉⣡⠔⠋⠉⢰⡤⣇⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠸
        ⠀⠀⠀⠀⠑⢄⢹⡆⠁⠛⣁⠔⠁⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⢠⡷⠋⠁⠀⠈⣿⡇⠀⠀⠀⠈⡇⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠑⣦⡔⠋⠁⠀⠀⠀⣿⠀⠀⢠⡀⢰⣼⡇⠀⡀⠀⠀⣿⠀⠁⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⡇⠀⠀⢴⣤⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⢨⣧⡿⠋⠀⠘⠛⠀⠀⣿⠀⠀⢀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢲⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡧⡄⠀⠹⣇⡆⠀⠀⠀⠀⠀⣿⠀⢰⣏⠀⣿⣸⣿⣿⠀⠀⠀⠀⣼⠀⠀⠰⠗⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡇⣷⣛⣦⣿⢀⠈⠑⠀⢠⡆⣿⠐⢠⣟⠁⢸⠸⣿⣿⢱⣤⢀⠀⣼⠀⠀⢀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⠀⠀⠀⢸⡇⠘⠫⣟⡇⠊⣣⠘⠛⣾⡆⢿⠀⠙⣿⢀⣘⡃⣿⣿⡏⠉⠒⠂⡿⠀⠰⣾⡄⠀⢸⡟⣽⣀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠘⣾⠀⠀⢸⡇⢸⣇⡙⠣⠀⣹⣇⠀⠈⠧⢀⣀⣀⡏⣸⣿⣇⢹⣿⡇⢴⣴⣄⣀⡀⢰⣿⡇⠀⢸⣇⢿⡿⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠓⠁⠈⠻⢷⠾⠦⠤⠬⣅⣹⣿⣖⣶⣲⣈⡥⠤⠶⡖⠛⠒⠛⠁⠉⠛⠮⠐⢛⡓⠒⢛⠚⠒⠒⠒⠛⣚⣫⡼⠿⠿⣯⠛⠤⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⡉⠉⠁⠀⠀⠘⠓⠀⠀⠀⠀⠀⣀⣞⡿⡉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            chapter1_dialogue = """
            Thy Journey Begins
            Through the ancient woods of Eldoria thou dost tread, where shadows linger and whispers of old fill the air.
            The scent of earth and moss surroundeth thee, yet unease pricketh at thy senses.

            Suddenly, the stillness breaketh.
            From the thicket cometh a low growl, fierce and unyielding.
            A monster emerges, its glowing eyes locked upon thee, its form both majestic and menacing.

            Thy companion readieth itself, prepared for battle.
            This beast standeth in thy way.

            What shalt thou do?
            """
            self.script_timer(chapter1_dialogue)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif self.level == 2:
            print("""
                   █████████  █████                           █████                           ████████
                  ███░░░░░███░░███                           ░░███                           ███░░░░███
                 ███     ░░░  ░███████    ██████   ████████  ███████    ██████  ████████    ░░░    ░███
                ░███          ░███░░███  ░░░░░███ ░░███░░███░░░███░    ███░░███░░███░░███      ███████
                ░███          ░███ ░███   ███████  ░███ ░███  ░███    ░███████  ░███ ░░░      ███░░░░
                ░░███     ███ ░███ ░███  ███░░███  ░███ ░███  ░███ ███░███░░░   ░███         ███      █
                 ░░█████████  ████ █████░░████████ ░███████   ░░█████ ░░██████  █████       ░██████████
                  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░░        ░░░░░░░░░░
                                                   ░███
                                                   █████
                                                  ░░░░░
            """)
            print("""
               ^^                __..-:'':__:..:__:'':-..__
                             _.-:__:.-:'':  :  :  :'':-.:__:-._
                           .':.-:  :  :  :  :  :  :  :  :  :._:'.
                        _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
                       [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
                       [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
              :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
              !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
              ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
                       [ ]                                        [ ]
                       [ ]                                        [ ]
                 jgs   [ ]                                        [ ]
               ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^
            """)  # https://www.asciiart.eu/buildings-and-places/bridges
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            chapter2_dialogue = """
            Thou Cometh Upon a Bridge
            At last, thou leavest the tangled embrace of the woods.
            Before thee stretcheth a narrow bridge, its ancient stones weathered by time and strife.
            It archest over a deep and yawning chasm, the wind howling through the void below.

            Yet as thou dost near, the air changeth.
            From the shadows of the bridge cometh a low growl, and a monstrous figure doth emerge.
            Its form is hulking, its eyes glowing like embers in the dark.
            This beast hath claimed the bridge as its own and shall not let thee pass unchallenged.

            Thy companion stepeth forward, unflinching, ready for battle.
            Steel thyself, for the path forward is fraught with peril!
            """
            self.script_timer(chapter2_dialogue)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif self.level == 3:
            print("""
                   █████████  █████                           █████                           ████████
                  ███░░░░░███░░███                           ░░███                           ███░░░░███
                 ███     ░░░  ░███████    ██████   ████████  ███████    ██████  ████████    ░░░    ░███
                ░███          ░███░░███  ░░░░░███ ░░███░░███░░░███░    ███░░███░░███░░███      ██████░
                ░███          ░███ ░███   ███████  ░███ ░███  ░███    ░███████  ░███ ░░░      ░░░░░░███
                ░░███     ███ ░███ ░███  ███░░███  ░███ ░███  ░███ ███░███░░░   ░███         ███   ░███
                 ░░█████████  ████ █████░░████████ ░███████   ░░█████ ░░██████  █████       ░░████████
                  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░░         ░░░░░░░░
                                                   ░███
                                                   █████
                                                  ░░░░░
            """)
            print("""
                                                 !_
                                                  |*~=-.,
                                                  |_,-'`
                                                  |
                                                  |
                                                 /^\\
                   !_                           /   \\
                   |*`~-.,                     /,    \\
                   |.-~^`                     /#"     \\
                   |                        _/##_   _  \_
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
           |*`--,_- _        |            |*`~-.,= []  |
           |.-'|=     []     |   !_       |_.-"`_-     |
           |   |_=- -        |   |*`~-.,  |  |=_-      |
          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
      |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\\
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \\
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
     | _- =-     |-_   | ((* |      |= _=       | -    |___\\
     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
     |=_ =       | =_-_| |  | |     |   =_      | -_   |
     |_=-_       |=_=  | |  | |     |=_=        |=-    |
^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^
            """)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            chapter3_dialogue = """
            Thou Hast Reached the Castle
            At long last, the dark silhouette of the castle loometh before thee, its spires piercing the storm-laden skies.
            The air is thick with dread, and the gates creak open as if beckoning thee to thy fate.
            Within the grand hall, upon a shadowed throne, sitteth King Maldrak, his gaze cold and unyielding.
            Beside him standeth the captive Princess Aria, her eyes pleading but steadfast.

            The wicked king riseth, his voice a thunderous command.
            “So thou hast come, tamer, seeking to defy me? Let us see if thou art worthy!”

            From the darkness, a monstrous guardian emergest, its power unlike any thou hast faced before.
            Thy companion standeth firm, ready for this final trial.

            The battle for Eldoria hath begun!
            """
            self.script_timer(chapter3_dialogue)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # the heart of this project
    def fight_sequence(self):
        print("""
              █████▒██▓  ▄████  ██░ ██ ▄▄▄█████▓
            ▓██   ▒▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒
            ▒████ ░▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░
            ░▓█▒  ░░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░
            ░▒█░   ░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░
             ▒ ░   ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░
             ░      ▒ ░  ░   ░  ▒ ░▒░ ░    ░
             ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░
                    ░        ░  ░  ░  ░
        """)
        time.sleep(0.5)
        if not self.boss:
            print(self.evil[random.randint(0, 4)])
            time.sleep(0.15)
            appearance = """
            A Wild Monster Appeareth!
            From the shadows, a fearsome creature doth emerge.
            Its eyes burn with unyielding fury, and its stance speaketh of a fierce challenge.
            The ground trembleth beneath its step as it approacheth thee.

            Thy companion groweth tense, ready to defend thee.

            Prepare thyself for battle!
            """
            self.script_timer(appearance)
        print(
            "======================================================================================================================================")
        print(
            f"Evil enemy has {self.evil_hp} health, {self.evil_atk} attack, and {self.type_list[self.evil_type - 1]} type.")
        time.sleep(0.15)
        print(
            f"{self.trainer}'s partner has {self.health} health, {self.attack} attack, and {self.type_list[self.type - 1]} type.")
        time.sleep(0.15)
        fight_dialogue = [
            "Your enemy looks determined.",
            "They are sizing you up.",
            "The monster lets out a fierce growl!",
            "Your foe seems hesitant.",
            "They don’t look good.",
            "Your enemy is frustrated.",
            "The monster flinches in pain.",
            "They seem ready to strike.",
            "Your foe looks weakened.",
            "The monster’s movements are sluggish.",
            "They glare at you with rage.",
            "Your enemy appears confident.",
            "The monster stumbles but regains balance.",
            "They seem to be biding their time.",
            "The monster lets out a triumphant roar!"
        ]
        moves = ['attack', 'debuff', 'heal']
        fight_or_flight = -1
        compared = self.compare_type()
        enemy_hp = self.evil_hp
        enemy_atk = self.evil_atk
        my_hp = self.health
        my_atk = self.attack
        now_turn = 0
        while fight_or_flight not in ['fight', 'flight']:
            if self.boss:
                fight_or_flight = 'fight'
            else:
                fight_or_flight = input("Will you fight or run?(fight/flight)\n")
        if fight_or_flight == 'flight':
            print("\nWomp Womp you ran away. Coward. Better luck next time!")
            time.sleep(0.15)
            print("(if you don't fight the game will not procede and will be in an infinite loop)\n")
            time.sleep(0.15)
            return 0
        elif fight_or_flight == "fight":
            while enemy_hp > 0 and my_hp > 0:
                move = -1
                if now_turn % 2 == 0:
                    while move not in moves:
                        move = input('Choose your move! (attack/debuff/heal)\n')
                    if move == "attack":
                        deal = my_atk * (1 if compared == 0 else 1.2 if compared < 0 else 0.8)
                        deal = random.uniform(deal*0.8,deal)
                        # print(deal)
                        enemy_hp -= round(deal)
                        print(f"You attack! You attack {round(deal)}.")
                        time.sleep(0.15)
                    elif move == "debuff":
                        debuff = round(random.uniform(0.1, 0.4), 2)
                        enemy_atk -= enemy_atk * debuff
                        enemy_atk = round(enemy_atk)
                        print(f"You decide to debuff! The enemy attack is down {round(enemy_atk * debuff)}")
                        time.sleep(0.15)
                    elif move == "heal":
                        heal = round(random.uniform(0.1, 0.4), 2)
                        my_hp += self.health * heal
                        my_hp = round(my_hp)
                        print(f"You decide to heal! The your health is healed {round(self.health * heal)}")
                        time.sleep(0.15)
                        if my_hp > self.health:
                            my_hp = self.health

                else:
                    decision = random.randint(0, 2)
                    move = moves[decision]
                    # move = 'attack'
                    if move == "attack":
                        deal = enemy_atk * (1 if compared == 0 else 1.2 if compared > 0 else 0.8)
                        deal = random.uniform(deal * 0.8, deal)
                        my_hp -= round(deal)
                        print(f"Monster attacks! It attacks {round(deal)}.")
                        time.sleep(0.15)
                    elif move == "debuff":
                        debuff = round(random.uniform(0.1, 0.4), 2)
                        my_atk -= my_atk * debuff
                        my_atk = round(my_atk)
                        print(f"Monster decides to debuff! Your attack is down {round(my_atk * debuff)}")
                        time.sleep(0.15)
                    elif move == "heal":
                        heal = round(random.uniform(0.1, 0.4), 2)
                        enemy_hp += self.evil_hp * heal
                        enemy_hp = round(enemy_hp)
                        print(f"Monster decide to heal! Its health is healed {round(self.evil_hp * heal)}")
                        time.sleep(0.15)
                        if enemy_hp > self.evil_hp:
                            enemy_hp = self.evil_hp
                print(fight_dialogue[random.randint(0, 14)])
                print(f"Your enemy has {enemy_hp} / {self.evil_hp} health {enemy_atk} / {self.evil_atk} attack")
                time.sleep(0.15)
                print(f"Your partner has {my_hp} / {self.health} health {my_atk} / {self.attack} attack")
                time.sleep(0.15)
                print(
                    "======================================================================================================================================")
                now_turn += 1
        if my_hp <= 0:
            print("Quest failed")
            return -1
        elif enemy_hp <= 0:
            print("You defeated the enemy!")
            time.sleep(0.15)
            exp_earned = random.randint(70, 100)
            print(f"You earned {exp_earned}")
            time.sleep(0.15)
            print(
                "======================================================================================================================================")
            self.exp += exp_earned
            return 1

    def compare_type(self):
        # ['fire', 'water', 'earth'] [1, 2, 3] General bigger num wins but fire wins earth so exception first
        if self.type == 1 and self.evil_type == 3:
            return -1
        elif self.type == 3 and self.evil_type == 1:
            return 1
        if self.type > self.evil_type:
            return -1
        elif self.type < self.evil_type:
            return 1
        if self.type == self.evil_type:
            return 0

    def repeat(self):
        rep_dialogue = ""
        if self.level == 1:
            rep_dialogue = """
            ======================================================================================================================================
            Thy Journey Continues
            The woods grow darker, the air thick with foreboding.
            From the shadows cometh a rustling, then a fearsome snarl.
            A monster emergeth, fiercer than the last, its eyes alight with fury.

            Thy companion standeth ready.
            Prepare thyself for battle once more!
            ======================================================================================================================================
            """
        if self.level == 2:
            rep_dialogue = """
            ======================================================================================================================================
            A Monster Blocketh Thy Path!
            As thou dost cross the bridge, the wind howlest beneath thee.
            From the shadows, a fearsome beast emergest, barring thy way.

            Thy companion standeth ready.
            Prepare for battle!
            ======================================================================================================================================
                        """
        self.script_timer(rep_dialogue)

    def boss_seq(self):
        boss_ani = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠖⠲⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠘⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠶⠤⣌⠈⢷⣄⠀⠀⠀⠀⣠⠞⢀⣠⠶⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠈⢳⡄⣽⠛⠀⠀⠀⡁⣰⠏⠀⠀⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣟⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠛⣿⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀⢀⣲⠟⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⠆⠀⠀⠈⣼⠁⠀⠀⠀⠀⠀⠀⠹⣿⡟⠂⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⢯⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢀⣴⠏⣀⣀⡀⣀⣀⣰⡟⣀⣀⣀⣀⣀⣀⣀⣀⣀⢀⣀⡀⢷⣀⣀⣀⣀⣀⣀⣳⣄⠀⠀⠀⠀
        ⠀⠀⠐⢻⡏⠉⠉⠉⢹⡉⠛⠛⠋⢉⡉⠉⠛⠉⢉⡍⠉⠉⠉⢩⡍⠉⠉⠉⣙⡉⠉⠉⠛⢹⠁⠀⠀⠀
        ⠀⠀⠀⢸⡇⠀⠀⣴⠋⠻⣄⠀⣰⠏⢻⣆⠀⣠⠟⠻⣆⠀⣠⠋⠹⣄⠀⣠⠏⠻⣆⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⠀⢸⡇⠀⠀⢿⡄⣴⠏⠀⢷⣦⣴⠟⠀⢻⣄⣴⠟⠈⢻⣄⢠⠟⠀⢿⣖⣴⠟⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⠀⣼⡇⠀⠀⠀⢹⠋⠀⡀⠀⢻⠏⠀⠀⠀⢻⡇⠀⠀⠀⢹⡏⠀⠀⠀⠹⠋⠀⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⣸⢿⡟⠛⢻⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡟⠛⢳⠞⣧⠀⠀⠀
        ⠀⢠⡿⣸⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡄⢹⡆⠀⠀
        ⠀⣼⣷⠟⣷⠀⠈⣿⠀⠀⠀⠀⣼⣦⡄⠀⠀⠀⠀⠀⠀⢀⣾⣦⠀⠀⠀⠀⠀⢠⡇⠀⣸⠃⠰⣳⠀⠀
        ⠀⡿⣿⠀⢻⠀⠀⢿⡀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠋⠉⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⣿⡄⠀
        ⢰⡇⠹⣦⢸⡆⠀⢸⡇⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢠⠃⢀⡼⠉⡇⠀
        ⢸⠇⠀⠈⠛⣷⡐⠘⡇⠀⠀⠀⠀⣠⡟⠁⠀⠀⠀⠀⠀⠈⢻⣄⠀⠀⠀⠀⢀⡿⠀⣸⠒⠋⠀⠀⣿⠀
        ⣿⠀⠀⠀⠀⢹⣇⠀⠿⣄⡀⠀⣴⠏⠷⣤⣤⣀⠀⣀⣤⡤⠾⠹⣧⠀⢀⣤⠞⠃⢰⠇⠀⠀⠀⠀⢿⡀
        ⣿⠀⠀⠀⠀⠀⢿⡄⠀⠈⠛⠾⠃⠀⢀⣤⣬⠉⠛⢉⣷⣄⠀⠀⠈⠷⠋⠁⠀⠀⡞⠀⠀⠀⠀⠀⢽⡇
        ⢹⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠸⣇⡉⠛⠛⠛⢃⣸⠇⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⣾⠀
        ⠸⠷⠶⠶⠶⠶⠶⠿⣇⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⣸⠷⠶⠖⠒⠒⠀⠀⠁⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠦⣤⣀⡀⠀⠀⠀⠀⣀⣀⣤⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                """
        print(boss_ani)
        self.evil_hp = random.randint(10 * self.level, 20 * self.level) * 1.5
        self.evil_atk = random.randint(10 * self.level / 2, 20 * self.level / 2) * 1.5
        self.evil_type = random.randint(1, 3)

    def winner(self):
        winner_dialogue = """
        A Triumph Most Glorious!
        Thy courage and valor hath shattered the chains of darkness, and Princess Aria is freed at last!
        The wicked King Maldrak hath been vanquished, his reign of terror brought to an end.
        The kingdom of Eldoria rejoiceth, for thou hast restored peace to the land.

        With the princess by thy side, thou dost return to the castle, where a grand feast awaits in thy honor.
        Songs of thy bravery shall echo through the halls for generations to come.

        And thus, thou hast completed thy quest, and the kingdom flourisheth under thy protection.
        Happily ever after shall be thy tale, forever sung by the bards of Eldoria.\n\n
        """
        self.script_timer(winner_dialogue)
        print("I hope you enjoyed the game")
        time.sleep(0.5)
        print("unlocked unlimited! Please name yourself 'unlimited' for endless monster fighting sequence")

    def script_timer(self, script, timing=0.15):
        for line in script.split("\n"):
            print(line)
            time.sleep(timing)

    def unlim(self):
        while True:
            result = self.fight_sequence()
            if result == -1:
                print("Game Over")
                quit()
            test.stats_update()


class Game_kor:
    def __init__(self, trainer='Unknown', monster=-1, level=1):
        self.trainer = trainer
        self.level = level
        self.health = random.randint(10 * level, 20 * level)
        self.attack = random.randint(10 * level / 2, 20 * level / 2)
        self.type = monster
        self.exp = 0
        self.evil_hp = random.randint(10 * level, 20 * level)
        self.evil_atk = random.randint(10 * level / 2, 20 * level / 2)
        self.evil_type = random.randint(1, 3)
        self.evil = [
            """
    ⠀⠀⠀⠀⢶⡆⠀⠀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⣾⣿⣦⣤⣭⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣰⠏⠀⢹⣻⣭⣭⡧⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢠⠏⠀⠴⠚⣷⣿⣿⠀⠀⢀⡤⠖⠛⠹⠶⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡏⠀⠀⠀⡼⠉⠉⠁⢀⡴⠋⠀⠀⠤⢄⡀⠀⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡇⠀⠀⠀⢧⡀⠀⢠⠎⠀⢠⣤⡞⠒⠲⡌⠃⠀⠀⠀⠱⢤⡀⠀⢀⣀⣀⣀⠀⠀
    ⠀⣧⠀⠀⠀⠀⠙⠲⠏⠀⢀⡀⠙⣇⠀⠀⢘⡶⠆⣤⠤⠔⢲⣯⡖⠉⠀⠀⠈⢧⠀
    ⠀⢺⣦⡀⠀⠂⠀⠀⠀⠀⠀⢠⣄⠼⣗⠒⠋⠀⠀⠹⣄⣠⣿⡋⡀⢠⣤⡆⠀⢸⠀
    ⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⠦⣠⠴⣄⢀⣠⣄⣸⠇⠀⣳⣿⣧⠈⢹⠁
    ⠀⠀⠀⠘⠶⡆⠀⠆⢶⣴⠀⢾⠀⠀⠀⠀⠀⠀⠈⠉⡼⡭⣭⡴⠖⠼⠛⣿⣿⠏⠀
    ⠀⠀⠀⠀⠀⢻⠀⠀⠀⠁⠀⠘⡄⠀⣠⢤⣀⡤⡄⢸⣿⣿⠋⠀⠀⠀⠀⠙⠁⠀⠀
    ⠀⠀⠀⠀⠀⣏⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠘⠛⢱⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣸⠁⠀⠀⠸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠃⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠹⡆⠀⠀⠀⣷⣄⢠⡀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⠃⠀⡄⠀⠀⠺⠾⠃⠀⠀⠀⠀⠾⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⣀⣀⡴⠋⠀⠛⠁⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢸⠁⠀⠀⠀⠀⣤⡄⠀⠀⠀⡴⠛⠲⡄⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⡇⠀⠀⠀⣀⠀⠘⠀⠀⣠⠞⠁⠀⠀⢣⠀⠀⠀⠀⠠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠘⠒⠒⠶⠁⠉⠉⠉⠉⠁⠀⠀⠀⠀⡞⠀⠀⠰⠇⠐⠛⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣼⠁⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠷⠤⠤⠤⠤⠿⠉⠁⠀⠀⠀⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠤⣤⣤⣀⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⢸⣄⠉⠁⠉⢉⡲⢤
    ⠀⠀⠀⢀⡠⠴⠊⣭⠃⠀⣀⣀⡤⠴⢶⠤⠤⢤⣀⠀⢸⠸⠈⠣⡀⢠⠃⠀⠀
    ⠀⢀⢔⡉⢀⣀⠐⠐⢧⣾⣴⣿⡿⠀⠀⡏⡄⠀⠀⢱⡧⢀⡠⠤⠬⣎⣧⠀⠀
    ⠐⠋⠁⠀⠀⢸⠔⢢⣿⣿⣿⡿⠃⠀⢠⠃⠀⠠⢚⣉⣠⢯⠀⠀⠀⠈⠛⠀⠀
    ⠀⠀⠀⠀⠀⠈⠀⣼⠙⠛⠉⠀⢀⣠⢊⠆⠀⠀⠈⣴⠃⣼⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡌⢦⣀⣀⠬⡺⠕⠁⠀⠀⠀⢀⠟⠸⡟⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡇⣀⠀⡦⢄⣠⣾⣿⣾⣦⠀⢀⠼⢱⠁⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠳⡏⠉⠁⣀⠈⠻⣿⣿⠉⠀⠈⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡏⠁⠈⠙⣿⢟⡀⢀⠄⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⡤⠀⡤⠃⠫⡉⠙⠃⠁⠀⠈⠠⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠰⠐⡀⠀⠀⠀⠀⣨⠆⠀⣀⠤⠒⠀⠙⠣⠤⠐⠒⠒⠄⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠊⡉⠀⠀⡜⠄⠀⠘⣏⡄⠀⣀⡠⠤⠠⢄⠘⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⢸⠀⡔⣳⠒⠒⠚⣿⠀⠰⢎⠀⠈⠁⠀⠀⠀⠀⢠⠇⡼⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠳⢌⡘⢄⡀⠀⠘⠦⣀⣉⣉⣁⠒⣄⠀⠀⠀⣸⢼⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⡧⣸⠀⠀⠀⠀⢠⠔⠋⢀⡼⠀⠀⠀⠉⠉⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠊⠁⠀⠀⠀⠀⠈⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠠⠤⠠⠤⠴⠠⠠⠠⠤⠤⠀⠠⠲⠀⠆⠤⠦⠴⠰⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⠀⡴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣧⠀⣾⠀⣰⠾⡇⠀⠀⢀⣶⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⡾⠤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢻⣾⠀⠸⣿⠋⣿⠃⢀⣷⣶⣴⠋⢹⠀⠀⠀⠀⠀⠀⠀⠀⢻⠳⣄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⡿⠦⠤⠿⢤⣀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠻⣀⣤⣻⣄⣀⣀⡉⠉⠹⠇⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⣸⠖⠚⣆⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣇⣀⣀⠤⠊⠈⢹⠶⣄⣀⣀⡤⠶⠚⠛⠉⠉⠉⠀⠀⠀⠉⠉⠙⠓⠲⠤⣾⣀⠀⠀⠀⢀⣠⡴⢾⠓⢤⣄⣸⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢻⡅⠀⠀⣠⠔⠁⡤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣞⠋⢇⠀⠈⠳⣄⣀⣸⠃⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠻⣖⠋⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡌⠳⢤⣀⣀⢠⠏⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠈⢦⣤⢟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⢀⡽⠋⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⠀⠀⣼⡧⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣤⠤⢴⠖⠘⡟⣃⣀⡀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⢰⡚⠛⡆⢠⡏⢉⢉⣿⡉⠉⣹⣏⠉⠉⣿⣉⠉⢹⣯⣁⣀⡿⣦⣶⣾⠆⠀⠘⢷⣤⠟⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠹⡆⠉⠉⠀⠀⠓⠖⠋⠈⠉⠉⠁⠙⠛⠛⠉⠙⠒⠛⠉⠉⠉⠀⠀⠉⠁⠀⠀⠀⠀⠀⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠴⠚⢿⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢺⡏⠙⠓⠶⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠈⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⠖⠁⠀⣾⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⣀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠈⠲⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣠⠞⠁⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠁⠀⠀⠀⠈⠉⠓⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠈⢢⡀⠀⠀⠀⠀
    ⠀⠀⢀⠞⠁⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠹⡄⠀⠀⠀
    ⠀⢠⠏⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠘⣆⠀⠀
    ⢀⡏⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠈⣇⠀
    ⠸⡇⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣆⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢸⡆
    ⠀⠹⢄⡀⠀⠀⣀⢾⡇⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⢸⠃
    ⠀⠀⠀⠉⠛⠛⠁⢸⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⡏⠳⣄⣀⣀⣀⠴⠃⠀
    ⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⡇⠀⠀⠉⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠀⠀⠀⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠜⠉⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠈⠙⠓⠶⠤⣤⣀⣀⣀⣀⣀⣀⣀⡤⠴⠒⠋⠁⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠲⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠈⠙⠓⠶⠤⣤⣤⣤⣤⣤⣤⣤⠤⣴⠖⠚⠋⠁⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⡀⠀⠀⠀⢀⣀⡼⠁⠀⠀⠀⠀⠀⠀⠘⢦⣤⣀⣀⣀⣀⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⢀⣤⣔⠲⢤⡖⢶⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⣴⠢⣄⡀⠀
    ⠀⢀⣤⣤⠤⣜⡿⠭⡤⠈⢳⣤⣀⡈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡤⢶⣿⡀⣠⣿⣴⣻⡇⠀
    ⠀⠘⠓⠓⢶⠈⢹⢀⡟⠀⣼⣡⠏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⣇⣻⣾⢻⠁⣨⣿⣭⣀⠀
    ⠀⠀⠀⢠⡿⠒⠋⠉⣉⣛⡻⠄⢀⡴⠋⠀⠀⠀⢀⣠⡶⠟⠉⠉⠉⠉⠛⠷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣀⣨⣇⣀⣸⣟⢁⣴⣻⣼⣷
    ⠀⢀⡶⠋⠐⠒⠒⠒⣏⠨⠭⠗⢯⡀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠀⠀⠀⠀⠀⠀⠀⢀⣠⠖⠻⠽⢩⡏⠀⠀⠉⢹⡟⠛⠋⠁
    ⠀⣼⣄⠀⠀⣰⠖⠑⠺⣗⠲⠆⢠⠇⠀⠀⢠⡏⠀⠀⠀⠀⣴⣻⣷⡆⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⢸⠁⠐⢶⣶⠯⠿⣕⠚⠁⠈⠻⡆⠀⠀
    ⢰⡟⡏⠒⠲⣄⠀⠀⠀⠈⢂⣠⠟⠀⠀⢀⣼⡇⠀⠀⠀⠀⠻⣿⡿⠃⠀⠀⠀⠀⠀⡏⠓⢦⣄⠀⠀⠀⠸⣆⠀⠈⠁⠀⠀⠼⠀⡀⠀⣠⣇⠀⠀
    ⢸⡿⣷⠀⠀⠈⠓⠲⣶⠞⠉⠁⠀⢀⣴⠟⠉⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠇⠀⠀⠈⢳⡀⠀⠀⠙⠷⣄⣀⣀⣀⡠⠞⠉⠉⣿⣼⠀⠀
    ⣿⣇⠈⠃⠀⠀⠀⢰⣇⣄⠀⠀⠀⡜⠁⠀⠀⠈⠻⣦⡀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠃⠀⠀⠀⠀⠀⢻⡀⠀⠀⠀⠀⣹⠉⠉⠀⠀⠀⢸⠟⡝⠀⠀
    ⡏⠛⠀⠀⠀⠀⠀⢸⣿⣗⠀⠀⣼⡥⠖⠒⠀⠀⠀⠈⠙⠻⠶⠶⠶⠶⠾⢛⠁⠀⠀⠀⠀⡀⠈⠉⠲⣇⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⠀⣰⣳⡄⠀
    ⢹⡄⠀⠀⠀⠀⠀⠀⠙⢿⣇⢰⠏⠀⢠⣶⢶⣦⣄⡀⠀⠀⠉⠒⠒⠒⠋⠁⠀⠀⣀⣴⣿⣿⣿⣦⠀⠘⡇⢀⣿⠟⠁⠀⠀⠀⠀⠀⠰⠋⢸⡇⠀
    ⠸⣷⠀⠀⠀⠀⠀⠀⠀⠘⠻⣾⠀⠀⢸⣿⣿⣧⣈⣿⣷⣤⣀⠀⠀⠀⠀⣀⣠⣾⣯⣼⣿⠛⣿⠏⠀⠀⢸⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀
    ⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠈⠻⣿⡿⢿⣿⣿⠀⠉⢻⣿⣿⣿⣿⣿⠛⠻⣿⣿⠟⠋⠀⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀
    ⠀⠀⠈⣷⡄⠀⠀⠀⠀⠀⠀⠸⣧⡄⠀⠀⠈⠙⠶⠼⣿⣿⣶⣿⣿⣿⣿⣀⣿⠶⠖⠋⠁⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⡴⡿⠃⠀⠀⠀
    ⠀⠀⠀⠈⢿⡳⠀⠀⠀⠀⠀⠀⠹⣽⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣠⡾⠃⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⢦⠀⠀⠀⠀⠀⠀⠙⢯⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣟⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⣠⡼⠋⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠷⣄⠀⠀⠀⠀⠀⠀⠀⠁⠘⠳⣤⢢⣄⠀⠀⠀⠀⠀⠀⣀⡀⢀⡴⠋⣰⠟⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⡀⠀⠀⠀⠀⠉⠻⠿⠲⢬⣆⣠⣞⣿⡵⢫⠖⠁⠀⠀⠀⠀⠀⡾⠁⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⢹⡀⡀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠘⠈⡴⠃⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠻⡿⣄⡀⣦⡀⠀⠀⠀⠀⠀⠀⠚⠁⠀⣀⡀⢀⣠⣾⡟⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣧⠤⠄⠀⠹⠌⠓⣿⠙⠷⣄⠀⠀⠀⡄⠀⣠⡴⣿⡵⠟⠹⠋⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣏⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠱⣄⣼⣿⠞⠋⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣠⡀⠀⠀⠀⡟⠳⠤⣄⣀⣀⠀⠀⠀⢀⣀⣀⣠⠤⠴⠚⡄⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠹⡷⣄⠀⠀⣷⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⣀⡇⠀⠀⢀⣴⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⢞⣁⣀⣀⣀⣈⣓⣤⣀⠙⣆⡀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣿⠁⣠⠴⢯⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢸⡟⡏⠁⠀⣀⣀⡽⠿⢿⣿⣷⢯⡩⠗⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢿⣟⠋⢹⣁⣀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠘⢧⢷⡖⠿⠟⢛⣏⠙⠲⡌⢻⣷⣷⢤⣀⠚⣧⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⢻⡘⣆⣨⠵⠚⠛⠛⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠛⢿⣆⡘⢉⣈⡉⠉⠙⠉⣁⣬⠟⡺⢵⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠳⣼⣉⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠒⠛⠿⢾⣵⣞⠁⠀⠒⣹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⣀⠉⠉⠙⠛⢛⣛⡫⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """,
            """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⣖⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄⠀⢰⣀⡼⡇⠀⠘⡆⠀⣀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⠿⠿⠛⣛⡿⠷⠶⣟⢷⡴⣧⣤⣰⡓⠉⡃⢀⣠⠄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠟⠋⠀⠀⢀⠞⠁⠀⠀⠀⠈⢳⣿⡟⠒⢿⣿⠢⡭⡝⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠋⠀⠀⣠⠤⠤⠼⣄⠀⠀⠿⠟⠀⡞⡿⢆⠀⠀⢻⣧⠙⢟⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣿⣿⠋⠀⠀⢠⠎⠀⢀⣀⠀⠈⢳⡀⠀⠀⣼⡾⣧⠀⠀⠀⠀⢏⠏⠈⢧⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣴⣿⡿⢁⡠⠔⠒⡞⠀⠀⠘⠿⠃⠀⢠⡿⢛⣿⡟⠓⠄⠀⠀⠀⠀⢸⢸⠀⠈⢆⠀⠀⠀⠀
    ⠀⠀⠀⠀⠰⢿⣿⣷⠋⠀⢀⣀⡙⢄⡀⠀⠀⠀⣠⣾⣷⣿⠋⠛⠀⠀⠀⠀⠀⠀⠈⡇⡧⢦⣼⡀⠀⠀⠀
    ⠀⠀⠀⠀⠘⣖⢺⣿⡀⠀⠘⠿⠃⠀⣹⢛⣿⠟⣋⠽⣾⡉⠃⠀⠀⠀⠀⠀⠀⠀⣀⡇⢡⠐⠂⡇⠀⠀⠀
    ⠀⢀⡆⢰⠺⣡⢋⣳⣵⣦⣤⣤⣤⣶⣿⣭⠶⡏⠙⠀⠈⠀⠀⠀⠀⢀⡤⠒⠉⢙⡢⡇⡘⠀⠀⢹⠀⠀⠀
    ⢀⡎⠣⠠⢧⠁⢸⢻⠹⡟⡇⠙⠇⠻⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⢀⣠⣬⠟⡱⠁⠀⠀⠸⡄⠀⠀
    ⠈⠧⣀⣀⠸⡄⠈⢆⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⡇⣤⣰⠾⢋⡥⠊⠀⠀⠀⠀⢤⡇⠀⠀
    ⠀⠀⢠⡿⡎⣧⢲⡈⢦⠳⡀⠀⠀⠀⠀⢀⡀⠀⢰⡄⢠⣜⣷⠼⠛⣩⠤⠚⠁⠀⠀⠀⠀⠀⠰⠚⡇⠀⠀
    ⠀⠀⠀⡠⢛⣿⠠⠍⠂⠑⢍⡢⠼⣦⣷⣼⡷⠼⡖⣛⣩⠥⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
    ⠀⠀⣴⡁⠾⢼⣀⣀⣀⣀⣀⣉⣑⣒⣒⣒⡓⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠠⠤⠤⠧⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠐⠒⠒⠤⠤⠤⠄⠀⠀⠀⠀⠈⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠀⠀⠀⠉⠉⠒⠒⠒⠈⠉
            """,
        ]
        self.type_list = ['fire', 'water', 'earth']
        self.boss = False

    # 캐릭터의 경험치가 100을 초과하면 레벨이 올라가고 스탯이 갱신됩니다.
    # 레벨이 3이 되면 보스 상태가 활성화됩니다.
    # 적의 체력과 공격력도 현재 레벨에 맞게 설정됩니다.
    def stats_update(self):
        if self.exp // 100 == 1:
            self.level += 1
            # print(self.level)
            print("당신의 파트너가 레벨 업했습니다!")
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            self.exp -= 100
            self.health = random.randint(10 * self.level, 20 * self.level)
            self.attack = random.randint(10 * self.level / 2, 20 * self.level / 2)
            if self.level == 3:
                self.boss = True

        self.evil_hp = random.randint(10 * self.level, 20 * self.level)
        self.evil_atk = random.randint(10 * self.level / 2, 20 * self.level / 2)
        self.evil_type = random.randint(1, 3)

    # 트레이너의 파트너의 상태를 출력하는 메서드입니다.
    def status(self):
        print(
            f"{self.trainer}의 파트너는 {self.level} 레벨, {self.health} 체력, {self.attack} 공격력, {self.type_list[self.type - 1]} 타입, 그리고 {self.exp} / 100 경험치를 가지고 있습니다.")

    # 게임의 오프닝 스크립트를 출력하고, 트레이너 이름을 받으며, 준비가 되었는지 묻는 메서드입니다.
    def opening(self):
        trainer = input("너의 이름은?\n")
        self.trainer = trainer
        if self.trainer == "unlimited":
            self.unlim()
        prepared = 'n'
        print("""

                             ▄█     █▄     ▄████████  ▄█        ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄████████
                            ███     ███   ███    ███ ███       ███    ███ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███
                            ███     ███   ███    █▀  ███       ███    █▀  ███    ███ ███   ███   ███   ███    █▀
                            ███     ███  ▄███▄▄▄     ███       ███        ███    ███ ███   ███   ███  ▄███▄▄▄
                            ███     ███ ▀▀███▀▀▀     ███       ███        ███    ███ ███   ███   ███ ▀▀███▀▀▀
                            ███     ███   ███    █▄  ███       ███    █▄  ███    ███ ███   ███   ███   ███    █▄
                            ███ ▄█▄ ███   ███    ███ ███▌    ▄ ███    ███ ███    ███ ███   ███   ███   ███    ███
                             ▀███▀███▀    ██████████ █████▄▄██ ████████▀   ▀██████▀   ▀█   ███   █▀    ██████████
        """)  # https://www.asciiart.eu/text-to-ascii-art
        opening_script = f"""
        ======================================================================================================================================

        Eldoria의 퀘스트에 오신 것을 환영합니다!

        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        {self.trainer}님, 환영합니다!

        Eldoria의 땅에서 그림자가 길어지고 절망의 속삭임이 바람에 실려오는 가운데, 어두운 세력이 세력을 확장하고 있습니다.
        악명 높은 말드락 왕이 아리아 공주를 납치하고 왕국의 희망을 빼앗았습니다.

        당신은 괴물을 다룰 수 있는 조련사로, 사납고 고귀한 생명체들과 함께 합니다.
        그러나 당신은 혼자가 아닙니다.

        당신과 함께할 강력한 동료가 있으며, 이 동물은 당신의 여정을 도울 것입니다.
        이 생명체는 당신의 손에 길들여졌으며, 다가오는 시험에서 당신을 돕고, 강력한 적들과 위험한 땅을 지나야 할 것입니다.

        당신의 퀘스트:

        1. 공주가 갇힌 어두운 성으로 향하세요.
        2. 당신의 동료와 함께 두려운 적들과 싸우며 공격, 치유, 적 약화 등을 결정하세요.
        3. 왕국의 운명이 당신의 손에 달려 있습니다. 당신의 힘과 지혜를 증명하세요.

        지혜를 가지고 선택하세요. 당신의 선택이 왕국의 운명을 결정할 것입니다.
        용기와 용맹을 가진 자만이 성공할 수 있습니다.

        준비를 마치고 여정을 시작하세요.
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """
        self.script_timer(opening_script)
        t = 0
        while prepared != 'y':
            text = "준비가 되었나" + " 이제" * t + "? (y/n)\n"
            prepared = input(text)
            t += 1
        print(
            "======================================================================================================================================")
        print("파트너의 속성을 선택하세요!")
        type_explanation = """
            타입에 대한 설명:
            불, 물, 땅의 타입이 있다.
            물은 불을 이기며, 불은 물에 비해 1.2배 더 강한 대미지를 준다.
            불은 물을 이길 때 대미지가 0.8배로 줄어든다.
            불 < 물 < 땅 < 불의 순서로 각 타입 간의 상성이 형성된다.
            """
        self.script_timer(type_explanation)
        print(self.type_list)
        # 번호는 타입을 나타냅니다.
        monster = -1
        t = 0
        while monster not in range(1, 4):
            monster = input("신중하게 선택하세요" + " 다시" * t + ": (1/2/3)\n")
            monster = int(monster) if monster.isnumeric() else -1
            t += 1
        print("훌륭한 선택입니다! 행운을 빕니다, 귀하의 동료 조련사!")
        self.type = monster
        # self.status()

    def chapters(self):
        if self.level == 1:
            print("""
                   █████████  █████                           █████                          ████
                  ███░░░░░███░░███                           ░░███                          ░░███
                 ███     ░░░  ░███████    ██████   ████████  ███████    ██████  ████████     ░███
                ░███          ░███░░███  ░░░░░███ ░░███░░███░░░███░    ███░░███░░███░░███    ░███
                ░███          ░███ ░███   ███████  ░███ ░███  ░███    ░███████  ░███ ░░░     ░███
                ░░███     ███ ░███ ░███  ███░░███  ░███ ░███  ░███ ███░███░░░   ░███         ░███
                 ░░█████████  ████ █████░░████████ ░███████   ░░█████ ░░██████  █████        █████
                  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░░        ░░░░░
                                                   ░███
                                                   █████
                                                  ░░░░░
            """)  # https://www.asciiart.eu/text-to-ascii-art
            print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⢠⢤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠔⠒⠒⠲⠎⠀⠀⢹⡃⢀⣀⠀⠑⠃⠀⠈⢀⠔⠒⢢⠀⠀⠀⡖⠉⠉⠉⠒⢤⡀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠚⠙⠒⠒⠒⠤⡎⠀⠀⠀⠀⢀⣠⣴⣦⠀⠈⠘⣦⠑⠢⡀⠀⢰⠁⠀⠀⠀⠑⠰⠋⠁⠀⠀⠀⠀⠀⠈⢦⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⢰⠃⠀⣀⣀⡠⣞⣉⡀⡜⡟⣷⢟⠟⡀⣀⡸⠀⡎⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣻⠀⠀⠀⠀
        ⢰⠂⠀⠀⠀⠀⠀⠀⠀⣗⠀⠀⢀⣀⣀⣀⣀⣀⣓⡞⢽⡚⣑⣛⡇⢸⣷⠓⢻⣟⡿⠻⣝⢢⠀⢇⣀⡀⠀⠀⠀⢈⠗⠒⢶⣶⣶⡾⠋⠉⠀⠀⠀⠀⠀
        ⠈⠉⠀⠀⠀⠀⠀⢀⠀⠈⠒⠊⠻⣷⣿⣚⡽⠃⠉⠀⠀⠙⠿⣌⠳⣼⡇⠀⣸⣟⡑⢄⠘⢸⢀⣾⠾⠥⣀⠤⠖⠁⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⢀⠀⠀
        ⠀⠀⠀⢰⢆⠀⢀⠏⡇⠀⡀⠀⠀⠀⣿⠉⠀⠀⠀⠀⠀⠀⠀⠈⢧⣸⡇⢐⡟⠀⠙⢎⢣⣿⣾⡷⠊⠉⠙⠢⠀⠀⠀⠀⠀⢸⡇⢀⠀⠀⠀⠀⠈⠣⡀
        ⠀⠀⠀⠘⡌⢣⣸⠀⣧⢺⢃⡤⢶⠆⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠋⢀⠔⣒⣚⡋⠉⣡⠔⠋⠉⢰⡤⣇⠀⠀⠀⠀⢸⡇⡇⠀⠀⠀⠀⠀⠀⠸
        ⠀⠀⠀⠀⠑⢄⢹⡆⠁⠛⣁⠔⠁⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⣿⢠⡷⠋⠁⠀⠈⣿⡇⠀⠀⠀⠈⡇⠉⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠑⣦⡔⠋⠁⠀⠀⠀⣿⠀⠀⢠⡀⢰⣼⡇⠀⡀⠀⠀⣿⠀⠁⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⡇⠀⠀⢴⣤⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⢨⣧⡿⠋⠀⠘⠛⠀⠀⣿⠀⠀⢀⠀⠀⠀⣿⣿⠀⠀⠀⠀⢲⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡧⡄⠀⠹⣇⡆⠀⠀⠀⠀⠀⣿⠀⢰⣏⠀⣿⣸⣿⣿⠀⠀⠀⠀⣼⠀⠀⠰⠗⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⢸⡇⣷⣛⣦⣿⢀⠈⠑⠀⢠⡆⣿⠐⢠⣟⠁⢸⠸⣿⣿⢱⣤⢀⠀⣼⠀⠀⢀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⢀⠀⠀⠀⢸⡇⠘⠫⣟⡇⠊⣣⠘⠛⣾⡆⢿⠀⠙⣿⢀⣘⡃⣿⣿⡏⠉⠒⠂⡿⠀⠰⣾⡄⠀⢸⡟⣽⣀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠘⣾⠀⠀⢸⡇⢸⣇⡙⠣⠀⣹⣇⠀⠈⠧⢀⣀⣀⡏⣸⣿⣇⢹⣿⡇⢴⣴⣄⣀⡀⢰⣿⡇⠀⢸⣇⢿⡿⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠓⠁⠈⠻⢷⠾⠦⠤⠬⣅⣹⣿⣖⣶⣲⣈⡥⠤⠶⡖⠛⠒⠛⠁⠉⠛⠮⠐⢛⡓⠒⢛⠚⠒⠒⠒⠛⣚⣫⡼⠿⠿⣯⠛⠤⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⡉⠉⠁⠀⠀⠘⠓⠀⠀⠀⠀⠀⣀⣞⡿⡉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            chapter1_dialogue = """
            여정이 시작되었도다
            엘도리아의 고대 숲을 지나가며, 그림자는 머무르고 오래된 속삭임이 공기를 채운다.
            땅과 이끼의 향기가 너를 둘러싸고 있지만, 불안감이 너의 감각을 자극한다.

            갑자기, 정적이 깨진다.
            덤불 속에서 낮은 으르렁거림이 들려오고, 그것은 사납고 굳건하다.
            괴물이 나타나며, 그 빛나는 눈이 너를 응시하고, 그 형태는 위엄 있고 위협적이다.

            너의 동료는 준비를 마쳤고, 전투를 준비하고 있다.
            이 괴물이 네 앞길을 막고 있다.

            무엇을 할 것인가?
            """
            self.script_timer(chapter1_dialogue)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif self.level == 2:
            print("""
                   █████████  █████                           █████                           ████████
                  ███░░░░░███░░███                           ░░███                           ███░░░░███
                 ███     ░░░  ░███████    ██████   ████████  ███████    ██████  ████████    ░░░    ░███
                ░███          ░███░░███  ░░░░░███ ░░███░░███░░░███░    ███░░███░░███░░███      ███████
                ░███          ░███ ░███   ███████  ░███ ░███  ░███    ░███████  ░███ ░░░      ███░░░░
                ░░███     ███ ░███ ░███  ███░░███  ░███ ░███  ░███ ███░███░░░   ░███         ███      █
                 ░░█████████  ████ █████░░████████ ░███████   ░░█████ ░░██████  █████       ░██████████
                  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░░        ░░░░░░░░░░
                                                   ░███
                                                   █████
                                                  ░░░░░
            """)
            print("""
               ^^                __..-:'':__:..:__:'':-..__
                             _.-:__:.-:'':  :  :  :'':-.:__:-._
                           .':.-:  :  :  :  :  :  :  :  :  :._:'.
                        _ :.':  :  :  :  :  :  :  :  :  :  :  :'.: _
                       [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
                       [ ]:  :  :  :  :  :  :  :  :  :  :  :  :  :[ ]
              :::::::::[ ]:__:__:__:__:__:__:__:__:__:__:__:__:__:[ ]:::::::::::
              !!!!!!!!![ ]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![ ]!!!!!!!!!!!
              ^^^^^^^^^[ ]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[ ]^^^^^^^^^^^
                       [ ]                                        [ ]
                       [ ]                                        [ ]
                 jgs   [ ]                                        [ ]
               ~~^_~^~/   \~^-~^~ _~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/   \~^ ~~_ ^
            """)  # https://www.asciiart.eu/buildings-and-places/bridges
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            chapter2_dialogue = """
            다리 앞에 이르다
            마침내, 너는 얽힌 숲의 품을 떠난다.
            너 앞에는 좁은 다리가 펼쳐져 있으며, 그 고대의 돌들은 시간과 전쟁에 의해 닳았다.
            그 다리는 깊고 커다란 협곡을 가로지르며, 그 아래로 바람이 울부짖는다.

            그러나 다가가자, 공기가 변한다.
            다리의 그림자 속에서 낮은 으르렁거림이 들려오고, 괴물 같은 형체가 나타난다.
            그 형태는 거대하고, 그 눈은 어둠 속에서 타오르는 불씨처럼 빛난다.
            이 괴물은 다리를 자신의 것으로 주장하며, 너가 방해 없이 지나가도록 허락하지 않을 것이다.

            너의 동료는 한 발짝 앞으로 나아가며, 흔들림 없이 전투를 준비한다.
            마음을 다잡아라, 앞으로 나아가는 길은 위험으로 가득하다!
            """
            self.script_timer(chapter2_dialogue)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        elif self.level == 3:
            print("""
                   █████████  █████                           █████                           ████████
                  ███░░░░░███░░███                           ░░███                           ███░░░░███
                 ███     ░░░  ░███████    ██████   ████████  ███████    ██████  ████████    ░░░    ░███
                ░███          ░███░░███  ░░░░░███ ░░███░░███░░░███░    ███░░███░░███░░███      ██████░
                ░███          ░███ ░███   ███████  ░███ ░███  ░███    ░███████  ░███ ░░░      ░░░░░░███
                ░░███     ███ ░███ ░███  ███░░███  ░███ ░███  ░███ ███░███░░░   ░███         ███   ░███
                 ░░█████████  ████ █████░░████████ ░███████   ░░█████ ░░██████  █████       ░░████████
                  ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░░░  ░███░░░     ░░░░░   ░░░░░░  ░░░░░         ░░░░░░░░
                                                   ░███
                                                   █████
                                                  ░░░░░
            """)
            print("""
                                                 !_
                                                  |*~=-.,
                                                  |_,-'`
                                                  |
                                                  |
                                                 /^\\
                   !_                           /   \\
                   |*`~-.,                     /,    \\
                   |.-~^`                     /#"     \\
                   |                        _/##_   _  \_
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
           |*`--,_- _        |            |*`~-.,= []  |
           |.-'|=     []     |   !_       |_.-"`_-     |
           |   |_=- -        |   |*`~-.,  |  |=_-      |
          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
      |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\\
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \\
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \\
     | _- =-     |-_   | ((* |      |= _=       | -    |___\\
     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
     |=_ =       | =_-_| |  | |     |   =_      | -_   |
     |_=-_       |=_=  | |  | |     |=_=        |=-    |
^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^
            """)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            chapter3_dialogue = """
            성에 이르다
            마침내, 성의 어두운 실루엣이 너 앞에 떠오른다. 그 첨탑은 폭풍에 가득한 하늘을 뚫고 솟아 있다.
            공기는 공포로 가득 차 있으며, 문이 삐걱거리며 열리고, 마치 운명을 부르고 있는 듯하다.
            성대한 홀 안에서, 그림자 속 왕좌에 앉은 말드락 왕이 차가운 시선으로 너를 바라본다.
            그의 옆에는 포로가 된 아리아 공주가 서 있으며, 그녀의 눈은 간청하지만 흔들림 없이 굳건하다.

            사악한 왕이 일어나며 그의 목소리는 천둥처럼 울린다.
            “그래, 네가 왔구나, 길들이는 자여, 나를 거역하려고? 네가 과연 자격이 있는지 보자!”

            어둠 속에서 괴물 같은 수호자가 나타난다. 그 힘은 네가 지금까지 만난 것과는 비교할 수 없다.
            너의 동료는 단호하게 서서, 이 마지막 시험을 준비한다.

            엘도리아를 위한 전투가 시작되었다!
            """
            self.script_timer(chapter3_dialogue)
            print(
                "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # the heart of this project
    # 위 코드는 플레이어가 싸울지 도망칠지를 선택하는 턴 기반 전투 시스템을 처리하며, 플레이어와 적의 행동에 따라 게임이 진행되고 한 쪽의 체력이 0에 도달할 때까지 계속됩니다.
    def fight_sequence(self):
        print("""
              █████▒██▓  ▄████  ██░ ██ ▄▄▄█████▓
            ▓██   ▒▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒
            ▒████ ░▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░
            ░▓█▒  ░░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░
            ░▒█░   ░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░
             ▒ ░   ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░
             ░      ▒ ░  ░   ░  ▒ ░▒░ ░    ░
             ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░
                    ░        ░  ░  ░  ░
        """)
        time.sleep(0.5)
        if not self.boss:
            print(self.evil[random.randint(0, 4)])
            time.sleep(0.15)
            appearance = """
            야생 괴물이 나타났다!
            그림자 속에서, 두려운 존재가 나타난다.
            그 눈은 굴하지 않는 분노로 타오르며, 그 자세는 치열한 도전을 말해준다.
            그 발걸음에 땅이 떨리며 다가오고 있다.
            전투를 준비하라!
            """
            self.script_timer(appearance)
        print(
            "======================================================================================================================================")
        print(f"악당은 {self.evil_hp}의 체력과 {self.evil_atk}의 공격력, 그리고 {self.type_list[self.evil_type - 1]} 속성을 가지고 있습니다.")
        time.sleep(0.15)
        print(
            f"{self.trainer}의 파트너는 {self.health}의 체력과 {self.attack}의 공격력, 그리고 {self.type_list[self.type - 1]} 속성을 가지고 있습니다.")
        time.sleep(0.15)
        fight_dialogue = [
            "적이 결연해 보입니다.",
            "적이 너를 살피고 있습니다.",
            "괴물이 사나운 으르렁거림을 냅니다!",
            "적이 망설이는 듯 보입니다.",
            "괴물이 좋지 않아 보입니다.",
            "적이 좌절한 것 같습니다.",
            "괴물이 고통에 움찔합니다.",
            "괴물이 공격할 준비가 된 것 같습니다.",
            "괴물이 약해 보입니다.",
            "괴물의 움직임이 둔해졌습니다.",
            "괴물이 분노에 찬 눈빛으로 너를 노려봅니다.",
            "괴물이 자신감 있어 보입니다.",
            "괴물이 비틀거리지만 균형을 되찾습니다.",
            "괴물이 시간을 끌고 있는 것 같습니다.",
            "괴물이 승리의 포효를 냅니다!"
        ]
        moves = ['attack', 'debuff', 'heal']
        fight_or_flight = -1
        compared = self.compare_type()
        enemy_hp = self.evil_hp
        enemy_atk = self.evil_atk
        my_hp = self.health
        my_atk = self.attack
        now_turn = 0
        while fight_or_flight not in ['fight', 'flight']:
            if self.boss:
                fight_or_flight = 'fight'
            else:
                fight_or_flight = input("싸우거나 도망칠래요? (fight/flight)\n")
        if fight_or_flight == 'flight':
            print("\nWomp Womp 너는 도망쳤다. 겁쟁이. 다음에 더 잘 하길 바란다!")
            time.sleep(0.15)
            print("(싸우지 않으면 게임이 진행되지 않고 무한 루프에 빠질 것입니다)\n")
            time.sleep(0.15)
            return 0
        elif fight_or_flight == "fight":
            while enemy_hp > 0 and my_hp > 0:
                move = -1
                if now_turn % 2 == 0:
                    while move not in moves:
                        move = input('네가 할 동작을 선택하세요! (attack/debuff/heal)\n')
                    if move == "attack":
                        deal = my_atk * (1 if compared == 0 else 1.2 if compared < 0 else 0.8)
                        deal = random.uniform(deal * 0.8, deal)
                        enemy_hp -= round(deal)
                        print(f"너가 공격했다! 공격한 데미지 {round(deal)}.")
                        time.sleep(0.15)
                    elif move == "debuff":
                        debuff = round(random.uniform(0.1, 0.4), 2)
                        enemy_atk -= enemy_atk * debuff
                        enemy_atk = round(enemy_atk)
                        print(f"너가 디버프를 사용했다! 적의 공격력이 {round(enemy_atk * debuff)}만큼 감소했다.")
                        time.sleep(0.15)
                    elif move == "heal":
                        heal = round(random.uniform(0.1, 0.4), 2)
                        my_hp += self.health * heal
                        my_hp = round(my_hp)
                        print(f"너가 회복했다! 너의 체력이 {round(self.health * heal)}만큼 회복됐다.")
                        time.sleep(0.15)
                        if my_hp > self.health:
                            my_hp = self.health

                else:
                    decision = random.randint(0, 2)
                    move = moves[decision]
                    # move = 'attack'
                    if move == "attack":
                        deal = enemy_atk * (1 if compared == 0 else 1.2 if compared > 0 else 0.8)
                        deal = random.uniform(deal * 0.8, deal)
                        my_hp -= round(deal)
                        print(f"괴물이 공격했다! 공격한 데미지 {round(deal)}.")
                        time.sleep(0.15)
                    elif move == "debuff":
                        debuff = round(random.uniform(0.1, 0.4), 2)
                        my_atk -= my_atk * debuff
                        my_atk = round(my_atk)
                        print(f"괴물이 디버프를 사용했다! 너의 공격력이 {round(my_atk * debuff)}만큼 감소했다.")
                        time.sleep(0.15)
                    elif move == "heal":
                        heal = round(random.uniform(0.1, 0.4), 2)
                        enemy_hp += self.evil_hp * heal
                        enemy_hp = round(enemy_hp)
                        print(f"괴물이 회복했다! 괴물의 체력이 {round(self.evil_hp * heal)}만큼 회복됐다.")
                        time.sleep(0.15)
                        if enemy_hp > self.evil_hp:
                            enemy_hp = self.evil_hp
                print(fight_dialogue[random.randint(0, 14)])
                print(f"너의 적은 {enemy_hp} / {self.evil_hp} 체력, {enemy_atk} / {self.evil_atk} 공격력을 가졌다.")
                time.sleep(0.15)
                print(f"너의 동료는 {my_hp} / {self.health} 체력, {my_atk} / {self.attack} 공격력을 가졌다.")
                time.sleep(0.15)
                print(
                    "======================================================================================================================================")
                now_turn += 1
        if my_hp <= 0:
            print("퀘스트 실패")
            return -1
        elif enemy_hp <= 0:
            print("너는 적을 처치했다!")
            time.sleep(0.15)
            exp_earned = random.randint(70, 100)
            print(f"너는 {exp_earned} 경험치를 얻었다")
            time.sleep(0.15)
            print(
                "======================================================================================================================================")
            self.exp += exp_earned
            return 1

    def compare_type(self):
        # ['fire', 'water', 'earth'] [1, 2, 3] 일반적으로 큰 인덱스 숫자가 이기지만 불이 땅을 이기므로 예외
        # 속성에 따라 공격력이 상승 및 하락합니다
        if self.type == 1 and self.evil_type == 3:
            return -1
        elif self.type == 3 and self.evil_type == 1:
            return 1
        if self.type > self.evil_type:
            return -1
        elif self.type < self.evil_type:
            return 1
        if self.type == self.evil_type:
            return 0

    # 플레이어의 현재 레벨에 따라 전투 대사를 설정합니다.
    def repeat(self):
        rep_dialogue = ""
        if self.level == 1:
            rep_dialogue = """
            ======================================================================================================================================
            여정이 계속된다
            숲은 점점 어두워지고, 공기는 불길한 기운으로 가득하다.
            그림자 속에서 바스락거리는 소리와 함께, 두려운 으르렁거림이 들린다.
            마지막보다 더 강력한 괴물이 나타나며, 눈은 분노로 타오르고 있다.

            동료는 준비를 마쳤다.
            다시 전투를 준비하라!
            ======================================================================================================================================
            """
        if self.level == 2:
            rep_dialogue = """
            ======================================================================================================================================
            괴물이 길을 막는다!
            다리를 건널 때, 바람이 너울거린다.
            그림자 속에서, 너의 길을 막고 있는 두려운 괴물이 나타난다.

            동료는 준비를 마쳤다.
            전투 준비를 하라!
            ======================================================================================================================================
                        """
        self.script_timer(rep_dialogue)

    # 최종 보스의 아트 및 스텟
    def boss_seq(self):
        boss_ani = """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠖⠲⠶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠘⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠶⠤⣌⠈⢷⣄⠀⠀⠀⠀⣠⠞⢀⣠⠶⠶⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠀⠈⢳⡄⣽⠛⠀⠀⠀⡁⣰⠏⠀⠀⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⣟⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠛⣿⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀⢀⣲⠟⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⠆⠀⠀⠈⣼⠁⠀⠀⠀⠀⠀⠀⠹⣿⡟⠂⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⢯⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⣸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀
        ⠀⠀⠀⢀⣴⠏⣀⣀⡀⣀⣀⣰⡟⣀⣀⣀⣀⣀⣀⣀⣀⣀⢀⣀⡀⢷⣀⣀⣀⣀⣀⣀⣳⣄⠀⠀⠀⠀
        ⠀⠀⠐⢻⡏⠉⠉⠉⢹⡉⠛⠛⠋⢉⡉⠉⠛⠉⢉⡍⠉⠉⠉⢩⡍⠉⠉⠉⣙⡉⠉⠉⠛⢹⠁⠀⠀⠀
        ⠀⠀⠀⢸⡇⠀⠀⣴⠋⠻⣄⠀⣰⠏⢻⣆⠀⣠⠟⠻⣆⠀⣠⠋⠹⣄⠀⣠⠏⠻⣆⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⠀⢸⡇⠀⠀⢿⡄⣴⠏⠀⢷⣦⣴⠟⠀⢻⣄⣴⠟⠈⢻⣄⢠⠟⠀⢿⣖⣴⠟⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⠀⣼⡇⠀⠀⠀⢹⠋⠀⡀⠀⢻⠏⠀⠀⠀⢻⡇⠀⠀⠀⢹⡏⠀⠀⠀⠹⠋⠀⠀⠀⢸⠀⠀⠀⠀
        ⠀⠀⣸⢿⡟⠛⢻⡛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⡟⠛⢳⠞⣧⠀⠀⠀
        ⠀⢠⡿⣸⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢸⡄⢹⡆⠀⠀
        ⠀⣼⣷⠟⣷⠀⠈⣿⠀⠀⠀⠀⣼⣦⡄⠀⠀⠀⠀⠀⠀⢀⣾⣦⠀⠀⠀⠀⠀⢠⡇⠀⣸⠃⠰⣳⠀⠀
        ⠀⡿⣿⠀⢻⠀⠀⢿⡀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠈⠋⠉⠀⠀⠀⠀⠀⢸⠀⠀⡇⠀⠀⣿⡄⠀
        ⢰⡇⠹⣦⢸⡆⠀⢸⡇⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢠⠃⢀⡼⠉⡇⠀
        ⢸⠇⠀⠈⠛⣷⡐⠘⡇⠀⠀⠀⠀⣠⡟⠁⠀⠀⠀⠀⠀⠈⢻⣄⠀⠀⠀⠀⢀⡿⠀⣸⠒⠋⠀⠀⣿⠀
        ⣿⠀⠀⠀⠀⢹⣇⠀⠿⣄⡀⠀⣴⠏⠷⣤⣤⣀⠀⣀⣤⡤⠾⠹⣧⠀⢀⣤⠞⠃⢰⠇⠀⠀⠀⠀⢿⡀
        ⣿⠀⠀⠀⠀⠀⢿⡄⠀⠈⠛⠾⠃⠀⢀⣤⣬⠉⠛⢉⣷⣄⠀⠀⠈⠷⠋⠁⠀⠀⡞⠀⠀⠀⠀⠀⢽⡇
        ⢹⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠸⣇⡉⠛⠛⠛⢃⣸⠇⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⣾⠀
        ⠸⠷⠶⠶⠶⠶⠶⠿⣇⠀⠀⠀⠀⠀⠀⠈⠉⠛⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⣸⠷⠶⠖⠒⠒⠀⠀⠁⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠦⣤⣀⡀⠀⠀⠀⠀⣀⣀⣤⠔⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                """
        print(boss_ani)
        self.evil_hp = random.randint(10 * self.level, 20 * self.level) * 1.5
        self.evil_atk = random.randint(10 * self.level / 2, 20 * self.level / 2) * 1.5
        self.evil_type = random.randint(1, 3)

    # 이 메서드는 승리 대사를 설정하고, 게임 완료 메시지와 무한 반복을 위한 이름을 알려줍니다.
    def winner(self):
        winner_dialogue = """
        가장 영광스러운 승리!
        너의 용기와 용맹이 어둠의 쇠사슬을 부수었고, 이제 공주 아리아는 마침내 자유를 얻었도다!
        사악한 왕 말드락은 패배하였고, 그의 공포의 통치는 끝이 났다.
        엘도리아 왕국은 기뻐하며, 너는 이 땅에 평화를 되돌려 놓았다.

        공주와 함께 너는 성으로 돌아가, 그곳에서 너를 위한 성대한 연회가 기다리고 있다.
        너의 용감함의 노래는 세대를 이어 성 홀을 울릴 것이다.

        그리고 이렇게 너는 퀘스트를 완료했으며, 왕국은 너의 보호 아래 번영할 것이다.
        "행복한 결말"이 바로 너의 이야기이며, 엘도리아의 음유시인들에 의해 영원히 불리리라.\n\n
        """
        self.script_timer(winner_dialogue)
        print("게임을 즐기셨기를 바랍니다.")
        time.sleep(0.5)
        print("무제한 기능이 열렸습니다! 끝없는 괴물 전투를 위해 'unlimited'라는 이름을 설정하세요.")

    # 스크립트 시간 설정
    def script_timer(self, script, timing=0.15):
        for line in script.split("\n"):
            print(line)
            time.sleep(timing)

    def unlim(self):
        while True:
            result = self.fight_sequence()
            if result == -1:
                print("Game Over")
                quit()
            test.stats_update()

language = "N/A"
while language not in range(1,3):
  language = input("English or Korean? (1/2)\n")
  language = int(language) if language.isnumeric() else language
test = Game() if language == 1 else Game_kor()
test.opening()
prev_level = 0
while test.level < 4:
    if test.level == prev_level + 1:
        prev_level += 1
        test.chapters()
        if test.level == 3:
            test.boss_seq()
    else:
        test.repeat()
    test.status()
    result = test.fight_sequence()
    if result == -1:
        print("Please restart!")
        quit()
    test.stats_update()
test.winner()
