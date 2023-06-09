import os
from flask import Flask, jsonify
from flask_smorest import Api
# from collections.abc import Mapping
from flask_jwt_extended import JWTManager
from db import db
from blocklist import BLOCKLIST
from resources.admin import blp as AdminBlueprint
# from resources.grades import blp as GPABlueprint
from resources.students import blp as StudentsBlueprint
# from resources.course_registration import blp as CourseRegistrationBlueprint
from resources.user import blp as UserBlueprint
from datetime import timedelta

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Students Management REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "postgres://kzgvxqiniokvbr:4acf5e02e5205a99314fae2fe3032b067e9207722197394459d3b7ccf04c0d07@ec2-3-93-160-246.compute-1.amazonaws.com:5432/d7k0gbmepi1m8h")
    # app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "justgifted94"
    jwt = JWTManager(app)
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload['jti'] in BLOCKLIST
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({
                "description": "This token has expired",
                "error": "token_expired"
            }), 401
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify({
                "description": "Signature verification failed",
                "error": "invalid_token"
            }), 401
        )
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify({
                "desciption": "Request does not contain an access token",
                "error": "authorization_required"
            }), 401
        )

    @app.before_first_request
    def create_tables():
        db.create_all()

    api.register_blueprint(AdminBlueprint)
    api.register_blueprint(StudentsBlueprint)
    # api.register_blueprint(GPABlueprint)
    # api.register_blueprint(RetrievalBlueprint) 
    api.register_blueprint(UserBlueprint)
    
    
# if __name__=="__main__":
    # app.run(debug=True)

    return app
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)