import requests
from app.__version__ import __version__

REPO = {
    'owner': 'Panopto-Video-DL',
    'target': 'Panopto-Video-DL'
}


def get_release_update() -> dict or None:
    response = requests.get(f'https://api.github.com/repos/{REPO["owner"]}/{REPO["target"]}/releases/latest')
    if 200 <= response.status_code <= 299:
        data = response.json()
        tag = data.get('tag_name')
        if tag is not None and tag != __version__:
            return {
                'tag': tag,
                'url': data.get('html_url', ''),
                'body': data.get('body', '').strip()
            }
    return None
