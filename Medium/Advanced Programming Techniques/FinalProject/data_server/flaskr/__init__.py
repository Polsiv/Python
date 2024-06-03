from flask import Flask, Response, jsonify
import os
import util.security as sc

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

    # a simple page that says hello    
    @app.route('/publickey', methods = ['GET'])
    def public_key():
        try:
            pk = sc.get_pk()
            return Response(pk, mimetype='text/plain')
        except Exception as e:
            app.logger.error(f"Error reading public key: {e}")
            return jsonify({"error": "Internal server error"}), 500

    return app