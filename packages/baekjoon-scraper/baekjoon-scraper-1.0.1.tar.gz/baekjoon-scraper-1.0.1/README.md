# baekjoon-scrapper-api
This is a fork of smartwe's baekjoon-api. The original api is currently broken because it does not pass baekjoon's bot detection.
## solved.ac & acmicpc.net api
  
### installing requirements
```
pip install baekjoon
```
  
  How to use [boj]
  ```Python
  from baekjoon import boj
  
  user = "smartwe"
  
  boj.get_status_message(user) #사용자 이름
  
  boj.get_rank(user) #백준 랭크(순위)
  
  boj.get_correct_qs(user) #맞은 문제들
  
  boj.get_correct_q(user) #맞은 문제의 개수
  
  boj.get_unsolved_qs(user) #시도했지만 맞지 못한 문제들
  
  boj.get_unsolved_q(user) #시도했지만 맞지 못한 문제의 개수
  
  boj.get_submit_time(user) #제출 개수
  ```
  
  How to use [solved.ac]
  ```Python
  from baekjoon import solvedac
  
  user = "smartwe"
  
  solvedac.get_tier(user) #티어
  
  solvedac.get_ac_rating(user) #AC RATING
  
  solvedac.get_exp(user) #EXP
  
  solvedac.get_rank(user) #solved.ac 기준 랭크 (순위)
  ```
  
  How to use [problems]
  ```Python
  from baekjoon import problem
  
  q_num = 1000 #정수와 문자열 상관없음
  
  user = "smartwe"
  
  problem.get_question(q_num) #문제를 가져옴
  
  problem.get_input(q_num) #문제의 입력 조건을 가져옴
  
  problem.get_output(q_num) #문제의 출력 조건을 가져옴
  
  problem.get_sample_input(q_num) #문제의 예제 입력을 가져옴 (테스트케이스 1만 가능 현재까지는(쩝))
  
  problem.get_sample_output(q_num) #문제의 예제 출력을 가져옴 (테스트케이스 1만 가능 현재까지는(쩝))
  
  problem.get_correct_rate(q_num) #문제의 정답 비율을 가져옴
  
  problem.get_time_limit(q_num) #문제의 시간 제한을 가져옴
  
  problem.get_memory_limit(q_num) #문제의 메모리 제한을 가져옴
  
  problem.get_random_question() #랜덤 문제를 가져옴 채첨 못하는 문제도 있음 (쩝)
  ```
  
  Optional parameters for scraping to avoid Baekjoon's bot detection
  (The parameters work on every function that uses requests.get())
  ```Python
    #Template: <module>.<api>(user_name,headers,params,proxies)
    #Passing in {} for any any argument after user_name uses default value from requests.get()
    #Example:
    from baekjoon import boj

    user = "smartwe"

    boj.get_status_message(user,{'User-Agent': '<user agent>'},{'somekey': 'somevalue', 'somekey2': 'somevalue2'},{"http":"http://0.0.0.0:80","https":"https://0.0.0.0:422","ftp":"ftp://0.0.0.0:21"}) 
  ```
  Currently, just passing a believable user-agent bypasses Baekjoon's detection, but you may need to implement fancier tricks such as ID address rotation when using this API on larger scales.