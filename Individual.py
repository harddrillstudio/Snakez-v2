from graphics import *
import random
import math


def intersect(e1, e2):
    if e1[0] < e2.get_bounds()[2] and e1[2] > e2.get_bounds()[0]:
        if e1[1] < e2.get_bounds()[3] and e1[3] > e2.get_bounds()[1]:
            return True
    else:
        return False


def distance(p1, p2):
    return math.sqrt(((p1.getX()-p2.getX())**2) + ((p1.getY()-p2.getY())**2))


class Individual:
    genes = []
    fitness = 0

    segment_length = 20
    segment_quantity = 20
    last_x, last_y = 0, 0
    gvars = None

    def __init__(self, gvars):
        self.genes = []
        self.gvars = gvars
        for i in range(self.segment_quantity):
            self.genes.append(random.random() * math.pi * 3)

    def barrier_collision(self, x, y):
        to_return = False
        for barrier in self.gvars.barriers:
            if intersect([x, y, x, y], barrier):
                to_return = True
        return to_return

    def get_points(self):
        x, y = self.gvars.origin_x, self.gvars.origin_y

        points = list()
        points.append(Point(x, y))

        for i in range(self.segment_quantity):
            dx = math.cos(self.genes[i]) * self.segment_length
            dy = math.sin(self.genes[i]) * self.segment_length

            x += dx
            y += dy

            # Barriers break snake
            if self.barrier_collision(x, y):
                self.last_x = x
                self.last_y = y
                break

            points.append(Point(x, y))

            if i == self.segment_quantity - 1:
                self.last_x = x
                self.last_y = y
        return points

    def get_fitness(self):
        self.get_points()
        self.fitness = distance(Point(self.last_x, self.last_y),
                                Point(self.gvars.target_x, self.gvars.target_y))
        return self.fitness

    def print_indiv(self):
        print('Fitness: ', self.fitness)

    def mutate(self):
        for i in range(self.segment_quantity):
            if random.random() <= self.gvars.mutation_rate:
                self.genes[i] += (1 - random.random() * math.pi ) / 2
