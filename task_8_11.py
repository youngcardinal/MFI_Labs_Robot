#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    def check_wall_above():
        if not wall_is_above():           # проверяем есть ли стена сверху
            move_up()
            fill_cell()
            move_down()

    def check_wall_beneath():
        if not wall_is_beneath():           # проверяем есть ли стена снизу
            move_down()
            fill_cell()
            move_up()

    def check_fill():
        if not cell_is_filled():
            fill_cell()

    check_fill()
    while not wall_is_on_the_right():      # двигаемся вправо, пока не увидим стену
        if not check_wall_above() and not check_wall_beneath():
            fill_cell()
            move_right()


if __name__ == '__main__':
    run_tasks()
