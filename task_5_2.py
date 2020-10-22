#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_2():
    def check_wall():   # поверяем есть ли стена снизу, иначе "стоп"
        while wall_is_beneath() == True:
            move_right()
    check_wall()

if __name__ == '__main__':
    run_tasks()
