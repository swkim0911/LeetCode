# 정규식으로 문자열 대체
> re.sub(r'[^\w]',' ', paragraph)

정규표현식은 특수 문자를 판단하려면 \를 붙여야한다.   
r은 raw의 약자로 문자열 앞에 r을 붙여주면 원시(raw)문자열이 되어서 \를 붙이지 않아도 특수 문자를 그대로 판단할 수 있다.   
따라서 raw 문자열에는 \\숫자, \\g<이름> 는 \숫자, \g<이름> 형식처럼 \를 하나만 붙여서 사용할 수 있다. 

\w은 Unicode=숫자, underscore(\_\)를 포함하는 모든 언어의 표현가능한 문자이다.   
즉 [\w]은 [a-zA-Z0-9\_\]을 나타낸다.