import os

def generate_markdown(path, level=0, exclude_list=None, parent_index=""):
    if exclude_list is None:
        exclude_list = []

    markdown = ""

    try:
        items = sorted(os.listdir(path))  # 获取当前文件夹中的所有内容
    except PermissionError:
        print(f"无法访问文件夹：{path}")
        return ""

    # 分离文件夹和文件
    folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if not os.path.isdir(os.path.join(path, item))]

    # 合并排序结果，文件夹在前，文件在后
    sorted_items = folders + files

    index = 1  # 初始化编号
    for item in sorted_items:
        item_path = os.path.join(path, item)

        # 检查路径是否包含排除词
        if any(exclude in item_path for exclude in exclude_list):
            continue  # 如果包含排除词，则跳过

        if os.path.isdir(item_path):  # 如果是文件夹
            markdown += f"<details>\n"
            markdown += f'  <summary>{item}/</summary>\n\n'
            markdown += f"<ul>\n"  # 开始无序列表
            markdown += generate_markdown(item_path, level + 1, exclude_list, parent_index)  # 递归处理子文件夹
            markdown += f"</ul>\n"  # 结束无序列表
            markdown += f"</details>\n\n"
        else:  # 如果是文件
            markdown += f"<li><code>{item}</code></li>\n"  # 使用 <li> 包裹文件，并用 <code> 包裹文件名

        index += 1  # 更新编号

    return markdown


if __name__ == "__main__":
    # 获取脚本所在路径
    script_path = os.path.dirname(os.path.abspath(__file__))
    print("正在生成Markdown内容...")

    # 定义排除词列表
    exclude_list = [".git", "py", "txt", "bat", "md"]

    # 生成Markdown内容
    markdown_content = generate_markdown(script_path, exclude_list=exclude_list)

    # 输出到文件
    output_file = os.path.join(script_path, "README.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"Markdown内容已生成并保存到：{output_file}")