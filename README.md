# hugging-downloader

---

![GitHub stars](https://img.shields.io/github/stars/isLinXu/hugging-downloader)![GitHub forks](https://img.shields.io/github/forks/isLinXu/hugging-downloader) ![GitHub watchers](https://img.shields.io/github/watchers/isLinXu/hugging-downloader) [![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fatrox%2Fsync-dotenv%2Fbadge&style=flat)](https://github.com/isLinXu/hugging-downloader)  ![img](https://badgen.net/badge/icon/learning?icon=deepscan&label)![GitHub repo size](https://img.shields.io/github/repo-size/isLinXu/hugging-downloader.svg?style=flat-square)  ![GitHub last commit](https://img.shields.io/github/last-commit/isLinXu/hugging-downloader) ![GitHub](https://img.shields.io/github/license/isLinXu/hugging-downloader.svg?style=flat-square)![img](https://hits.dwyl.com/isLinXu/hugging-downloader.svg)

# Installation

```shell
pip install -r requirements.txt
```
or
```shell
pip install git+https://github.com/huggingface/transformers
```

# Usage:

## spider and request model from huggingface

```shell
python hf_downloader/spider_hf_downloader.py 
```
<div style="text-align:center;">   <img src="https://user-images.githubusercontent.com/59380685/247611154-380ac3eb-07e7-4e5e-be5c-b5b9a11b320f.png" alt="image" style="max-width:60%;max-height:100%;" /> </div>

<div style="text-align:center;">   <img src="https://user-images.githubusercontent.com/59380685/247611366-013142ef-f4e0-4375-8eed-baedb99b6d9f.png" alt="image" style="max-width:60%;max-height:100%;" /> </div>

<div style="text-align:center;">   <img src="https://user-images.githubusercontent.com/59380685/247611887-12a9df58-0db6-4c4d-8ef4-99a95d26948a.png" alt="image" style="max-width:60%;max-height:100%;" /> </div>

## Download models from huggingface

```shell
python hf_downloader/huggingface_download.py --repo-id prajjwal1/bert-tiny --cache-dir ../cache --local-dir ../bert-tiny
```

<div style="text-align:center;">   <img src="https://user-images.githubusercontent.com/59380685/247585900-15fc44d4-8835-412b-9f11-2cc10b650a69.png" alt="image" style="max-width:60%;max-height:100%;" /> </div>

<div style="text-align:center;">   <img src="https://user-images.githubusercontent.com/59380685/247585984-6b984dc3-8b98-4018-9a2a-175b348d5fc7.png" alt="image" style="max-width:30%;max-height:30%;" /> </div>

## Download models use git ifs

```shell
python hf_downloader/git_lfs_clone.py --repo_url https://huggingface.co/prajjwal1/bert-tiny --repo_path bert-tiny
```

<div style="text-align:center;">   <img src="https://user-images.githubusercontent.com/59380685/247892381-ed5651ff-8073-4e6b-b51f-fefaf6e1129c.png" alt="image" style="max-width:60%;max-height:100%;" /> </div>

