#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    def check_wall_above():
        if not wall_is_above():           # проверяем есть ли стена сверху
            fill_cell()
    while not wall_is_on_the_right():      # двигаемся вправо, пока не увидим стену
        check_wall_above()
        move_right()
    check_wall_above()


if __name__ == '__main__':
    run_tasks()
