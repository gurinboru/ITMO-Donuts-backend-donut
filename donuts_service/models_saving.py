import requests


def download_file_from_google_drive(link, destination):
    URL = "https://docs.google.com/uc?export=download"
    id = get_id_from_link(link)
    session = requests.Session()

    response = session.get(URL, params={'id': id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    save_response_content(response, destination)
    with open(destination, 'rb') as f:
        return f.read()


# https://drive.google.com/file/d/1_mF_dUGMGxcob0k7eJb6d4d_JED6uSRp/view?usp=share_link

def get_id_from_link(link):
    return link.split('/')[-2]


def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value


def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


if __name__ == "__main__":
    file_id = '1iXw0vmAlGNzHj_YUfKoyr51PslfqZQUt'
    destination = 'model.obj'
    download_file_from_google_drive(file_id, destination)
