import credentials
import wolframalpha


def api_response(input):

    app_id = credentials.my_wolfram
    client = wolframalpha.Client(app_id)

    res = client.query(input)

    # Includes only text from the response
    answer = next(res.results).text
    return answer
