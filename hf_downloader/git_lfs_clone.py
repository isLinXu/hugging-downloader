import argparse
import os
import subprocess

def get_hf_repo(repo_url, repo_path):
    '''
    使用Git LFS下载HuggingFace模型
    @param repo_url: 模型的Git LFS存储库URL
    '''
    # 定义Git LFS操作的存储库路径
    repo_name = repo_url.split("/")[-1]
    repo_path = "../" + repo_name
    # git lfs install
    git = subprocess.run(["git", "lfs", "install"], stdout=subprocess.PIPE)

    # 使用subprocess运行Git LFS命令
    result = subprocess.run(["git", "clone", repo_url, repo_path], stdout=subprocess.PIPE)

    # 输出结果
    print(git.stdout.decode())
    print(result.stdout.decode())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo_url', type=str, help='huggingface repo url')
    parser.add_argument('--repo_path', type=str, help='local path to store repo')
    args = parser.parse_args()
    '''
    usage:
        sudo apt-get install git-lfs
    example:
        python git_lfs_clone.py --repo_url https://huggingface.co/prajjwal1/bert-tiny --repo_path ../bert-tiny
        repo_url = "https://huggingface.co/bert-base-uncased"
        repo_url = "https://huggingface.co/prajjwal1/bert-tiny"
    '''
    args.repo_url = "https://huggingface.co/prajjwal1/bert-tiny"
    args.repo_url = "../bert-tiny"
    get_hf_repo(args.repo_url, args.repo_path)
