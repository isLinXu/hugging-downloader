import argparse

from huggingface_hub import snapshot_download


class HuggingFaceDownloader(object):
    def __init__(self, args):
        self.revision = args.revision
        self.repo_type = args.repo_type
        self.cache_dir = args.cache_dir
        self.local_dir = args.local_dir
        self.local_dir_use_symlinks = args.local_dir_use_symlinks
        self.library_name = args.library_name
        self.library_version = args.library_version
        self.user_agent = args.user_agent
        self.proxies = args.proxies
        self.etag_timeout = args.etag_timeout
        self.resume_download = args.resume_download
        self.force_download = args.force_download
        self.token = args.token
        self.local_files_only = args.local_files_only
        self.allow_patterns = args.allow_patterns
        self.ignore_patterns = args.ignore_patterns
        self.max_workers = args.max_workers
        self.tqdm_class = args.tqdm_class

    def download_repo_from_hf(self, repo_id: str):
        return snapshot_download(
            repo_id=repo_id,
            revision=self.revision,
            repo_type=self.repo_type,
            cache_dir=self.cache_dir,
            local_dir=self.local_dir,
            local_dir_use_symlinks=self.local_dir_use_symlinks,
            library_name=self.library_name,
            library_version=self.library_version,
            user_agent=self.user_agent,
            proxies=self.proxies,
            etag_timeout=self.etag_timeout,
            resume_download=self.resume_download,
            force_download=self.force_download,
            token=self.token,
            local_files_only=self.local_files_only,
            allow_patterns=self.allow_patterns,
            ignore_patterns=self.ignore_patterns,
            max_workers=self.max_workers,
            tqdm_class=self.tqdm_class
        )

'''
repo_id: str：要下载的代码库的ID。

revision: Optional[str] = None：要下载的快照文件的版本号，可选参数，默认为 None。

repo_type: Optional[str] = None：代码库类型，可选参数，默认值为 None，由函数自动判断。

cache_dir: Union[str, Path, None] = None：缓存下载的快照文件路径，可选参数，默认为 None。

local_dir: Union[str, Path, None] = None：下载的文件所保存的本地路径，可选参数，默认为 None。

local_dir_use_symlinks: Union[bool, Literal["auto"]] = "auto"：本地保存路径是否使用符号链接，可选参数，默认为 "auto"。

library_name: Optional[str] = None：用于下载时指定要使用的库的名称，可选参数，默认为 None。

library_version: Optional[str] = None：用于下载时指定要使用的库的版本号，可选参数，默认为 None。

user_agent: Optional[Union[Dict, str]] = None：用户标识，可选参数，默认为 None。

proxies: Optional[Dict] = None：用于HTTP请求的代理，可选参数，默认为 None。

etag_timeout: float = 10：用于HTTP缓存的ETag超时时间，可选参数，默认为 10。

resume_download: bool = False：是否从上次下载的进度处继续下载，可选参数，默认为 False。

force_download: bool = False：是否强制重新下载，可选参数，默认为 False。

token: Optional[Union[bool, str]] = None：用于鉴权的用户令牌，可选参数，默认为 None。

local_files_only: bool = False：是否只使用本地已有的文件，可选参数，默认为 False。

allow_patterns: Optional[Union[List[str], str]] = None：包含要允许的文件名模式的通配符列表或字符串，可选参数，默认为 None。

ignore_patterns: Optional[Union[List[str], str]] = None：包含要忽略的文件名模式的通配符列表或字符串，可选参数，默认为 None。

max_workers: int = 8：要使用的最大线程数，可选参数，默认为 8。

tqdm_class: Optional[base_tqdm] = None：用于实例化进度条的base_tqdm类，可选参数，默认为 None。

'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download a repo from the Hugging Face hub')
    parser.add_argument('--repo-id', type=str, default='prajjwal1/bert-tiny',
                        help='ID of the repo on the Hugging Face hub')
    parser.add_argument('--revision', type=str, default=None, help='Revision of the repo to download')
    parser.add_argument('--repo-type', type=str, default=None, help='Type of the repo to download')
    parser.add_argument('--cache-dir', type=str, default=None, help='Path to the download cache directory')
    parser.add_argument('--local-dir', type=str, default=None, help='Path to the output local directory')
    parser.add_argument('--local-dir-use-symlinks', type=str, default='auto',
                        help='If "auto", symbolic links are used iff the cache and local directories are in the same filesystem partition')
    parser.add_argument('--library-name', type=str, default=None, help='Name of the library to download')
    parser.add_argument('--library-version', type=str, default=None, help='Version of the library to download')
    parser.add_argument('--user-agent', type=str, default=None, help='Custom user agent for the download requests')
    parser.add_argument('--proxies', type=str, default=None, help='Proxy configuration for the download requests')
    parser.add_argument('--etag-timeout', type=int, default=10, help='Timeout for the download requests ETag checks')
    parser.add_argument('--resume-download', action='store_true', help='If set, resume an interrupted download')
    parser.add_argument('--force-download', action='store_true',
                        help='If set, force the download of an already downloaded file')
    parser.add_argument('--token', type=str, default=None,
                        help='Authentication token for private repository downloads')
    parser.add_argument('--local-files-only', action='store_true',
                        help='If set, only look for local files and never download over HTTP')
    parser.add_argument('--allow-patterns', type=str, default=None,
                        help='Comma-separated list of filename patterns to accept')
    parser.add_argument('--ignore-patterns', type=str, default=None,
                        help='Comma-separated list of filename patterns to ignore')
    parser.add_argument('--max-workers', type=int, default=8, help='Maximum number of workers for parallel downloads')
    parser.add_argument('--tqdm-class', type=str, default=None, help='Custom tqdm class to use for the progress bars')
    args = parser.parse_args()

    args.repo_id = 'prajjwal1/bert-tiny'
    args.cache_dir = '../cache'
    args.local_dir = '../downloads'
    downloader = HuggingFaceDownloader(args)
    downloader.download_repo_from_hf(args.repo_id)
