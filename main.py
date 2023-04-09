import sys
import os
from google.cloud import storage

def upload_to_bucket(bucket_name, source_file_name, destination_blob_name):
    """Upload a file to the specified Google Cloud Storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def implicit():
    """
    Google Cloud Storageからバケットのリストを取得し、表示します。
    クライアントを構築する際に認証情報を指定しない場合、
    クライアントライブラリは環境中の認証情報を探します。
    """
    from google.cloud import storage

    # 認証情報を指定せずにクライアントを構築すると、
    # クライアントライブラリは環境中の認証情報を探します。
    storage_client = storage.Client()

    # 認証付きAPIリクエストを行う
    buckets = list(storage_client.list_buckets())
    print(buckets)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_file_path> <destination_blob_path>")
        sys.exit(1)

    # コマンドライン引数からバケット名、アップロードするファイルのパス、およびGoogle Cloud Storage内のフォルダとファイル名を取得
    # bucket_name = sys.argv[1]
    # bucket_name = 'loochs-wordpress-blogpost'
    bucket_name = os.environ['BUCKET_NAME']
    source_file_name = sys.argv[1]
    destination_blob_name = sys.argv[2]

    # ファイルをアップロード
    upload_to_bucket(bucket_name, source_file_name, destination_blob_name)