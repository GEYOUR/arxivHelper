

import os
import re
import shutil

def arxivHelper(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".pdf"):
                old_path = os.path.join(root, file)
                new_filename = os.path.join(os.path.basename(root) + "_" + file)
                new_path = os.path.join(directory_path, new_filename)
                shutil.move(old_path, new_path)


def edit_tex_file(tex_file_path):
    with open(tex_file_path, 'r') as f:
        tex_contents = f.read()
    tex_lines = tex_contents.split('\n')
    for i in range(len(tex_lines)):
        match = re.search(r'\\includegraphics.*?{(.*?)}', tex_lines[i])
        if match:
            old_path = match.group(1)
            path_parts = old_path.split('/')
            new_path = '_'.join(path_parts[-2:])
            tex_lines[i] = tex_lines[i].replace(old_path, new_path)
    with open(tex_file_path, 'w') as f:
        f.write('\n'.join(tex_lines))
    print("successfully modified the tex file.")


if __name__ == '__main__':
    path = r"./testDir"
    # arxivHelper(path)
    edit_tex_file(os.path.join(path, "main.tex"))