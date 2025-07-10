import datetime
from typing import Callable, Any, Optional, TypeVar, cast
from functools import wraps

T = TypeVar('T', bound=Callable[..., Any])


def log(filename: Optional[str] = None) -> Callable[[T], T]:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для записи логов. Если None, логи выводятся в консоль.

    Returns:
        Декорированную функцию с логированием.
    """

    def decorator(func: T) -> T:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Формируем сообщение о начале выполнения
            start_time = datetime.datetime.now()
            log_message = (
                f"{start_time} - Вызов функции {func.__name__} с аргументами: "
                f"args={args}, kwargs={kwargs}"
            )

            try:
                # Вызываем исходную функцию
                result = func(*args, **kwargs)

                # Формируем сообщение об успешном выполнении
                end_time = datetime.datetime.now()
                duration = end_time - start_time
                success_message = (
                    f"{end_time} - Функция {func.__name__} успешно выполнена. "
                    f"Результат: {result}. Время выполнения: {duration}"
                )

                # Записываем или выводим сообщение
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message + '\n')
                        f.write(success_message + '\n')
                else:
                    print(log_message)
                    print(success_message)

                return result

            except Exception as e:
                # Формируем сообщение об ошибке
                error_time = datetime.datetime.now()
                duration = error_time - start_time
                error_message = (
                    f"{error_time} - Функция {func.__name__} вызвала исключение {type(e).__name__}: {e}. "
                    f"Аргументы: args={args}, kwargs={kwargs}. Время выполнения до ошибки: {duration}"
                )

                # Записываем или выводим сообщение
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(log_message + '\n')
                        f.write(error_message + '\n')
                else:
                    print(log_message)
                    print(error_message)

                raise

        return cast(T, wrapper)

    return decorator
