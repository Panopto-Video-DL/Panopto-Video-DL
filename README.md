# Panopto-Video-DL

![Downloads](https://img.shields.io/github/downloads/Panopto-Video-DL/Panopto-Video-DL/total?style=for-the-badge)  

Download video from Panopto!  

## Prerequisites  

- [Panopto-Video-DL-browser](https://github.com/Panopto-Video-DL/Panopto-Video-DL-browser)
- [FFmpeg](https://ffmpeg.org/download.html) (Recommended. See [below](#ffmpeg))  
    **Note**: FFmpeg **must** be added in the _system PATH_  
- Python 3.9

## Download

### Simple

Download the latest release: [Panopto-Video-DL](https://github.com/Panopto-Video-DL/Panopto-Video-DL/releases) _(No installation needed)_    

### Advanced

1. Clone this repository  
```shell
git clone https://github.com/Panopto-Video-DL/Panopto-Video-DL.git Panopto-Video-DL && cd Panopto-Video-DL
```
2. This project use [Mise](https://mise.jdx.dev) to ensure tool version management
```shell
mise i
python --version # verify python version 3.9
```
3. Create a virtual environment
```shell
python -m venv .venv
source .venv/bin/activate
```
4. Install requirements
```shell
python -m pip install -r requirements.txt
```
5. Open
```shell
python main.py
```

### FFmpeg

FFmpeg is optional, but it is **highly recommended**.  
It is possible that some videos will not download properly without FFmpeg.

## Usage

- Open _Panopto-Video-DL_  
- Paste the link automatically copied from [Panopto-Video-DL-browser](https://github.com/Panopto-Video-DL/Panopto-Video-DL-browser)  
- Set the destination folder  
- Wait for the download to finish  
