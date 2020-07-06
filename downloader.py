from pytube import YouTube, exceptions
import constants

history = []
video_output_path = constants.VIDEOS_DIR
general_path = constants.OUTPUT_DIR


def start_process(playlist_name):
    history.clear()
    print('Starting playlist:' + playlist_name)
    queue = open_download_queue(playlist_name)
    for video_id in queue:
        start_download(video_id.replace('\n', ''), playlist_name)
    save_video_history()
    clear_download_queue(playlist_name)


def open_download_queue(playlist_name):
    with open(general_path + 'queue/' + playlist_name + '_queue.txt', 'r') as f:
        x = f.readlines()
    return x


def start_download(video_id, playlist_name):
    try:
        video = YouTube('https://www.youtube.com/watch?v=' + video_id)
        print(f"Downloading: {video.title}")
        video.streams.get_highest_resolution().download(output_path=video_output_path + playlist_name,
                                                        filename=f"{video.title} - {video_id}")
        history.append(video_id)
    except exceptions.VideoUnavailable:
        print('Video unavailable: ' + video_id)
    except exceptions.RegexMatchError:
        print("HTML Parse error while trying to download video  " + video_id)
    except exceptions.HTMLParseError:
        print("HTML Parse error while trying to download video " + video_id)
    except:
        print("Unknown error while trying to download video: " + video_id)


def save_video_history():
    with open(general_path + 'history/history.txt', 'a') as file:
        for link in history:
            file.writelines(link + '\n')


def clear_download_queue(playlist_name):
    file = open(general_path + 'queue/' + playlist_name + '_queue.txt', 'w')
    file.truncate(0)
    file.close()
