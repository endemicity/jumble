from flask import abort, Flask

from ..logic.exceptions import WordlistLookupError, LettersValueError
from ..logic.solution import solve_pangram


app = Flask(__name__)


@app.route("/api/pangram/<wordlist>/<letters>/", methods=["GET"])
def wordlist_letters_solution(wordlist, letters):

    try:
        solution = solve_pangram(letters, wordlist)
    except WordlistLookupError as e:
        app.logger.info("WordlistLookupError: {}".format(e))
        abort(404)
    except LettersValueError as e:
        app.logger.info("LettersValueError: {}".format(e))
        abort(404)
    except Exception as e:
        app.logger.error("Exception: {}".format(e))
        abort(500)

    return {
        "pangrams": solution,
    }
