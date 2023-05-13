from huggingface_hub import snapshot_download


def download_snapshot(repo_id: str):
    snapshot_download(repo_id=repo_id)


if __name__ == '__main__':
    download_snapshot(repo_id="lysandre/arxiv-nlp")
