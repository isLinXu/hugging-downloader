
import os
import subprocess

# 定义Git LFS操作的存储库路径
# repo_path = "/path/to/repo"
repo_path = "https://huggingface.co/bert-base-uncased"

# git lfs install
git = subprocess.run(["git", "lfs", "install"], stdout=subprocess.PIPE)

# 使用subprocess运行Git LFS命令
result = subprocess.run(["git", "clone", repo_path], stdout=subprocess.PIPE)

# 输出结果
print(result.stdout.decode())
