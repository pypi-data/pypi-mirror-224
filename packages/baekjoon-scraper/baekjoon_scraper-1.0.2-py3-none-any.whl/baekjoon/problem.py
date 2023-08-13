import requests
from bs4 import BeautifulSoup
import random
from . import args

def get_question(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    question = soup.select_one("#problem_description > p")
    return question.text

def get_input(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    input = soup.select_one("#problem_input > p")
    return input.text

def get_output(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    output = soup.select_one("#problem_output > p")
    return output.text

def get_sample_input(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    sample_input = soup.select_one("#sample-input-1")
    return sample_input.text

def get_sample_output(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    sample_output = soup.select_one("#sample-output-1")
    return sample_output.text

def get_correct_rate(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    correct_rate = soup.select_one("#problem-info > tbody > tr > td:nth-child(6)")
    return correct_rate.text

def get_time_limit(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    time_cut = soup.select_one("#problem-info > tbody > tr > td:nth-child(1)")
    return time_cut.text

def get_memory_limit(number, headers={}, params={}, proxies={}):
    url = "https://www.acmicpc.net/problem/" + str(number)
    response = requests.get(**args.requestArgs(url,headers,params,proxies))
    soup = BeautifulSoup(response.text, "html.parser")
    memory_cut = soup.select_one("#problem-info > tbody > tr > td:nth-child(2)")
    return memory_cut.text

def get_random_question():
    url = "https://www.acmicpc.net/problem/" + str(random.randint(1000, 28677))
    return url

