import os as _os


def list_files(*targets):
    ans = list()
    for target in targets:
        if _os.path.isfile(target):
            if target not in ans:
                ans.append(target)
            continue
        for (root, dirnames, filenames) in _os.walk(target):
            for filename in filenames:
                file = _os.path.join(root, filename)
                if file not in ans:
                    ans.append(file)
    return ans  
