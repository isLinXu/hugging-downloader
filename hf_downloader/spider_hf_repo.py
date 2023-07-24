
import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm
import time
import hf_downloader.profiles
import os

def get_hf_repo_dict(url_template="https://huggingface.co/models?p={}&sort=downloads", pages=100):

    all_links = []
    #! total pages = 7923
    for i in tqdm(range(0, pages)):
        # 访问网页
        if i == 0:
            url = "https://huggingface.co/models?sort=downloads"
        else:
            url = url_template.format(i)
        print("current_page: ", url)
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            links = []
            tags = []
            # 获取此页面的所有链接
            for a in soup.find_all("a", href=True):
                text_href = a["href"]
                # links.append("https://huggingface.co" + text_href)
                if "?" not in text_href and "#" not in text_href and "type" not in text_href and \
                        "login" not in text_href and "join" not in text_href and \
                        "docs" not in text_href and "privacy" not in text_href and \
                        "spaces" not in text_href and "pricing" not in text_href and "huggingface" not in text_href and \
                        "apply" not in text_href and "datasets" not in text_href and len(text_href) > 7:
                    links.append("https://huggingface.co" + text_href)

            all_links.extend(links)
        except requests.exceptions.RequestException as e:
            print("Error: ", e)
            print("Retrying in 3 seconds...")
            time.sleep(3)
            continue

    all_links = list(set(all_links))
    # print(all_links)
    print("len(all_links): ", len(all_links))

    model_dict = {}
    for i in tqdm(range(len(all_links))):
        link = all_links[i]
        # print("link: ", link)
        model_name = link.split("/")[-1]
        # print("model_name: ", model_name)
        model_dict[model_name] = link

    modeling_dict = {}
    for (key, value) in model_dict.items():
        print('"'+key+'"' + ':' + '"'+value+'"', end=",\n")
        modeling_dict[key] = value
    with open("../download/models_all.json", "w") as json_file:
        json.dump(modeling_dict, json_file)
    return model_dict


if __name__ == '__main__':
    get_hf_repo_dict(url_template="https://huggingface.co/models?p={}&sort=downloads",
                     pages=7923)
