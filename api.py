from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, abort
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, parser

# create a Flask app
app = Flask(__name__)

# Don't sort the JSON Response so we can get it
# EXACTLY as the instructions specify.  If we sort it,
# Response will look like this:
# {"numbers":[1,2,3],"status":"ok"}
# We want status first and numbers array second.
app.config['JSON_SORT_KEYS'] = False

# Don't pretty print the response, we want it condensed
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# connect flask_restful to flask
api = Api(app)


# Define a standard error response that meets the exercise style
def error_response():
    abort(make_response(jsonify({'status': 'error', 'numbers': []}), 400))


'''Validation errors from 'args' are handled with a 400 response
Properly formed request will include word (str) & max_value (int).

If 'word' is not a string and is not one of fizz, buzz, or fizzbuzz
then we return an error.

If 'max_value is not an integer or is less than 1, then we
return an error.

Error format is defined in the instructions as:
{"status":"error","numbers":[]}

A successful response will return "status":"ok" and the numbers
in an ascending array

Example:

Request:
curl -X GET 'http://localhost:4002/api?word=fizz&max_value=30'

Response:
{"status":"ok","numbers":[3,6,9,12,15,18,21,24,27,30]}
'''


class FizzBuzz(Resource):
    # Create validation schema for params 'word' and 'max_value'
    args = {
        'word':
        fields.Str(
            required=True,
            validate=validate.OneOf(['fizz', 'buzz', 'fizzbuzz'])),
        'max_value':
        fields.Int(required=True, validate=validate.Range(min=1)),
    }
    # Assign divisor/s to each word per instructions
    word_values = {'fizz': [3], 'buzz': [5], 'fizzbuzz': [3, 5]}
    # access the params when we receive them in http GET
    @use_kwargs(args)
    def get(self, word, max_value):
        # Uncomment the code below to reject all requests that have
        # extra paramaters i.e. params if params other than 'word' or
        # 'max_value' are included, we return an error response

        # for param in request.args:
        #     print(param)
        #     if param not in self.args.keys():
        #         error_response()

        # initalize an empty array of numbers
        numbers = []
        # loop from 1 to max_value
        for i in range(1, max_value + 1):
            # run the modulus calculation for the divisors given
            # our 'word' api value
            # if our max value is wholly divisible by our iterator
            # then we append it to the numbers array
            if any(i % n == 0 for n in self.word_values.get(word)):
                numbers.append(i)
        # return the response
        return jsonify({'status': 'ok', 'numbers': numbers})

    # if 'word' or 'max_value' doesnt validate per the schema,
    # we use this decorator to return an error defined under
    # error_response()
    @parser.error_handler
    def handle_request_parsing_error(err):
        # We could also return a more descriptive response
        # abort(422, errors=err.messages)
        error_response()


# Run the app from the CLI, python newapi.py
if __name__ == '__main__':
    api.add_resource(FizzBuzz, '/api', endpoint='api')
    app.run(debug=True, port=4002, threaded=True, host='0.0.0.0')
