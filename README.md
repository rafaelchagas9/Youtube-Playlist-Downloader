# Youtube Playlist Downloader

> Python script that automatically downloads all items of a playlist or various playlist

![ezgif-4-0839ca71a6ac](https://user-images.githubusercontent.com/33136664/86649706-5f2e9f00-bfb8-11ea-9e29-32fd137c2782.gif)

## Table of Contents

- [Installation](#Installation)
- [Using it](#Using)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/BlackGamesHD/Youtube-Playlist-Downloader.git`

### Setup

> Install [Python](https://www.python.org/downloads/)

> update and install this package first via CMD

```shell
$ pip install pytube3
```

> then run this command and copy the location

```shell
$ pip show pytube3
```
![CMD](https://user-images.githubusercontent.com/33136664/86653895-ecbfbe00-bfbb-11ea-9876-eb23fc1ee840.png)

> Go to that location, open the folder pytube and the file extract.py

![Folder](https://user-images.githubusercontent.com/33136664/86655592-365cd880-bfbd-11ea-9d0f-e8cb024177dc.png)

> Search this line (It will probally be on line 301)

```shell
parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
```

> Change it to

```shell
parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
```
