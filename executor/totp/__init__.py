from configuration import environment_impl
from executor.totp.generate_executor import GenerateExecutor

generate_executor_impl = GenerateExecutor(env=environment_impl)
