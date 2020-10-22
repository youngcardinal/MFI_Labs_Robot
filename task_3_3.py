#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if wall_is_above() == False:            # проверяем наличие стены сверху
        move_up()
    elif wall_is_on_the_right() == False:   # проверяем наличие стены справа
        move_right()
    elif wall_is_beneath() == False:        # проверяем наличие стены снизу
        move_down()
    else:
        move_left()                         # иначе двигаемся влево


if __name__ == '__main__':
    run_tasks()
