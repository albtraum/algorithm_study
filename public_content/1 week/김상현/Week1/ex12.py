def solution(numbers):
    if numbers.count(0)==len(numbers):
      return "0"
    # "0000"과 같은 숫자는 없으므로 모든 숫자가 0이면 "0"을 출력한다.
    else:
      # idea: 10 1000 중 무엇이 앞에 와야할지 구분하는 방법은 1010 10001000 중 무엇이 앞에 있어야할지 확인하는 것
      numbers=sorted(list(map(str,numbers)),reverse=True,
      key=lambda x: (x[0],
      # 기본적으로 첫 번째, 두 번째, 세 번째, 네 번째 숫자를 순차적으로 비교하면 되지만 숫자가 모두 네자리가 아니기 때문에
      x[-1] if len(x)<=1 else x[1],
      # 길이가 1일 때는 다시 첫 번째 숫자를 두 번째 숫자와 비교해주면 된다.
      x[0] if len(x)<=2 else x[2],
      # 길이가 2보다 작을 때는 두 번째 숫자를 세 번째와 비교하면 안된다(10 1000) 위의 idea를 이용한다
      x[-1] if len(x)<=3 else x[3],
      # 길이가 3보다 작을 때는 다시 -1로 돌아와야한다. (두 번째까지 같으므로 100 1000 제외하고는 상관없음) 
      -len(x)))
      # 위에서 말한 100 1000같은 경우 숫자가 작은게 즉, 길이가 작은게 앞으로 오도록 -를 붙여주었다.
      return "".join(numbers)