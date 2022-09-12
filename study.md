### 리스트 관련 메소드

|메소드명|사용법|설명|시간복잡도|
|---|---|---|---|
|append()|변수명.apend()|리스트에서 원소를 하나 삽입할 때 사용한다|O(1)|
|sort()|변수명.sort()|기본 정렬 기능으로 오름차순으로 정렬한다.|O(NlogN)|
|sort()|변수명.sort(reverse=True)|내림차순으로 정렬한다.|O(NlogN)|
|reverse()|변수명.reverse()|리스트의 원소의 순서를 모두 뒤집어 놓는다.|O(N)|
|insert()|변수명.insert(삽입할 위치 인덱스, 삽입할 값)|특정한 인덱스 위치에 원소를 삽입할 때 사용한다.|O(N)|
|count()|변수명.count(특정 값)|리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때 사용한다.|O(N)|
|remove()|변수명.remove(특정 값)|특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러개 면 하나만 제거한다.|O(N)|

> insert 는 O(N)으로 남발하면 시간 초과를 발생시킬 수 있다.

> remove 는 O(N)이고, 하나만 제거한다.

> remove all 이 없는데, 여러번의 remove 를 쓰기 보다 특정 값의 set 을 만들고, comprehension 으로 처리하는게 좋다.
```python
a = [1, 2, 3, 4, 5, 6, 7]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
```

### 입력 함수
> input() 을 이용하여 데이터 입력을 받는다.

> 5  
> 65 90 75 34 99  
> 3 5 7

를 코드로 처리하면

```python
a = input()
b = list(map(int, input().split()))
n, m, k = map(int, input().split())
```

> 입력의 개수가 많을 경우 input() 함수를 그대로 사용하지 않는다.  
> 파이썬의 기본 input() 함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문이다.
> 이 경우 파이썬의 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수를 이용한다.
> readline 을 입력하면 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다.

```python
import sys

data = sys.stdin.readline().rstrip()
```

> 파이썬 3.6 이상의 버전부터 f-string 문법을 사용할 수 있다.  
> f-string은 문자열 앞에 접두사 'f'를 붙임으로써 사용할 수 있는데, f-string을 이용하면 중괄호({}) 안에 변수명을 넣으므로써 자료형을 출력할 수 있다.

> heapq는 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용된다.    
> heapq 외에도 PriorityQueue 라이브러리를 사용할 수 있지만, 코딩 테스트 환경에서는 보통 heapq 가 더 빠르게 동작하므로 heapq 를 사용한다.  
> 파이썬 heap 은 최소 힙(Min Heap)으로 구성되어 있으므로 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.  
> 힙에 원소를 삽입할 때는 heapq.heappush() 메서드를 이용하고, 힙에서 원소를 꺼내고자 할 때는 heapq.heappop() 메서드를 이용한다.    
> 파이썬은 최대 힙(Max Heap)을 제공하지 않는다.  
    > 힙에 넣을때 - 부호를 붙여서 넣고, 빼낼때 다시 - 부호를 붙이는 방법을 쓴다.

> 파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다.  
> bisect 라이브러리는 '오름차순으로 정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.   
> bisect_left, bisect_right 는 복잡도 O(logN)에 동작한다.

> deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능을 사용할 수 없다.   
> 다만, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적으로 사용될 수 있다.   
> deque는 첫 번째 원소를 제거할 때는 popleft()를, 마지막 원소를 제거할 때는 pop()를 사용한다.   
> 첫 번째 인덱스에 원소 x를 삽입할 때는 append_left(x)를 사용하면, 마지막 원소를 삽입할 때는 append(x)를 사용한다.  

> collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공한다.
```python
from collections import Counter

count = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(count)

{'red': 2, 'blue': 3, 'green':1}
```

> math 라이브러리의 gcd(a, b) 함수는 최대 공약수를 반환한다.


