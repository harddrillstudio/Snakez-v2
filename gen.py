from tkinter import *
from graphics import *
from Individual import Individual
from Population import Population
from Data_vars import DataVars

gvars = DataVars()

root = Tk()

w = Canvas(root, width=500, height=500)
w.pack()

pts = []

# Generate population
population = Population(gvars)

# Compute fitness
population.compute_fitness()


def update_target(event):
    global gvars
    gvars.target_x = event.x
    gvars.target_y = event.y


def update_origin(event):
    global gvars
    gvars.origin_x = event.x
    gvars.origin_y = event.y


def task():
    for i in range(population.pop_size):
        # Selection
        in1 = population.tournament_select()
        in2 = population.tournament_select()

        # print("Best: ", in1.get_fitness())
        # print("Best: ", in2.get_fitness())

        # Crossover
        population.individuals[i] = population.crossover(in1, in2)

        # Mutation
        population.individuals[i].mutate()

    # Compute fitness
    population.compute_fitness()

    # ___ RENDER ____
    w.delete(ALL)

    # Barriers
    for barrier in gvars.barriers:
        w.create_rectangle(barrier.get_bounds())

    w.create_oval(gvars.origin_x, gvars.origin_y, gvars.origin_x + 5, gvars.origin_y + 5)
    w.create_rectangle(gvars.target_x, gvars.target_y, gvars.target_x + 10, gvars.target_y + 10)
    w.create_text(100, 480, text="Best Fitness: " + str(population.get_best_fitness()))

    for indiv in population.individuals:
        pts = indiv.get_points()
        # indiv.print_indiv()

        for i in range(len(pts) - 1):
            # l = Line(pts[i], pts[i+1])
            w.create_line(pts[i].getX(), pts[i].getY(), pts[i + 1].getX(), pts[i + 1].getY())

    # if not population.get_best_fitness() < 2:
    #     # print()
    root.after(1, task)


w.bind("<B1-Motion>", update_target)
w.bind("<B3-Motion>", update_origin)
root.after(0, task)
root.mainloop()
