from flask import request, jsonify

from hex.web.responses import ErrorResponse


def handle_500(error):
    status = 500
    title = "Internal Server Error"
    detail = "Something went wrong on our side."
    response = ErrorResponse(status, title, detail, request.path)
    return jsonify(response.to_dict()), status
