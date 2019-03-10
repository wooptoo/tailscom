import json
from pathlib import Path
from operator import attrgetter, itemgetter

from flask import Flask, abort, jsonify
from webargs import fields
from webargs.flaskparser import use_args

from model import db, Postcodes
from schema import PostcodeSchema

app = Flask(__name__)

index_args = {'postcode': fields.Str(), 'radius': fields.Str()}


@app.route('/')
@use_args(index_args)
def index(args):
    query_result = Postcodes.select()
    postcode_schema = PostcodeSchema(many=True)
    result = postcode_schema.dump(query_result).data
    return jsonify(result)


if __name__ == '__main__':
    db.connect()
    app.run(debug=True, port=8080)
