import logging

from halo import Halo


def available_output_format():
    return ["stdout",
            "json",
            "xml"]


def available_output_format_help():
    return f"({', '.join(available_output_format())})"


def check_output_format(output_format):
    if output_format not in available_output_format():
        raise RuntimeError("Unrecognised output format")


def execute_without_logs(func, *args, **kwargs):
    current_level = logging.getLogger().getEffectiveLevel()
    logging.getLogger().setLevel(logging.CRITICAL + 1)
    result = func(*args, **kwargs)
    logging.getLogger().setLevel(current_level)
    return result


def filter_non_null_args(parsed_args):
    return {key: value for key, value in parsed_args.items() if value is not None}


def do_command_logic(args,
                     parsed_args,
                     executor_impl,
                     parse_stdout):
    parsed_args = filter_non_null_args(parsed_args=parsed_args)
    spinner = None
    if not args.verbose:
        spinner = Halo(text='Executing requested action')
        spinner.start()

    output = execute_without_logs(executor_impl.execute,
                                  **parsed_args) if not args.verbose else executor_impl.execute(**parsed_args)

    if not args.verbose:
        spinner.stop()
    if args.output == "stdout":
        print(parse_stdout(args=args,
                           output=output))
    elif args.output == "json":
        print(output.model_dump_json(indent=2))
