#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    def check_cell():                   # проверить закрашена ли ячейка
        while not cell_is_filled():
            move_up()
    check_cell()
    move_right()
    if not cell_is_filled():
        move_left(2)


if __name__ == '__main__':
    run_tasks()
