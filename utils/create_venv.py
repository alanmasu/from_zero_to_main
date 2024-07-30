import os
import subprocess

def check_and_update_gitignore():
    gitignore_path = '.gitignore'
    venv_entry = '.venv\n'
    
    # Controlla se il file .gitignore esiste
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as file:
            lines = file.readlines()
            
        # Controlla se .venv è già presente
        if venv_entry not in lines:
            with open(gitignore_path, 'a') as file:
                file.write(venv_entry)
            print(f'{venv_entry.strip()} è stato aggiunto a {gitignore_path}')
        else:
            print(f'{venv_entry.strip()} è già presente in {gitignore_path}')
    else:
        # Crea il file .gitignore e aggiunge .venv
        with open(gitignore_path, 'w') as file:
            file.write(venv_entry)
        print(f'{gitignore_path} è stato creato e {venv_entry.strip()} è stato aggiunto')

def create_virtual_environment():
    venv_dir = '.venv'
    
    if not os.path.exists(venv_dir):
        # Crea l'ambiente virtuale
        subprocess.run(['python3', '-m', 'venv', venv_dir])
        print(f'Ambiente virtuale creato nella directory {venv_dir}')
    else:
        print(f'L\'ambiente virtuale esiste già nella directory {venv_dir}')

if __name__ == "__main__":
    check_and_update_gitignore()
    create_virtual_environment()
