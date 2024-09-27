from os import system as os_system
from os import getcwd, chdir
from os.path import join as os_path_join


def main():
    chdir(os_path_join(getcwd(), 'test-service'))
    os_system('docker compose up --build -d')


if __name__ == '__main__':
    main()
