from Barrier import Barrier


class DataVars:
    origin_x, origin_y = 50, 50
    target_x, target_y = 260, 300
    mutation_rate = 0.1

    barriers = []

    def __init__(self):
        self.barriers.append(Barrier(230, 100, 200, 50))
        self.barriers.append(Barrier(0, 100, 200, 50))
