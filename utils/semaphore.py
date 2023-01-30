"""Scripts usefull to check semaphore

    2023 Juan Luis Ruiz Vanegas (juanluisruiz971@gmail.com)
"""


class Semaphore():

    def __init__(self):
        self.semaphore = open('semaphore.dat')

    def read_config(self):
        self.status = self.semaphore.read(1)

    def set_false(self):
        self.status = 0