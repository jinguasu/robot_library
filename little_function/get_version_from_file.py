import re
def ge_sm_version(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            version = re.match(r'BTSSM_TDD\s/\w+/\w+/BTS_SE_UI/lte/td/installer/tags/(TL\d+_BTSSM_\d+_\d+_\d+)',line)
            if version != None:
                return version.group(1)
if __name__ == '__main__':
    a = ge_sm_version('config')
    print(a)


