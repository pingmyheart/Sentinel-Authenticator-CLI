from tabulate import tabulate

from argparser import available_output_format_help, available_output_format, check_output_format, do_command_logic
from executor.totp import generate_executor_impl as executor_impl


def setup_parser(subparsers):
    parser = subparsers.add_parser('generate',
                                   help="Generate TOTP")
    parser.add_argument('--output',
                        help=f"Choose output format {available_output_format_help()}",
                        choices=available_output_format())
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help="Enable verbosity")

    parser.set_defaults(verbose=False)
    parser.set_defaults(output="stdout")
    parser.set_defaults(func=generate)


def parse_stdout(args, output):
    data = [["Label", "Issuer", "TOTP"]]
    for totp in output.response:
        data.append([totp['label'], totp['params']['issuer'], totp['totp']])
    return tabulate(data, headers='firstrow', tablefmt='grid')


def generate(args):
    check_output_format(args.output)
    parsed_args = {
    }
    do_command_logic(args=args,
                     parsed_args=parsed_args,
                     executor_impl=executor_impl,
                     parse_stdout=parse_stdout)
