#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_3():
    def check_wall():   # поверяем есть ли стена снизу, иначе "стоп"
        while wall_is_beneath() == True:
            move_right()
    move_right()        # делаем первый шаг без проверки наличия стены
    check_wall()


if __name__ == '__main__':
    run_tasks()
