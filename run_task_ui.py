import platform
from os import system as os_system
from os.path import join as os_path_join
from webbrowser import open as open_report


def main():
    os_system('pytest tests/ -n 3 --alluredir=allure-results --clean-alluredir')

    # env_data = [f'os_platform = {platform.system()}\n',
    #             f'os_release = {platform.release()}\n',
    #             f'python_version = {platform.python_version()}']
    env_data = [f'os_platform = My Os Platform\n',
                f'os_release = My Os Release\n',
                f'python_version = My Python Version',
                'test run']

    with open(os_path_join('allure-results', 'environment.properties'), 'w') as env_file:
        for line in env_data:
            env_file.write(line)

    os_system('allure generate allure-report --clean --single-file allure-results')

    open_report(os_path_join('allure-report', 'index.html'))


if __name__ == '__main__':
    main()
