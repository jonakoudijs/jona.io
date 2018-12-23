import os
import json
import requests

def gigography(request):
    """
    Retrieve list of past concerts from Songkick.

    Args:
        no arguments are required for this function.
    Returns:
        a list of past concerts from Songkick.
    """

    # set required variables
    username = os.environ['SONGKICK_USERNAME']
    apikey   = os.environ['SONGKICK_APIKEY']

    # construct url
    url = 'https://api.songkick.com/api/3.0/users/' + username + '/gigography.json?apikey=' + apikey

    # connect to songkick api
    response = requests.get(url)
    response_dict = json.loads(response.text)

    # select all events from api output
    events = response_dict['resultsPage']['results']['event']

    # select page information
    response_perpage      = response_dict['resultsPage']['perPage']
    response_page         = response_dict['resultsPage']['page']
    response_totalentries = response_dict['resultsPage']['totalEntries']

    # build new dictionary of events
    concerts = []
    for event in reversed(events):
        if event['type'] == 'Concert':
            case = {
                'artist_id'   : event['performance'][0]['artist']['id'],
                'artist_name' : event['performance'][0]['artist']['displayName'],
                'date'        : event['start']['date'],
                'venue'       : event['venue']['displayName'],
                'uri'         : event['uri']
            }
            concerts.append(case)

    # set dictionary variables
    concerts = json.dumps(concerts)

    # set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        response_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, response_headers)

    # Set CORS headers for the main request
    response_headers = {
        'Access-Control-Allow-Origin': '*'
    }

    # return list of past concerts
    return (concerts, 200, response_headers)
