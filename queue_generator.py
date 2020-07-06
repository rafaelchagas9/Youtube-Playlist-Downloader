import json
import constants
import downloader


def get_dict_keys_list(dictionary):
    return dictionary.keys()


playlists = get_dict_keys_list(constants.PLAYLISTS)
store_list = []

# Path Constant
general_path = constants.OUTPUT_DIR


def main():
    for playlist in playlists:
        check_history(playlist)


def check_history(playlist_name):
    store_list.clear()
    # Carregando informações do json
    f = open(general_path + 'playlist_items/'+playlist_name+'.json', 'r')
    data = json.load(f)

    for i in data:
        store_list.append(i['contentDetails']['videoId'])

    f.close()

    # Adicionando na fila caso o item não tenha sido baixado anteriormente
    f = open(general_path + 'history/history.txt', 'r')
    x = f.readlines()
    f.close()
    file = open(general_path + 'queue/' + playlist_name + '_queue.txt', 'a')

    for item in store_list:
        if x.__contains__(item + '\n') or x.__contains__(item):
            print('Video Already Downloaded')
        else:
            file.writelines(f"{item}\n")

    file.close()
    downloader.start_process(playlist_name)
