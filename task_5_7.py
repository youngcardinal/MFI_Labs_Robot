#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_7():
    for i in range(11):         # цикл работает только для заданного диапазона клеток
        if wall_is_above() == True:
            move_right()
        else:
            if wall_is_beneath() == True:
                move_right()
            else:
                pass


if __name__ == '__main__':
    run_tasks()
