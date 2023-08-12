from .jlogr import (
        info as _info,
        debug as _debug,
        warning as _warning,
        error as _error,
        parse_list_of_logs as _parse_list_of_logs
        )

from typing import Optional

__all__ = ["info", "debug", "warning", "error", "parse_list_of_logs"]
__doc__ = """
Module for clean and colourful logging in python
This is just how i like my logs, so there aren't formatting options or anything like that.
If you want to change the format, feel free to make a fork.
"""

def info(message: str) -> None:
    """
    Log an info message to stdout

    # Example
    ```python
        import jlogr
        jlogr.info(\"Hello, world!\")
    ```

    # Output
    ```bash
        2021-08-15T21:04:05.000000000+00:00 :: [INFO] :: Hello, world!
    ```

    # Parameters
    - message: The message to log
    - module: The module that the message is coming from
    - function: The function that the message is coming from
    - class: The class that the message is coming from

    """
    ...

def debug(message: str) -> None:
    """
    Log a debug message
    # Example
    ```python
        import jlogr
        jlogr.debug(\"Hello, world!\")
    ```

    # Output
    ```bash
        2021-08-15T21:04:05.000000000+00:00 :: [DEBUG] :: Hello, world!
    ```

    # Parameters
    - message: The message to log
    - module: The module that the message is coming from
    - function: The function that the message is coming from
    - class: The class that the message is coming from
    """
    ...

def warning(message: str) -> None:
    """
    Log a message as a warning

    # Example
    ```python
        import jlogr
        jlogr.warning(\"Hello, world!\")
    ```

    # Output
    ```bash
        2021-08-15T21:04:05.000000000+00:00 :: [WARNING] :: Hello, world!
    ```

    # Parameters
    - message: The message to log
    - module: The module that the message is coming from
    - function: The function that the message is coming from
    - class: The class that the message is coming from
    """
    ...

def error(message: str) -> None:
    """
    Log a message as an error

    # Example
    ```python
        import jlogr
        jlogr.error(\"Hello, world!\")
    ```

    # Output
    ```bash
        2021-08-15T21:04:05.000000000+00:00 :: [ERROR] :: Hello, world!
    ```

    # Parameters
    - message: The message to log
    - module: The module that the message is coming from
    - function: The function that the message is coming from
    - class: The class that the message is coming from
    """
    ...

def parse_list_of_logs(
        logs: list[tuple[str, str, Optional[str], Optional[str], Optional[str]]]
        ) -> None:
    """
    Logs should be a list of tuples of strings, where the first string is the message \
            and the second
    string is the log level.

    # Example
    ```python
        import jlogr
        logs = [\
                (\"Hello, world!\", \"info\"), \
                (\"Hello, world!\", \"debug\"), \
                (\"Hello, world!\", \"warning\"), \
                (\"Hello, world!\", \"error\")]
        jlogr.parse_list_of_logs(logs)
    ```

    # Output
    ```bash
        2021-08-15T21:04:05.000000000+00:00 :: [INFO] :: Hello, world!
        2021-08-15T21:04:05.000000000+00:00 :: [DEBUG] :: Hello, world!
        2021-08-15T21:04:05.000000000+00:00 :: [WARNING] :: Hello, world!
        2021-08-15T21:04:05.000000000+00:00 :: [ERROR] :: Hello, world!
    ```

    # Parameters
    - logs: A list of tuples of strings, where the tuple is structured \
            (message, level, module, function, class)

    """
    ...


class Log:
    """
    A class representing a log
    """
    def __new__(
        cls,
        message: str,
        level: str,
        module: Optional[str],
        function: Optional[str],
        class_name: Optional[str],
        ) -> Log: ...

    @staticmethod
    def from_log_string(log_string: str) -> Log:
        """
        Create a log from a log string
        """
        ...

    def pretty_print(self):
        """
        Print the log to stdout
        """
        ...

# #[derive(Debug, Clone)]
# #[pyclass]
# pub enum LogLevel {
#     Info,
#     Debug,
#     Warning,
#     Error,
# }
#
# impl LogLevel {
#     fn color(&self) -> Color {
#         match self {
#             LogLevel::Info => Color::Green,
#             LogLevel::Debug => Color::Blue,
#             LogLevel::Warning => Color::Yellow,
#             LogLevel::Error => Color::Red,
#         }
#     }
#
#     fn prefix(&self) -> &'static str {
#         match self {
#             LogLevel::Info => "[INFO]",
#             LogLevel::Debug => "[DEBUG]",
#             LogLevel::Warning => "[WARNING]",
#             LogLevel::Error => "[ERROR]",
#         }
#     }
#     fn from_log_string(level: &str) -> Self {
#         match level {
#             "[INFO]" => LogLevel::Info,
#             "[DEBUG]" => LogLevel::Debug,
#             "[WARNING]" => LogLevel::Warning,
#             "[ERROR]" => LogLevel::Error,
#             _ => {
#                 println!("Invalid log level {}, setting to info.", level);
#                 LogLevel::Info
#             }
#         }
#     }
# }
#
# impl From<&str> for LogLevel {
#     fn from(level: &str) -> Self {
#         match level {
#             "info" => LogLevel::Info,
#             "debug" => LogLevel::Debug,
#             "warning" => LogLevel::Warning,
#             "error" => LogLevel::Error,
#             _ => {
#                 println!("Invalid log level {}, setting to info.", level);
#                 LogLevel::Info
#             }
#         }
#     }
#  }
