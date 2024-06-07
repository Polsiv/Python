#pylint: disable = E0401, W0718, W1203,  C0114
import os
import random
import json
import signal
from flask import Flask, Response, jsonify, request
from util.normal_distribution import NormalDistribution
from util.uniform_distribution import UniformDistribution

from util.security import Cryptographer

CRYPT = Cryptographer()
CRYPT.generate_keys()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='118115c9d8814e719aee7dba24433e0a',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/publickey', methods=['GET'])
    def public_key():
        try:
            pk = CRYPT.public_key.export_key().decode()
            return Response(pk, mimetype='text/plain')
        except Exception as e:
            app.logger.error(f"Error reading public key: {e}")
            return jsonify({"error": "Internal server error"}), 500

    @app.route('/numbers', methods=['POST'])
    def numbers():
        try:
            data = request.json
            json_data = CRYPT.decrypt(data['data'])
            low, sup, total = json_data["LowLimit"], json_data["SupLimit"], json_data["Total"]
            normal = NormalDistribution()
            uniform = UniformDistribution()
            to_choice = [normal.gen_numbers(low, sup, total), uniform.gen_numbers(low, sup, total)]
            numbers = random.choice(to_choice)
            to_send = {"numbers": numbers}
            to_send_json = json.dumps(to_send)
            encrypted_json = CRYPT.encrypt(to_send_json, data['problem_solver_pk'])
            sent_data = {'data': encrypted_json}

            return jsonify(sent_data), 200
        except Exception as e:
            app.logger.error(f"Error processing numbers: {e}")
            return jsonify({"error": "Internal server error"}), 500

    @app.route('/shutdown', methods=['GET'])
    def shutdown():
        pid = os.getpid()
        os.kill(pid, signal.SIGINT)
        return "flask shut down"

    return app
