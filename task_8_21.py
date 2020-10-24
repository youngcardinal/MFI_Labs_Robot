#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    def check_walls():
        if wall_is_above():
            for i in range(9):
                move_down()
        else:
            for i in range(9):
                move_up()

    def check_walls_2():
        if wall_is_on_the_left():
            for i in range(9):
                move_right()
        else:
            for i in range(9):
                move_left()

    check_walls()
    check_walls_2()


if __name__ == '__main__':
    run_tasks()
