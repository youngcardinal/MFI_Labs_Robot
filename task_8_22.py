#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    def check_wall():
        while not wall_is_above():
            move_up()

    def check_div():
        if wall_is_on_the_left():
            while not wall_is_on_the_right():
                move_right()
        else:
            while not wall_is_on_the_left():
                move_left()
    check_wall()
    check_div()


if __name__ == '__main__':
    run_tasks()
