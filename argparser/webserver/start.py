from flasgger import Swagger
from flask import Flask

from controller import blueprints


def setup_parser(subparsers):
    parser = subparsers.add_parser('start',
                                   help="Analyze the kubernetes cluster")
    parser.add_argument('--server-port',
                        nargs='?',
                        type=int,
                        help="Server port number")

    parser.set_defaults(port=5000)
    parser.set_defaults(func=start)


def start(args):
    app = Flask(__name__)
    Swagger(app, template={
        "info": {
            "title": "Sentinel Authenticator",
            "description": "Sentinel Authenticator Command Line Interface Web Adapter",
            "version": "Unknown"
        }
    })

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    app.run(host="0.0.0.0",
            port=args.server_port,
            debug=False)
