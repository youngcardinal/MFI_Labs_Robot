#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
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
    while not wall_is_on_the_right():      # двигаемся вправо, пока не увидим стену
        check_wall_above()
        check_wall_beneath()
        move_right()
    check_wall_above()
    check_wall_beneath()


if __name__ == '__main__':
    run_tasks()
