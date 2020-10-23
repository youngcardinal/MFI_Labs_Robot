#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    def check_fill():
        if cell_is_filled() == False:           # проверяем закрашена ли клетка
            fill_cell()
    for i in range(4):
        check_fill()
        move_right()
        check_fill()
        move_down()


if __name__ == '__main__':
    run_tasks()
