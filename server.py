from flask import render_template, redirect

from app import create_app
from app.config import TASK_TIMEOUT
from app.libs.error import APIException
from app.libs.error_code import ServerError
from werkzeug.exceptions import HTTPException
from app.libs.logging_helper import logger

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 调试模式
        # log
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    # return redirect('./static/index.html')


if __name__ == "__main__":
    # app.template_folder = "./static"
    # app.static_folder = "./static"
    app.run(host='0.0.0.0', port=5002)

