# -*- coding: utf-8 -*-
import random
import time
import simple_draw as sd

sd.resolution = (1200, 600)

def draw_buble(position, radius=50, step=5, color=sd.COLOR_GREEN, width=1):

    for y in range(3):
        sd.circle(center_position=position, radius=radius, color=color, width=width)
        radius += step

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
buble_position = sd.get_point(300, 300)
draw_buble(position=buble_position, radius=50)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


