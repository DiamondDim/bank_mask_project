import pytest
from src.decorators import log
from pathlib import Path


# Тестовая функция для проверки успешного выполнения
@log()
def successful_function(a: int, b: int) -> int:
    """Функция для тестирования успешного выполнения"""
    return a + b


# Тестовая функция для проверки ошибок
@log()
def failing_function(a: int, b: int) -> int:
    """Функция для тестирования обработки ошибок"""
    raise ValueError("Test error")


def test_log_decorator_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирование вывода в консоль при успешном выполнении"""
    result = successful_function(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "Вызов функции successful_function" in captured.out
    assert "Функция successful_function успешно выполнена" in captured.out
    assert "Результат: 5" in captured.out


def test_log_decorator_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Тестирование вывода в консоль при ошибке"""
    with pytest.raises(ValueError, match="Test error"):
        failing_function(2, 3)

    captured = capsys.readouterr()
    assert "Вызов функции failing_function" in captured.out
    assert "Функция failing_function вызвала исключение ValueError" in captured.out


def test_log_decorator_file_success(tmp_path: Path) -> None:
    """Тестирование записи в файл при успешном выполнении"""
    log_file = tmp_path.joinpath("test_log.txt")

    @log(filename=str(log_file))
    def file_success_function(x: int, y: int) -> int:
        """Функция для тестирования записи в файл"""
        return x * y

    result = file_success_function(4, 5)
    assert result == 20

    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
        assert "Вызов функции file_success_function" in log_content
        assert "Функция file_success_function успешно выполнена" in log_content
        assert "Результат: 20" in log_content


def test_log_decorator_file_error(tmp_path: Path) -> None:
    """Тестирование записи в файл при ошибке"""
    log_file = tmp_path.joinpath("test_log_error.txt")

    @log(filename=str(log_file))
    def file_failing_function(x: int, y: int) -> int:
        """Функция для тестирования ошибок при записи в файл"""
        raise TypeError("File test error")

    with pytest.raises(TypeError, match="File test error"):
        file_failing_function(1, 2)

    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
        assert "Вызов функции file_failing_function" in log_content
        assert "Функция file_failing_function вызвала исключение TypeError" in log_content
