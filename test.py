from typing import List
HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''Returns a list of requirements'''
    with open(file_path, 'r') as f:
        require = [line.strip() for line in f.readlines() if not line.startswith('#')]
    if HYPHEN_E_DOT in require:
        require.remove(HYPHEN_E_DOT)
    return require

print(get_requirements('requirements.txt'))