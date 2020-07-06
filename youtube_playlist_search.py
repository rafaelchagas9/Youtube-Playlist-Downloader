import requests
import queue_generator
import json
import constants

# List that contains all items from a specific playlist
playlist_items = []

# Path Constant
general_path = constants.OUTPUT_DIR

# Obtaining constants
client_secret = constants.CLIENT_SECRET
client_id = constants.CLIENT_ID
code_refresh_token = constants.REFRESH_TOKEN
playlists_id = constants.PLAYLISTS


def main():
    access_token = refresh_token()
    for playlist_id in playlists_id:
        # Clear list containing all items from another playlist
        playlist_items.clear()
        # Calling youtube request with page token = 0 so the program knows we want the first page
        make_youtube_request(playlists_id[playlist_id], playlist_id, 0, access_token)
    # Calling another python script that will generate your download queue
    queue_generator.main()


def refresh_token():
    url = 'https://accounts.google.com/o/oauth2/token'
    body = {'client_id': client_id,
            'client_secret': client_secret,
            'refresh_token': code_refresh_token,
            'grant_type': 'refresh_token'}
    response = requests.post(url, data=body)
    response_json = json.loads(response.text)
    if response_json['access_token']:
        return response_json['access_token']
    else:
        print('Failed to get token, please review if you authorized this app on your Google Account')
        quit(1)


def make_youtube_request(playlist_id, playlist_name, page_token, access_token):
    response = ''
    if page_token == 0:
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&' \
              f'playlistId={playlist_id}'
        headers = {'Authorization': f'Bearer {access_token}',
                   'Accept': 'application/json'}
        r = requests.get(url, headers=headers)
        response = json.loads(r.text)
    else:
        url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&' \
              f'playlistId={playlist_id}&pageToken={page_token}'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json'}
        r = requests.get(url, headers=headers)
        response = json.loads(r.text)

    # Checking if there is another page
    if 'nextPageToken' in response:
        playlist_items.extend(response['items'])
        make_youtube_request(playlist_id, playlist_name, response['nextPageToken'], access_token)
    else:
        playlist_items.extend(response['items'])
        generate_json(playlist_items, playlist_name)


def generate_json(response, playlist_name):
    # Generating JSON
    js = (json.dumps(response))
    fp = open(general_path + 'playlist_items/'+playlist_name+'.json', 'w')
    fp.write(js)
    fp.close()


if __name__ == "__main__":
    main()
