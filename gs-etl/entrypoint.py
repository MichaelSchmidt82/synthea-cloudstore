import os
import glob
import time
from google.cloud import storage


def main():
    """
    Main entrypoint
    """

    storage_client = storage.Client()
    bucket = storage_client.bucket(os.environ.get('BUCKET_NAME'))

    while True:
        if os.path.exists('/messages/synthea'):
            break
        time.sleep(2)

    upload('/input', bucket)


def upload(path, bucket):
    """
    Recursively copy a folder of files & folders to GCS.

    path should be a valid folder without a trailing slash
    """
    assert os.path.isdir(path)
    for local_file in glob.glob(path + '/**'):
        if not os.path.isfile(local_file):
            upload(local_file, bucket)
            continue
        remote_path = os.path.join(os.environ.get('GCS_PATH'),
                                   local_file[1 + len('/input'):])
        blob = bucket.blob(remote_path)
        blob.upload_from_filename(local_file)
        print(f'uploaded {local_file[len("/input"):]}', flush=True)


if __name__ == '__main__':
    main()
