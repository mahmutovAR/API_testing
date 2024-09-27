import platform
from os import getcwd, chdir
from os import system as os_system
from os.path import join as os_path_join
from webbrowser import open as open_report


def main():
    base_dir = getcwd()

    # setUp()

    chdir(base_dir)
    os_system('pytest -n 1 --alluredir=allure-results --clean-alluredir')

    # os_system('pytest --alluredir=allure-results --clean-alluredir')
    # os_system('pytest -n 5 -vv')
    # os_system('pytest -vv')

    env_data = [f'os_platform = {platform.system()}\n',
                f'os_release = {platform.release()}\n',
                f'python_version = {platform.python_version()}']

    with open(os_path_join('allure-results', 'environment.properties'), 'w') as env_file:
        for line in env_data:
            env_file.write(line)

    os_system('allure generate allure-report --clean --single-file allure-results')

    open_report(os_path_join('allure-report', 'index.html'))

    # tearDown()


def setUp():
    chdir(os_path_join(getcwd(), 'test-service'))
    os_system('docker compose up --build -d')


def tearDown():
    os_system('docker compose down')


# import multiprocessing
#
# p1 = multiprocessing.Process(target=worker, args=[1, 32])
# p2 = multiprocessing.Process(target=worker, args=[32, 64])
# p3 = multiprocessing.Process(target=worker, args=[64, 96])
# p4 = multiprocessing.Process(target=worker, args=[96, 128])
#
# # Start all the processes
# p1.start()
# p2.start()
# p3.start()
# p4.start()
#
# # Wait until all processes finish
# p1.join()
# p2.join()
# p3.join()
# p4.join()

if __name__ == '__main__':
    main()
