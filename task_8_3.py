#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    def check_wall():
        if wall_is_above():           # проверяем есть ли стена сверху
            fill_cell()
            move_right()
        elif wall_is_beneath():
            fill_cell()
            move_right()
        else:
            move_right()
    while not wall_is_on_the_right():       # двигаемся вправо, пока не увидим стену
        check_wall()

    if wall_is_above():
        fill_cell()
    elif wall_is_beneath():
        fill_cell()


if __name__ == '__main__':
    run_tasks()
