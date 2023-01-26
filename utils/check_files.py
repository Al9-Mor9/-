import os

def get_code_list():
    code_dirs = [file for file in os.listdir("./Code/") if os.path.isdir(os.path.join("./Code", file))]
    code_list = {}
    for dir in code_dirs:
        codes = [file for file in os.listdir("./Code/"+dir) if os.path.isfile(os.path.join("./Code/"+dir, file))]
        for code in codes:
            tup = os.path.splitext(code)
            solution = tup[0].split('_')
            if len(solution) == 2 and len(solution[1]) == 1:
                if dir in code_list:
                    code_list[dir].append(solution[1])
                else:
                    code_list[dir] = []
                    code_list[dir].append(solution[1])
    return code_list
  

def update_readme(newReadme, profile):
    code_list = get_code_list()
    for idx in range(len(newReadme)):
        line = newReadme[idx]
        for problem_number in code_list:
            if problem_number in line:
                for author in code_list[problem_number]:
                    if profile[author] in line: 
                        continue
                    else :
                        line = line.rstrip() + profile[author]
                        line += '\n'

        newReadme[idx] = line
    return newReadme


if __name__ == "__main__":
    profile = {
        "P" : "Frog-Slayer",
        "L" : "sulogc",
        "H" : "wocjs",
        "K" : "Haaarimmm",
        "S" : "suchshin"
    }
    
    for alph in profile:
        profile[alph] = '<img src = "https://github.com/' + profile[alph] + '.png" width="25" height="25">'

    with open("./README.md", 'r', encoding='utf-8') as readme:
        newReadme = readme.readlines()
        update_readme(newReadme, profile)
        readme.close()

    with open("./README.md", 'w', encoding='utf-8') as readme:
        newReadme = "".join(newReadme)
        readme.write(newReadme)
        readme.close()
