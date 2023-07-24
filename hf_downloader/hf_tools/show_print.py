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

def show_print_dict(json_path):
    # 读取JSON文件
    with open(json_path, 'r') as file:
        json_data = json.load(file)

    # 将JSON数据转换为字符串字典
    string_dict = json_data

    # 确定行数和列数
    n = len(string_dict) // 10 + (len(string_dict) % 10 != 0)  # 计算行数，确保每行至少有10个元素
    m = 10  # 列数为10

    # 打印字符串字典
    for i in range(n):
        for j in range(m):
            if i * m + j < len(string_dict):
                print(string_dict[i * m + j].ljust(10) + ["||", "="][j % 2], end="")
            else:
                print(["||", "="][j % 2])  # 如果字典长度不足10，用“||”填充；如果列长度不足10，用“=


if __name__ == '__main__':
    json_path = "download/datasets_all.json"
    # json_path = "download/models_all.json"
    # show_print_info(json_path)
    show_print_dict(json_path)