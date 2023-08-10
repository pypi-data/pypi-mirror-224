import copy
from logging import StreamHandler, Formatter, LogRecord
from typing import Callable


class EnhancedStreamHandler(StreamHandler):
    def __init__(
            self,
            stream=None,
            level: int = 0,
            formatter: Formatter | None = None,
            msg_func: Callable[[str], str] | None = None):
        super().__init__(stream)
        self.setFormatter(formatter)
        self.setLevel(level)
        self.msg_func = msg_func

    def emit(self, record: LogRecord) -> None:
        modified_record = copy.deepcopy(record)
        if self.msg_func:
            modified_record.msg = self.msg_func(modified_record.msg)
        super().emit(modified_record)
