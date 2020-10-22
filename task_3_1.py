#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_1():
    def check_wall():
        if wall_is_on_the_right() == False:
            move_right()
    for i in range(9):
        check_wall()


if __name__ == '__main__':
    run_tasks()
