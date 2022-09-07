# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев

class Unit:
    def move_unit_on_field(self, field, field_1_param, field_2_param, direct, is_fly, is_creep, base_speed=1):
        """Функция реализует перемещение юнита по полю. В качестве параметров принимает текущие координаты юнита,
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param field_1_param: x-координата юнита
        :param field_2_param: у- координата юнита
        :param direct: направление перемещения
        :param is_fly: летит ли юнит
        :param is_creep: крадется ли юнит
        :param base_speed: базовый параметр скорости
        """
        # Для начала проверим не установлены ли у нас два флага полета и подкрадывания в истину,
        # т.к. одновременно эти события не должны происходить

        if is_fly and is_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            base_speed *= 1.2
            if direct == 'UP':
                new_y = field_2_param + base_speed
                new_x = field_1_param
            elif direct == 'DOWN':
                new_y = field_2_param - base_speed
                new_x = field_1_param
            elif direct == 'LEFT':
                new_y = field_2_param
                new_x = field_1_param - base_speed
            elif direct == 'RIGHT':
                new_y = field_2_param
                new_x = field_1_param + base_speed
        if is_creep:
            base_speed *= 0.5
            if direct == 'UP':
                new_y = field_2_param + base_speed
                new_x = field_1_param
            elif direct == 'DOWN':
                new_y = field_2_param - base_speed
                new_x = field_1_param
            elif direct == 'LEFT':
                new_y = field_2_param
                new_x = field_1_param - base_speed
            elif direct == 'RIGHT':
                new_y = field_2_param
                new_x = field_1_param + base_speed

            field.set_unit(x=new_x, y=new_y, unit=self)

# class Unit:
#     # ...
#     def mvmntobjbfld(self, field, feld_1_param, field_2_param, d, fl, cr, points_per_action = 1):
#         """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита,
#         направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с
#         которым двигается юнит
#         :param field: поле по которому перемещается юнит
#         :param feld_1_param: x-координата юнита
#         :param field_2_param: у- координата юнита
#         :param d: направление перемещения
#         :param fl: летит ли юнит
#         :param cr: крадется ли юнит
#         :param points_per_action: базовый параметр скорости
#         """
#         # Для начала проверим не установлены ли у нас два флага полета и подкрадывания в истину,
#         # т.к. одновременно эти события не должны происходить
#         if fl and cr:  # если оба параметра установлены как True
#             # выбросим ошибку
#             raise ValueError('Рожденный ползать летать не должен!')
#         # Если ошибку мы не выбросили, значит все у нас ок и в принципе мы можем переходить к дальнейшему выполнению кода
#
#         if fl:  # для начала реализуем логику для состояния когда мы летим
#             points_per_action *= 1.2 # раз мы летим то сцепления наших тапочек с землей нет, и следовательно трение меньше, и поэтому скорость выше
#             if d == 'UP':  # если направление нашего движения установлено как UP
#                 new_y = field_2_param + points_per_action   # увеличим нашу координату Y на нашу текущую скорость
#                 new_x = feld_1_param  # оставим нашу координату Х без изменений
#             elif d == 'DOWN':  # если направление нашего движения установлено как DOWN
#                 new_y = field_2_param - points_per_action   # уменьшим нашу координату Y на нашу текущую скорость
#                 new_x = feld_1_param  # оставим нашу координату Х без изменений
#             elif d == 'LEFT':  # если направление нашего движения установлено как LEFT
#                 new_y = field_2_param  # оставим нашу координату Y без изменений
#                 new_x = feld_1_param - points_per_action # уменьшим нашу координату Х на нашу текущую скорость
#             elif d == 'RIGHT':  # если направление нашего движения установлено как RIGHT
#                 new_y = field_2_param  # оставим нашу координату Y без изменений
#                 new_x = feld_1_param + points_per_action # увеличим нашу координату Х на нашу текущую скорость
#         if cr:
#             points_per_action *= 0.5
#             if d == 'UP':  # если направление нашего движения установлено как UP
#                 new_y = field_2_param + points_per_action  # увеличим нашу координату Y на нашу текущую скорость
#                 new_x = feld_1_param  # оставим нашу координату Х без изменений
#             elif d == 'DOWN':  # если направление нашего движения установлено как DOWN
#                 new_y = field_2_param - points_per_action  # уменьшим нашу координату Y на нашу текущую скорость
#                 new_x = feld_1_param  # оставим нашу координату Х без изменений
#             elif d == 'LEFT':  # если направление нашего движения установлено как LEFT
#                 new_y = field_2_param  # оставим нашу координату Y без изменений
#                 new_x = feld_1_param - points_per_action  # уменьшим нашу координату Х на нашу текущую скорость
#             elif d == 'RIGHT':  # если направление нашего движения установлено как RIGHT
#                 new_y = field_2_param  # оставим нашу координату Y без изменений
#                 new_x = feld_1_param + points_per_action  # увеличим нашу координату Х на нашу текущую скорость
#
#             field.set_unit(x=new_x, y=new_y, unit=self)

#     ...