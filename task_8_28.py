#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    def check_wall():
        while not wall_is_on_the_right():
            if not wall_is_above():
                move_up()
            else:
                move_right()

    def check_wall_2():
        while not wall_is_on_the_left():
            if not wall_is_above():
                move_up()
            else:
                move_left()

    check_wall()
    check_wall_2()


if __name__ == '__main__':
    run_tasks()
