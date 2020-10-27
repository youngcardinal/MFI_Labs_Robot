#!/usr/bin/python3

from pyrob.api import *


@task
def task_4_3():
    def right_way():            # проход строки вправо
        for i in range(27):
            fill_cell()
            move_right()
        move_down()
        move_left()

    def left_way():             # проход строки влево
        for i in range(27):
            fill_cell()
            move_left()
        move_down()
        move_right()

    move_right()
    for i in range(6):          # цикл проходов
        right_way()
        left_way()


if __name__ == '__main__':
    run_tasks()
