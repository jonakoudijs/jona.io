import os
import json
import base64
import requests

def refreshtoken():
    """
    Generate a short-lived Spotify API access token. Internal use.

    Args:
        no arguments are required for this function.
    Returns:
        a Spotify API access token
    Raises:
        KeyError: if the response does not contain an acces token.
    """

    # set required variables
    url = 'https://accounts.spotify.com/api/token'
    client_id     = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    client_string = client_id + ':' + client_secret
    client_auth   = client_string.encode("utf-8")
    client_auth   = base64.standard_b64encode(client_auth)
    client_auth   = client_auth.decode('UTF-8')
    refresh_token = os.environ['SPOTIFY_REFRESH_TOKEN']

    # set auth headers and api payload
    headers = {
        'Authorization' : 'Basic ' + client_auth
    }
    payload  = {
        'grant_type' : 'refresh_token',
        'refresh_token' : refresh_token
    }

    # connect to spotify api and request an access token
    response = requests.post(url, headers=headers, data=payload)
    response = json.loads(response.text)
    access_token = response['access_token']

    # return the access token
    return access_token

def nowplaying(request):
    """
    Retrieve currently playing artist/title and status.

    Args:
        no arguments are required for this function.
    Returns:
        current artist, title and status.
    """

    # set required variables
    url = 'https://api.spotify.com/v1/me/player'
    access_token = refreshtoken()

    # set auth eaders
    headers = {
        'Authorization' : 'Bearer ' + access_token
    }

    # connect to spotify api
    response = requests.get(url, headers=headers)
    response_dict = json.loads(response.text)

    artist  = response_dict['item']['album']['artists'][0]['name']
    title   = response_dict['item']['name']
    playing = response_dict['is_playing']

    # construct nowplaying json object
    nowplaying = {
        'artist': artist,
        'title': title,
        'playing': playing
    }
    nowplaying = json.dumps(nowplaying)

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

    # return current/latest artist and title playing
    return (nowplaying, 200, response_headers)

def topartists(request):
    """
    Get the current user's top artists.

    Args:
        no arguments are required for this function.
    Returns:
        list of top artists and their details.
    """

    # set required variables
    playlist_id  = os.environ['SPOTIFY_PLAYLIST_ID']
    user_id      = os.environ['SPOTIFY_USER_ID']
    url          = 'https://api.spotify.com/v1/me/top/artists?time_range=long_term'
    access_token = refreshtoken()

    # set auth headers
    headers = {
        'Authorization' : 'Bearer ' + access_token
    }

    # connect to spotify api
    response = requests.get(url, headers=headers)

    # set dictionary variables
    response_dict = json.loads(response.text)
    artists = json.dumps(response_dict['items'])

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

    # return list of artists
    return (artists, 200, response_headers)
