#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    def check_fill():
        if cell_is_filled() == False:           # проверяем закрашена ли клетка
            fill_cell()
    while wall_is_on_the_right() == False:      # двигаемся вправо, пока не увидим стену
        check_fill()
        move_right()


if __name__ == '__main__':
    run_tasks()
