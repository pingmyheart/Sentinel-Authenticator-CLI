from abc import abstractmethod, ABC

from configuration.environment import Environment
from dto.common.executor import ExecutorResponse


class Executor(ABC):
    def __init__(self, env: Environment):
        self.env = env

    @abstractmethod
    def execute(self, **kwargs) -> ExecutorResponse:
        pass

    @abstractmethod
    def usage(self):
        pass

    @abstractmethod
    def _load_check_args(self, kwargs):
        pass

    @abstractmethod
    def pre_check_executor(self, **kwargs):
        pass

    @staticmethod
    def kwargs_get_or_default(kwargs, get, default):
        return kwargs[get] if get in kwargs else default
