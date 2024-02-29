import sys
import pytest
import math
import matplotlib.pyplot as plt
import numpy as np
import itertools as it

class Vertex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return abs(self.x - other.x) < 0.00001 and abs(self.y - other.y) < 0.00001

    def __repr__(self):
        return "({0}, {1})".format(round(self.x, 2), round(self.y, 2))


    def __iter__(self):
        yield self.x
        yield self.y


 

height = 1 / 2 * (3 ** 0.5)
standard_triangle = [(0, 0), (1 / 4, height / 2), (1 / 2, height), (3 / 4, height / 2), (1, 0), (1 / 2, 0), (1 / 2, height / 3)]
standard_triangle = [Vertex(x, y) for (x, y) in standard_triangle]

def generate_triangle(size):
    vertices = []

    print("Creating vertices")
    def try_add_vertex(vertex):
        for other in vertices:
            if vertex == other:
                return
        vertices.append(vertex)

    # generate list of vertices
    for y_index in range(size):
        for x_index in range(size - y_index):
            corner_y = y_index * height
            corner_x = x_index + y_index * 0.5
            for vertex in standard_triangle:
                x, y = vertex.x, vertex.y
                try_add_vertex(Vertex(x + corner_x, y + corner_y))
                if y_index > 0:
                    try_add_vertex(Vertex(x + corner_x, - y + corner_y))

    print("Created {0} vertices".format(len(vertices)))

    print("Looking for lines (1 / 6).")

    adjacency_matrix = np.zeros([len(vertices), len(vertices)])
    line_lengths = []

    # Horizontal lines
    for y_index in range(size):
        line = []
        for (i, vertex) in enumerate(vertices):
            if abs(vertex.y - y_index * height) < 0.00001:
                line.append(i)

        for (i, j) in it.combinations(line, 2):
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1
        if len(line) > 2:
            line_lengths.append(len(line))

    print("Looking for lines (2 / 6).")
    # Vertical lines
    for x_index in range(2 * size):
        x_coord = x_index * 0.5
        line = []
        for (i, vertex) in enumerate(vertices):
            if abs(vertex.x - x_coord) < 0.00001:
                line.append(i)

        for (i, j) in it.combinations(line, 2):
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1
        if len(line) > 2:
            line_lengths.append(len(line))


    print("Looking for lines (3 / 6).")
    # 30 degree lines
    for x_index in range(size):
        for y_index in range(size):
            if x_index > 0 and y_index > 0:
                continue
            line = []
            corner_y = y_index * height
            corner_x = x_index + y_index * 0.5

            for (i, vertex) in enumerate(vertices):
                if vertex == Vertex(corner_x, corner_y):
                    line.append(i)
                    continue
                elif vertex.x == corner_x:
                    continue
                slope = (vertex.y - corner_y) / (vertex.x - corner_x) 
                if abs(slope - 2 / 3 * height) < 0.00001:
                    line.append(i)

            for (i, j) in it.combinations(line, 2):
                adjacency_matrix[i, j] = 1
                adjacency_matrix[j, i] = 1
            if len(line) > 2:
                line_lengths.append(len(line))

    print("Looking for lines (4 / 6).")
    # 60 degree lines
    for x_index in range(size):
        line = []
        corner_y = 0
        corner_x = x_index

        for (i, vertex) in enumerate(vertices):
            if vertex == Vertex(corner_x, corner_y):
                line.append(i)
                continue
            elif vertex.x == corner_x:
                continue
            slope = (vertex.y - corner_y) / (vertex.x - corner_x) 
            if abs(slope - 2 * height) < 0.00001:
                line.append(i)

        for (i, j) in it.combinations(line, 2):
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1
        if len(line) > 2:
            line_lengths.append(len(line))

    print("Looking for lines (5 / 6).")
    # -30 degree lines
    for x_index in range(1, 2 * size):
        line = []
        corner_y = x_index * height / 2
        corner_x = x_index / 4

        for (i, vertex) in enumerate(vertices):
            if vertex == Vertex(corner_x, corner_y):
                line.append(i)
                continue
            elif vertex.x == corner_x:
                continue
            slope = (vertex.y - corner_y) / (vertex.x - corner_x) 
            if abs(slope - (-2 / 3 * height)) < 0.00001:
                line.append(i)

        for (i, j) in it.combinations(line, 2):
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1
        if len(line) > 2:
            line_lengths.append(len(line))


    print("Looking for lines (6 / 6).")
    # -60 degree lines
    for x_index in range(size):
        line = []
        corner_y = 0
        corner_x = x_index + 1

        for (i, vertex) in enumerate(vertices):
            if vertex == Vertex(corner_x, corner_y):
                line.append(i)
                continue
            elif vertex.x == corner_x:
                continue
            slope = (vertex.y - corner_y) / (vertex.x - corner_x) 
            if abs(slope - (-2 * height)) < 0.00001:
                line.append(i)

        for (i, j) in it.combinations(line, 2):
            adjacency_matrix[i, j] = 1
            adjacency_matrix[j, i] = 1

        if len(line) > 2:
            line_lengths.append(len(line))

    # generate lines
    return vertices, adjacency_matrix, line_lengths


def count_triangles(size):
    print("Generating triangle...")
    vertices, adjacency_matrix, line_lengths = generate_triangle(size)

    # for (i, v1), (j, v2) in it.combinations(enumerate(vertices), 2):
    #     if adjacency_matrix[i, j]:
    #         plt.plot([v1.x, v2.x], [v1.y, v2.y])

    # plt.scatter(*zip(*[(vertex.x, vertex.y) for vertex in vertices]))
    # plt.show()

    triangle_count = 0
    neighbour_table = [set() for _ in range(len(vertices))]

    print("Generating fast neighbour table...")
    for (i, j) in it.combinations(range(len(vertices)), 2):
        if i != j and adjacency_matrix[i, j]:
            neighbour_table[i].add(j)
            neighbour_table[j].add(i)


    print("Looking for triangles...")
    for i in range(len(vertices)):
        for j in neighbour_table[i]:
            for k in neighbour_table[i].intersection(neighbour_table[j]):
                assert i != j and j != k and i != k
                triangle_count += 1

    for length in line_lengths:
        triangle_count -= (length * (length - 1) * (length - 2))

    return triangle_count / 6

print(count_triangles(45))
