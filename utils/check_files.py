import os

def get_code_list():
    code_list = [file for file in os.listdir("./Code")]
    return code_list
  
def make_info(code_list):
    info = {}
    for code in code_list:
        tup = os.path.splitext(code)
        prob = tup[0].split('_')
        info[prob[0]].append(prob[1])
        
    return info

def update_readme(readme):
    code_list = get_code_list()
    info = make_info(code_list)
    while True:
        line = readme.readline()
        if not line : break
        for problem_number in info.keys:
            if problem_number in line:
                for author in info[problem_number]:
                    line = line.rstrip() + author
                    print(line)
                break
    return readme


if __name__ == "__main__":
    readme = open("./README.md", 'a', encoding='utf-8')
    update_readme(readme)
    readme.close()
