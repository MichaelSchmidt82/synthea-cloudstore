import os
import sys
import glob
import time
from google.cloud import storage, exceptions


def main():
    """
    Main entrypoint
    """
    #* Wait for synthea
    while True:
        if os.path.exists('/messages/synthea'):
            break
        time.sleep(2)

    storage_client = storage.Client()
    bucket = storage_client.bucket(os.environ.get('BUCKET_NAME'))

    try:
        assert storage_client.lookup_bucket(bucket)
    except AssertionError as exc:
        print(f'Bucket {os.environ.get("BUCKET_NAME")} does not exist',
              file=sys.stderr,
              flush=True)
        print(exc)
        return 1
    except exceptions.GoogleCloudError as exc:
        print(exc)
        return 1

    upload('/input', bucket)
    os.remove('/messages/synthea')
    return 0


def upload(path, bucket):
    """
    Recursively copy a folder of files & folders to GCS.
    path should be a valid folder without a trailing slash
    """
    assert os.path.isdir(path)
    for local_file in glob.glob(path + '/**'):

        #* local_file is a folder. Recurse into that folder
        if not os.path.isfile(local_file):
            upload(local_file, bucket)
            os.rmdir(local_file)
            continue

        #* local_file is a file.  Create a path and attempt to upload the file
        remote_path = os.path.join(os.environ.get('GCS_PATH'),
                                   local_file[1 + len('/input'):])

        try:
            blob = bucket.blob(remote_path)
            blob.upload_from_filename(local_file)
        except exceptions.GoogleCloudError:
            print(f'failed to upload {local_file[len("/input"):]}',
                  file=sys.stderr,
                  flush=True)
            continue

        print(f'uploaded {remote_path}', flush=True)
        os.remove(local_file)


if __name__ == '__main__':
    sys.exit(main())
