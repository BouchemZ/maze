import turtle
import random

class Node:
    def __init__(self, height, width, ind=None, left_child=None, right_child=None):
        self.height = height
        self.width = width
        self.ind = ind
        self.left_child = left_child
        self.right_child = right_child

def gen_maze(HEIGHT, WIDTH):
    if HEIGHT < 1 or WIDTH < 1:
        return None

    if HEIGHT == 1 or WIDTH == 1:
        return Node(HEIGHT, WIDTH)

    if HEIGHT >= WIDTH:
        left_child = gen_maze(int(HEIGHT / 2), WIDTH)
        right_child = gen_maze(HEIGHT - int(HEIGHT / 2), WIDTH)
        ind = random.randint(0, WIDTH - 1)
        return Node(HEIGHT, WIDTH, ind, left_child, right_child)

    else:
        left_child = gen_maze(HEIGHT, int(WIDTH / 2))
        right_child = gen_maze(HEIGHT, WIDTH - int(WIDTH / 2))
        ind = random.randint(0, HEIGHT - 1)
        return Node(HEIGHT, WIDTH, ind, left_child, right_child)


def draw_maze(maze: Node):
    pen = turtle.Turtle()

    pen.up()
    pen.setpos(0, 0)
    pen.down()
    pen.forward(maze.width * 5)
    pen.right(90)
    pen.forward(maze.height * 5)
    pen.right(90)
    pen.forward(maze.width * 5)
    pen.right(90)
    pen.forward(maze.height * 5)
    pen.right(90)
    pen.up()

    node_pile = [maze]
    pos_pile = [[0, 0]]

    while len(node_pile) > 0:
        curr_node = node_pile.pop()
        curr_pos = pos_pile.pop()

        if curr_node.height == 1 or curr_node.width == 1:
            # leaf
            pass
        else:
            # move to top left corner of current room
            pen.setpos(x=curr_pos[0], y=curr_pos[1])

            if curr_node.height >= curr_node.width:
                pen.setpos(x=curr_pos[0], y=curr_pos[1] - 5 * int(curr_node.height / 2))
                pen.setheading(0)
                pen.down()
                pen.forward(curr_node.ind * 5)
                pen.up()
                pen.forward(5)
                pen.down()
                pen.forward((curr_node.width - curr_node.ind - 1) * 5)
                pen.up()
            else:
                pen.setpos(x=curr_pos[0] + 5 * int(curr_node.width / 2), y=curr_pos[1])
                pen.setheading(270)
                pen.down()
                pen.forward(curr_node.ind * 5)
                pen.up()
                pen.forward(5)
                pen.down()
                pen.forward((curr_node.height - curr_node.ind - 1) * 5)
                pen.up()

            # update the node_pile
            if curr_node.left_child is not None:
                node_pile.append(curr_node.left_child)
            if curr_node.right_child is not None:
                node_pile.append(curr_node.right_child)

            # update the pos_pile
            if curr_node.height >= curr_node.width:
                pos_pile.append(curr_pos)
                pos_pile.append([curr_pos[0], curr_pos[1] - 5 * int(curr_node.height / 2)])
            else:
                pos_pile.append(curr_pos)
                pos_pile.append([curr_pos[0] + 5 * int(curr_node.width / 2), curr_pos[1]])


my_maze = gen_maze(40, 70)

draw_maze(my_maze)

while True:
    pass
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
