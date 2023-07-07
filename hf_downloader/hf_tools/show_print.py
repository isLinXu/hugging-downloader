import json
from colorama import init, Fore, Style

def show_print_info(json_path):
    # 读取JSON文件
    with open(json_path, 'r') as file:
        json_data = json.load(file)

    # 将JSON数据转换为字符串列表
    string_list = json_data

    # 确定行数
    n = len(string_list) // 10 + (len(string_list) % 10 != 0)  # 计算行数，确保每行至少有10个元素

    # 打印字符串列表
    for i in range(n):
        line = ""
        for j in range(10):
            if i * 10 + j < len(string_list):
                line += string_list[i * 10 + j] + " || "
            else:
                line += " "
        print(Style.BRIGHT + Fore.GREEN + line.rstrip() + Style.RESET_ALL)
        print('\n' + "=" * (350))


if __name__ == '__main__':
    json_path = "/download/datasets_all.json"
    show_print_info(json_path)