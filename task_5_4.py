#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    def find_wall():    # ищем стену внизу, пока её нет двигаемся вниз
        while wall_is_beneath() == False:
            move_down()
    def check_wall():   # поверяем есть ли стена снизу, иначе "стоп"
        while wall_is_beneath() == True:
            move_right()
    find_wall()
    check_wall()
    move_down()
    while wall_is_on_the_left() == False:   # двигаемся влево, пока не увидим стену
        move_left()

if __name__ == '__main__':
    run_tasks()
