import doctest


class Pencil:
    def __init__(self, length: float):
        """
        Создание и подготовка к работе объекта "Карандаш"

        :param length: Длина карандаша в сантиметрах

        Примеры:
        >>> pencil = Pencil(10.0)
        >>> pencil.length
        10.0
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина карандаша должна быть числом")
        if length <= 0:
            raise ValueError("Длина карандаша должна быть больше нуля")
        self.length = length

    def sharpen(self, amount: float) -> None:
        """
        Заточить карандаш, уменьшив его длину.

        :param amount: Сколько сантиметров убрать при заточке
        :raise ValueError: Если количество удаляемого материала превышает текущую длину карандаша, вызывается ошибка

        Примеры:
        >>> pencil = Pencil(10.0)
        >>> pencil.sharpen(0.5)
        >>> pencil.length
        9.5
        >>> pencil.sharpen(9.6)
        ...
        ValueError: Нельзя сточить карандаш больше его текущей длины
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество удаляемого материала должно быть числом")
        if amount <= 0:
            raise ValueError("Количество удаляемого материала должно быть положительным")
        if amount > self.length:
            raise ValueError("Нельзя сточить карандаш больше его текущей длины")
        self.length -= amount

    def use(self, amount: float) -> None:
        """
        Использовать карандаш, что также уменьшит его длину.

        :param amount: Сколько сантиметров карандаша будет израсходовано
        :raise ValueError: Если количество израсходованного превышает длину, вызывается ошибка

        Примеры:
        >>> pencil = Pencil(10.0)
        >>> pencil.use(1.5)
        >>> pencil.length
        8.5
        >>> pencil.use(8.6)
        ...
        ValueError: Нельзя использовать карандаш больше его текущей длины
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество израсходованного материала должно быть числом")
        if amount <= 0:
            raise ValueError("Количество израсходованного материала должно быть положительным")
        if amount > self.length:
            raise ValueError("Нельзя использовать карандаш больше его текущей длины")
        self.length -= amount


class Jacket:

    def __init__(self, size: str):
        """
        Создание и подготовка к работе объекта "Куртка"

        :param size: Размер куртки (например, "S", "M", "L")

        Примеры:
        >>> jacket = Jacket("M")
        >>> jacket.size
        'M'
        """
        if not isinstance(size, str):
            raise TypeError("Размер куртки должен быть типа str")
        self.size = size

    def wear(self) -> None:
        """
        Надеть куртку.

        Примеры:
        >>> jacket = Jacket("M")
        >>> jacket.wear()
        >>> # Если действие выполнилось без исключений, то считаем, что куртка надета
        """

    def take_off(self) -> None:
        """
        Снять куртку.

        Примеры:
        >>> jacket = Jacket("M")
        >>> jacket.wear()
        >>> jacket.take_off()
        >>> # Если действие выполнилось без исключений, то считаем, что куртка снята
        """


class Music:
    def __init__(self, total_duration: float, current_position: float):
        """
        Создание и подготовка к работе объекта "Музыка"

        :param total_duration: Общая продолжительность музыкального трека
        :param current_position: Текущее положение в проигрывании трека

        Примеры:
        >>> track = Music(300, 0)  # инициализация экземпляра класса
        """
        if not isinstance(total_duration, (int, float)):
            raise TypeError("Продолжительность музыкального трека должна быть типа int или float")
        if total_duration <= 0:
            raise ValueError("Продолжительность музыкального трека должна быть положительным числом")
        self.total_duration = total_duration

        if not isinstance(current_position, (int, float)):
            raise TypeError("Положение в треке должно быть int или float")
        if current_position < 0:
            raise ValueError("Положение в треке не может быть отрицательным числом")
        self.current_position = current_position

    def is_track_start(self) -> bool:
        """
        Проверка начала проигрывания трека

        :return: В начале ли трек

        Примеры:
        >>> track = Music(300, 0)
        >>> track.is_track_start()
        True
        """
        return self.current_position == 0

    def play_music(self, time: float) -> None:
        """
        Проигрывание музыки на определенное количество времени.

        :param time: Время проигрывания в секундах

        :raise ValueError: Если время проигрывания выходит за общую продолжительность, вызывается ошибка

        Примеры:
        >>> track = Music(300, 0)
        >>> track.play_music(30)
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время проигрывания должно быть типа int или float")
        if time < 0:
            raise ValueError("Время проигрывания должно быть положительным числом")
        if self.current_position + time > self.total_duration:
            raise ValueError("Время проигрывания выходит за общую продолжительность трека")
        self.current_position += time

    def rewind_music(self, time: float) -> None:
        """
        Перемотка проигрывания музыки на заданное количество времени.

        :param time: Время на которое происходит перемотка

        :raise ValueError: Если перемотка приводит к выходу за начало трека,
        вызывается ошибка и позиция трека не изменяется.

        Примеры:
        >>> track = Music(300, 150)
        >>> track.rewind_music(30)
        """
        if not isinstance(time, (int, float)):
            raise TypeError("Время перемотки должно быть типа int или float")
        if self.current_position - time < 0:
            raise ValueError("Перемотка не может привести к отрицательному значению позиции трека")
        self.current_position -= time


if __name__ == "__main__":
    doctest.testmod()
