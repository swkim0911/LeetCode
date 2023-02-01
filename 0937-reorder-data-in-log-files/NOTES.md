# list sorting할 때 key 사용법
> logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))   

ket에 조건을 두 개이상 할 때, lambda함수 return에 튜플로 넣어준다.

> x.split()[1] vs x.split()[1:]

x.split()[1]은 split된 리스트에 첫 번째 요소만으로 비교하는 거고 x.split()[1:]은 첫 번째 이후 요소들로 비교 한다. 
즉, 첫 번째 요소가 같으면 두 번째 요소, 그 다음 번째 요소를 비교한다.
