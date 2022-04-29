    # original code : https://github.com/6Soo/BOJ_maker
    # name="bojmaker",
    # version="1.3",
    # license='MIT',
    # author="6Soo",
    # author_email="kkokko-hero@hanmail.net",
    # description="Setting up bothering BOJ problems all at once.",
from calendar import month_abbr
import datetime
import os, sys, argparse, requests
from bs4 import BeautifulSoup
d=datetime.datetime.utcnow()
m='{:02d}'.format(d.month)
month_dir = (f"{d.year}-{m}")


def file_maker(folder_name, problem_input, problem_title,link):
    sol_py_content = f'''# {folder_name[3:]}번 {problem_title}
# {link}
import sys, os
sys.stdin = open('{{}}/{folder_name}.txt'.format(os.path.dirname(os.path.realpath(__file__))))
N=int(sys.stdin.readline())'''

    sol_py = open('./{}/{}/{}.py'.format(month_dir,folder_name,folder_name), 'w')
    sol_py.write(sol_py_content)
    sol_py.close()
    
    input_text = open('./{}/{}/{}.txt'.format(month_dir,folder_name,folder_name), 'w')
    input_text.write(problem_input)
    input_text.close()
    
def bojmaker(problem_number):
    url = 'https://www.acmicpc.net/problem/'
    link=url+problem_number
    html = requests.get('{}{}'.format(url, problem_number), headers={'User-Agent': 'Mozilla/5.0'}).content
    bs_object = BeautifulSoup(html, 'html.parser')
    problem_title = bs_object.find('span', id='problem_title').text
    problem_input = bs_object.find('pre', id='sample-input-1').text
    folder_name = 'BOJ'+str(problem_number)
    try:
        os.mkdir('./{}'.format(month_dir))
        print("year, month = {}".format(month_dir))
    except :
        print("year, month = {}".format(month_dir))
    try:
        os.mkdir('./{}/{}'.format(month_dir,folder_name))
    except:
        print("Already exist")
        exit()


    
    file_maker(folder_name, problem_input, problem_title,link)

    print('\n-------------------\n{}\n\nSet up completed\n-------------------\n{}{}\n'.format(folder_name, url, problem_number))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('problem_number', help="Write BOJ problem number")

    args = parser.parse_args()

    problem_number = args.problem_number

    bojmaker(problem_number)

if __name__ == "__main__":
    main()