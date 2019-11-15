from datetime import datetime

import flask


def datetime_to_rfc822_string(dt: datetime) -> str:
    return flask.json.loads(flask.json.dumps(dt))
