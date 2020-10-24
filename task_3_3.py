#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if not wall_is_above():            # проверяем наличие стены сверху
        move_up()
    elif not wall_is_on_the_right():   # проверяем наличие стены справа
        move_right()
    elif not wall_is_beneath():        # проверяем наличие стены снизу
        move_down()
    else:
        move_left()                         # иначе двигаемся влево


if __name__ == '__main__':
    run_tasks()
