# Fluent Python
## 목차
1. [CH01 파이썬 데이터 모델](https://github.com/heaven324/Python/blob/master/Fluent_python/ch01.ipynb)
2. [CH02 시퀀스](https://github.com/heaven324/Python/blob/master/Fluent_python/ch02.ipynb)
3. [CH03 딕셔너리와 집합](https://github.com/heaven324/Python/blob/master/Fluent_python/ch03.ipynb)


## CH01, 파이썬 데이터 모델 ([view code](https://github.com/heaven324/Python/blob/master/Fluent_python/ch01.ipynb))

1. 특별 메서드
    - `__?__()` 메서드를 던더 메서드(dunder method)라고 통용해서 부름

### 특별 메서드명(연산자 제외)
| **범주**           | **메서드명**                                                                          |
|--------------------|---------------------------------------------------------------------------------------|
| 문자열/바이트 표현 | `__repr__`, `__str__`, `__format__`, `__bytes__`                                      |
| 숫자로 변환        | `__abs__`, `__bool__`, `__complex__`, `__int__`, `__float__`, `__hash__`, `__index__` |
| 컬렉션 에뮬레이션  | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`                |
| 반복               | `__iter__`, `__reversed__`, `__next__`                                                |
| 콜러블 에뮬레이션  | `__call__`                                                                            |
| 콘텍스트 관리      | `__enter__`, `__exit__`                                                               |
| 객체 생성 및 소멸  | `__new__`, `__init__`, `__del__`                                                      |
| 속성 관리          | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__`            |
| 속성 디스크립터    | `__get__`, `__set__`, `__delete__`                                                    |
| 클래스 서비스      | `__prepare__`, `__instancecheck__`, `__subclasscheck__`                               |

### 연산자에 대한 특별 메서드명
| **범주**              | **메서드명 및 관련 연산자**                                                                                                                                     |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 단항 수치 연산자      | `__neg__` -, `__pos__` +, `__abs__` `abs()`                                                                                                                     |
| 향상된 비교 연산자    | `__lt__` <, `__le__` <=, `__eq__` ==, `__ne__` !=, `__gt__` >, `__ge__` >=                                                                                      |
| 산술 연산자           | `__add__` +, `__sub__` -, `__mul__` *, `__truediv__` /, `__floordiv__` //, `__mod__` %, `__divmod__` `divmod()`, `__pow__` ** or `pow()`, `__round__` `round()` |
| 역순 산술 연산자      | `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`, `__rfloordiv__`, `__rmod__`, `__rdivmod__`, `__rpow__`                                                      |
| 복합 할당 산술 연산자 | `__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, `__ifloordiv__`, `__imod__`, `__ipow__`                                                                     |
| 비트 연산자           | `__invert__` ~, `__lshift__` <<, `__rshift__` >>, `__and__` &, `__or__` \|, `__xor__` ^                                                                         |
| 역순 비트 연산자      | `__rlshift__`, `__rrshift__`, `__rand__`, `__rxor__`, `__ror__`                                                                                                 |
| 복합 할당 비트 연산자 | `__ilshift__`, `__irshift__`, `__iand__`, `__ixor__`, `__ior__`                                                                                                 |


## CH02, 시퀀스 ([view code](https://github.com/heaven324/Python/blob/master/Fluent_python/ch02.ipynb))

| 시퀀스 형                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------|
| 컨테이너 시퀀스(메모리 참조) </br> -> 서로 다른 자료형의 항목들을 담을 수 있는 list, tuple, collections, deque 형  |
| 균일 시퀀스(직접 할당) </br> -> 단 하나의 자료형만 담을 수 있는 str, bytes, bytearray, memoryview, array, array 형 |
| 가변 시퀀스 </br> -> list, bytearray, array.array, collections.deque, memoryview 형                                |
| 불변 시퀀스 </br> -> tuple, str, bytes 형                                                                          |

### 지능형 리스트
- [ for 문 ]과 같은 형태의 리스트
- python3에서는 지능형 리스트 내부의 변수와 외부의 변수명이 같을 때도 값이 혼용되지 않는다.
- 내장된 `filter()`와 `map()`함수를 사용해서 리스트를 만듦.
- 두 개 이상의 반복 가능한 자료형의 데카르트 곱을 나타내는 일련의 리스트를 만들 수 있다.

### 제너레이터 표현식
- 지능형 리스트처럼 리스트를 통째로 만들지 않고 반복자 프로토콜을 이용해서 항목을 하나씩 생성(메모리를 더 적게 사용함)

### 레코드로서의 튜플
- 튜플 언패킹을 이용해 병렬할당
- *를 사용해 초과 항목 할당 가능
- 내포된 튜플도 언패킹 가능
- `collections.namedtuple()`을 사용하여 필드명과 클래스명을 추가한 서브클래스 생성 가능
    - `_make()`으로 튜플을 생성하고, `_asdict()`으로 `Collection.OderedDict()` 객체 반환 가능

### 불변 리스트로서의 튜플
리스트나 튜플에서 지원되는 메서드
  
- | method                     | list | tuple | 설명                                                                      |
  |:---------------------------|:----:|:-----:|:--------------------------------------------------------------------------|
  | `s.__add__(s2)`            | o    | o     | `s + s2` -- 리스트를 연결한다.                                            |
  | `s.__iadd__(s2)`           | o    |       | `s += s2` -- 리스트를 연결하고 `s`에 저장한다.                            |
  | `s.append(e)`              | o    |       | 제일 뒤에 요소를 하나 추가한다.                                           |
  | `s.clear()`                | o    | o     | 모든 항목을 삭제한다.                                                     |
  | `s.__contains__(e)`        | o    |       | `e` in `s`                                                                |
  | `s.copy()`                 | o    |       | 리스트를 얕게 복사한다.                                                   |
  | `s.count(e)`               | o    | o     | `e`가 발생한 횟수를 계산한다.                                             |
  | `s.__delitem__(p)`         | o    |       | `p`위치의 요소를 삭제한다.                                                |
  | `s.extend(it)`             | o    |       | 반복형 `it`안에있는 요소를 추가한다.                                      |
  | `s.__getitem__(p)`         | o    | o     | `s[p]` -- `p`위치의 항목을 가져온다.                                      |
  | `s.__getnewargs__()`       |      | o     | pickle을 이용해서 최적화된 직렬화를 지원한다.                             |
  | `s.index(e)`               | o    | o     | `s`안에서 `e`가 처음 나타나는 위치를 찾는다.                              |
  | `s.insert(p, e)`           | o    |       | `p`위치에 있는 요소 앞에 `e`요소를 삽입한다.                              |
  | `s.__iter__()`             | o    | o     | 반복자를 가져온다.                                                        |
  | `s.__len__()`              | o    | o     | `len(s)` -- 항목 개수를 구한다.                                           |
  | `s.__mul__(n)`             | o    | o     | `s * n` -- 문자열을 반복한다.                                             |
  | `s._imul__(n)`             | o    |       | `s *= n` -- 문자열을 반복하여 `s`에 저장한다.                             |
  | `s.__rmul__(n)`            | o    | o     | `n * s` -- 역순 반복 추가 메서드.                                         |
  | `s.pop([p])`               | o    |       | 마지막 항목이나 `p`위치의 항목을 제거하고 반환한다.                       |
  | `s.remove(e)`              | o    |       | `e`값을 가진 첫 번째 항목을 삭제한다.                                     |
  | `s.reverse()`              | o    |       | 항목을 역순으로 배치한 후 `s`에 저장한다.                                 |
  | `s.__reversed__()`         | o    |       | 마지막에서 첫 번째 항목까지 반복하는 반복자를 반환한다.                   |
  | `s.__setitem__(p, e)`      | o    |       | `s[p] = e` -- `e`를 `p`위치에 저장하고, 기존 항목을 덮어쓴다.             |
  | `s.sort([key], [reverse])` | o    |       | 선택적인 키워드 `key`와 `reverse`에 따라 항목을 정렬하고 `s`에 저장한다.  |

### 슬라이싱
- 슬라이스에 네이밍을 하면 가독성이 좋아질 수 있다.
- 동일한 리스트에 대한 세 개의 참조(+ or *)를 가진 리스트는 쓸모없다.
- 시퀀스의 복합 할당에서는 시퀀스가 가변인지 불변인지에 따라서 객체의 정체성이 바뀐다.(가변은 기존 객체의 내용을 변경)

### 정렬된 시퀀스를 bisect로 관리하기
- `bisect`모듈이 표준 이진 검색 알고리즘을 제공.

### 배열(array)
- `array.tofile()`과 `array.fromfile()`로 배열을 이진파일(.bin)에 저장하고 빠르게 불러올 수 있다.(속도와 용량에 유리함)
- 리스트와 배열에서 볼 수 있는 메서드와 속성
  
  - | method                     | list | array | 설명                                                                                     |
    |:---------------------------|:----:|:-----:|:-----------------------------------------------------------------------------------------|
    | `s.__add__(s2)`            | o    | o     | `s + s2` -- 연결한다.                                                                    |
    | `s.__iadd__(s2)`           | o    | o     | `s += s2` -- 연결하고 `s`에 저장한다.                                                    |
    | `s.append(e)`              | o    | o     | 마지막 요소 뒤에 `e`를 추가한다.                                                         |
    | `s.byteswap()`             |      | o     | 엔디언 변환을 위해 배열 안의 모든 요소의 바이트 순서를 바꾼다.                           |
    | `s.clear()`                | o    |       | 모든 항목을 삭제한다.                                                                    |
    | `s.__contains__(e)`        | o    | o     | `e` in `s`                                                                               |
    | `s.copy()`                 | o    |       | 리스트를 얕게 복사한다.                                                                  |
    | `s.__copy__()`             |      | o     | `copy.copy()`메서드를 지원한다.                                                          |
    | `s.count(e)`               | o    |       | `s`안에 `e`요소가 발생한 횟수를 계산한다.                                                |
    | `s.__deepcopy__()`         |      | o     | `copy.deepcopy()`를 최적화해서 지원한다.                                                 |
    | `s.__delitem__(p)`         | o    | o     | `p`위치의 요소를 삭제한다.                                                               |
    | `s.extend(it)`             | o    | o     | 반복형 `it`에서 요소들을 가져와서 추가한다.                                              |
    | `s.frombytes(b)`           |      | o     | 패킹된 기계값으로 해석한 바이트 시퀀스에서 요소를 가져와서 추가한다.                     |
    | `s.fromfile(f, n)`         |      | o     | 패킹된 기계값으로 해석한 이진 파일 `f`에서 `n`개의 항목을 가져와서 추가한다.             |
    | `s.fromlist(l)`            |      | o     | 리스트 `l`의 요소를 추가한다. TypeError가 한번이라도 발생하면 아무 것도 추가하지 않는다. |
    | `s.__getitem__(p)`         | o    | o     | `s[p]` -- `p`위치의 항목을 가져온다.                                                     |
    | `s.index(e)`               | o    | o     | `e`가 처음 나타나는 위치를 찾는다.                                                       |
    | `s.insert(p, e)`           | o    | o     | `p`위치에 있는 항목 앞에 `e`요소를 삽입한다.                                             |
    | `s.itemsize`               |      | o     | 각 배열 항목의 바이트 단위 크기                                                          |
    | `s.__iter__()`             | o    | o     | 반복자를 가져온다.                                                                       |
    | `s.__len__()`              | o    | o     | `len(s)` -- 항목 수를 반환한다.                                                          |
    | `s.__mul__(n)`             | o    | o     | `s * n` -- `n`회 반복해서 연결한다.                                                      |
    | `s._imul__(n)`             | o    | o     | `s *= n` -- `n`회 반복해서 연결한 후 `s`에 저장한다.                                     |
    | `s.__rmul__(n)`            | o    | o     | `n * s` -- 역순 반복 연결 메서드                                                         |
    | `s.pop([p])`               | o    | o     | `p`위치 혹은 제일 마지막 항목을 제거하고 반환한다.                                       |
    | `s.remove(e)`              | o    | o     | 값이 `e`와 일치하는 항목을 제거한다.                                                     |
    | `s.reverse()`              | o    | o     | 항목들의 순서를 역으로 나열해서 다시 `s`에 저장한다.                                     |
    | `s.__reversed__()`         | o    |       | 마지막부터 처음까지 반복하는 반복자를 반환한다.                                          |
    | `s.__setitem__(p, e)`      | o    | o     | `s[p] = e` -- `p`위치에 `e`요소를 저장하고, 기존 값을 덮어쓴다.                          |
    | `s.sort([key], [reverse])` | o    |       | 선택적인 키워드 `key`와 `reverse`에 따라 항목을 정렬하고 `s`에 저장한다.                 |
    | `s.tobytes`                |      | o     | bytes 객체에 패킹된 기계값으로 항목을 반환한다.                                          |
    | `s.tofile(f)`              |      | o     | 이진 파일 f에 패킹된 기계값으로 항목을 저장한다.                                         |
    | `s.tolist()`               |      | o     | 항목을 수치형 객체로 변환해서 넣은 리스트를 반환한다.                                    |
    | `s.typecode`               |      | o     | 항목의 C 형을 나타내는 한 글자짜리 문자열                                                |

### 덱 및 기타 큐
덱(`collections.deque`) 클래스는 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 스레드 안전한 양방향 큐다.

리스트나 덱에 구현된 메서드
- | method                     | list | deque | 설명                                                                          |
  |:---------------------------|:----:|:-----:|:------------------------------------------------------------------------------|
  | `s.__add__(s2)`            | o    |       | `s + s2` -- 연결한다.                                                         |
  | `s.__iadd__(s2)`           | o    | o     | `s += s2` -- 연결한 후 `s`에 저장한다.                                        |
  | `s.append(e)`              | o    | o     | 마지막 항목 오른쪽에 요소 하나를 추가한다.                                    |
  | `s.appendleft(e)`          |      | o     | 첫 번째 항목 왼쪽에 요소 하나를 추가한다.                                     |
  | `s.clear()`                | o    | o     | 모든 항목을 제거한다.                                                         |
  | `s.__contains__(e)`        | o    |       | `e` in `s`                                                                    |
  | `s.copy()`                 | o    |       | 목록을 얕게 복사한다.                                                         |
  | `s.__copy__()`             |      | o     | `copy.copy()`지원(얕은 복사)                                                  |
  | `s.count(e)`               | o    | o     | `e`요소가 발생한 횟수를 반환한다.                                             |
  | `s.__delitem__(p)`         | o    | o     | `p`위치의 항목을 삭제한다.                                                    |
  | `s.extend(i)`              | o    | o     | 반복 가능한 `i`에 있는 요소를 오른쪽에 추가한다.                              |
  | `s.extendleft(i)`          |      | o     | 반복 가능한 `i`에 있는 요소를 왼쪽에 추가한다.                                |
  | `s.__getitem__(p)`         | o    | o     | `s[p]` -- `p`위치의 항목을 가져온다.                                          |
  | `s.index(e)`               | o    |       | 처음 `e`가 나타난 위치를 반환한다.                                            |
  | `s.insert(p, e)`           | o    |       | `p`위치의 항목 앞에 `e`요소를 추가한다.                                       |
  | `s.__iter__()`             | o    | o     | 반복자를 반환한다.                                                            |
  | `s.__len__()`              | o    | o     | `len(s)` -- 항목 수를 반환한다.                                               |
  | `s.__mul__(n)`             | o    |       | `s * n` -- 반복해서 연결한다.                                                 |
  | `s._imul__(n)`             | o    |       | `s *= n` -- 반복해서 연결한 후 `s`에 저장한다.                                |
  | `s.__rmul__(n)`            | o    |       | `n * s` -- 역순 반복 연결.                                                    |
  | `s.pop([p])`               | o    | o     | 마지막 항목을 삭제하고 반환한다.                                              |
  | `s.popleft([p])`           |      | o     | 첫 번째 항목을 삭제하고 반환한다.                                             |
  | `s.remove(e)`              | o    | o     | `e`와 같은 값을 가진 첫 번째 항목을 삭제한다.                                 |
  | `s.reverse()`              | o    | o     | 항목을 역순으로 나열해서 다시 `s`에 저장한다.                                 |
  | `s.__reversed__()`         | o    | o     | 뒤에서부터 앞으로 나열하는 반복자를 반환한다.                                 |
  | `s.rotate(n)`              |      | o     | 한쪽에 있는 `n`개의 항목을 반대쪽으로 이동시킨다.                             |
  | `s.__setitem__(p, e)`      | o    | o     | `s[p] = e` -- `p`위치에 `e`값을 저장하고, 기존 값을 덮어쓴다.                 |
  | `s.sort([key], [reverse])` | o    |       | 선택적인 키워드 인수 `key`와 `reverse`에 따라 항목을 정렬하고 `s`에 저장한다. |



## CH03, 딕셔너리와 집합 ([view code](https://github.com/heaven324/Python/blob/master/Fluent_python/ch03.ipynb))

딕셔너리에 여러 매핑형이 사용될 수 있기 때문에 함수 인수를 검사할 때 `dict`형인지 검사하는 것보다 `isinstance()` 함수를 사용하는 것이 좋다.

### 해시 가능성
- `str, byte, 수치형, frozenset` 은 모두 해시 가능하다.
- 튜플은 들어있는 항목들이 모두 해시 가능해야 해시 가능하다.
- `dict`는 키가 해시 가능해야한다.

### 지능형 딕셔너리
- listcomp와 비슷한 구문이 많다.

### 공통적인 매핑 메서드(`dict`, `collections.defaultdict`, `collections.OrderedDict`)
| 메서드                       | dict | defaultdict | OrderedDict | 설명                                                                                       |
|:-----------------------------|:----:|:-----------:|:-----------:|:-------------------------------------------------------------------------------------------|
| `d.clear()`                  | o    | o           | o           | 모든 항목을 제거한다.                                                                      |
| `d.default_factory`          |      | o           |             | 빠진 값을 설정하기 위해 `__missing__()`메서드에 호출되는 콜러블                            |
| `d.__delitem__(k)`           | o    | o           | o           | `del d[k]` -- 키가 `k`인 항목을 제거한다.                                                  |
| `d.fromkeys(it, [initial])`  | o    | o           | o           | 선택적인 초깃값(기본값은 `None`)을 받아, 반복 가능한 객체의 키들을 이용해서 새로 매핑한다. |
| `d.get(k, [default])`        | o    | o           | o           | `k`키를 가진 항목을 반환한다. 해당 항목이 없으면 `default`나 `None`을 반환한다.            |
| `d.__getitem__(k)`           | o    | o           | o           | `d[k]` -- `k`키를 가진 항목을 반환한다.                                                    |
| `d.items()`                  | o    | o           | o           | (키, 값)쌍으로 구성된 항목들의 뷰를 가져온다.                                              |
| `d.__iter__()`               | o    | o           | o           | 키에 대한 반복자를 가져온다.                                                               |
| `d.keys()`                   | o    | o           | o           | 키에 대한 뷰를 가져온다.                                                                   |
| `d.__len__()`                | o    | o           | o           | `len(d)` -- 항목 수를 반환한다.                                                            |
| `d.__missing__(k)`           |      | o           |             | `__getitem__()`이 `k`키를 찾을 수 없을 때 호출된다.                                        |
| `d.move_to_end(k, [last])`   |      |             | o           | 앞이나 뒤에서 `k`개의 항목을 이동한다(`last`의 기본값은 `True`다).                         |
| `d.pop(k, [defualt])`        | o    | o           | o           | `k`키 항목을 제거하고 반환한다. 항목이 없으면 `default`나 `None`을 반환한다.               |
| `d.popitem()`                | o    | o           | o           | 처음이나 마지막 (키, 값)항목을 제거하고 반환한다.                                          |
| `d.__reversed__()`           |      |             | o           | 키에 대한 역순 반복자를 가져온다.                                                          |
| `d.setdefault(k, [default])` | o    | o           | o           | `k in d`가 참이면 `d[k]`를 반환하고, 아니면 `d[k] = default`로 설정하고 이 값을 반환한다.  |
| `d.__setitem__(k, v)`        | o    | o           | o           | `d[k] = v` -- `k`키를 가진 항목의 값을 `v`로 설정한다.                                     |
| `d.update(m, [**kargs])`     | o    | o           | o           | (키, 값)쌍의 매핑이나 반복형 객체에서 가져온 항목들로 `d`를 갱신한다.                      |
| `d.values()`                 | o    | o           | o           | 값들에 대한 뷰를 가져온다.                                                                 |


### 그 외 매핑형
- `collections.OrderedDict`
  - 키를 삽입한 순서대로 유지
- `collections.ChainMap`
  - 매핑 목록을 담고있으며 한꺼번에 모두 검색할 수 있다.
- `collections.Counter`
  - 모든 키에 정수형 카운터를 갖고 있는 매핑.

### 집합
- 고유 객체 모음(중복 제거)
- 요소는 반드시 해시 가능해야 한다.
- 중위 연산자(`|`, `&`, `-`)로 기본적인 집합연산 구현.
  - 기본적으로 집합형일때 반복문보다 빠르지만, 둘중 하나라도 집합형이라면 반복문보다 빠르다.(해시 테이블 덕분)
- `frozenset`은 별도의 리터럴 구문은 없으며, 생성자를 호출해서 생성해야 한다.
- listcomp 형태를 이용해서 집합을 생성할 수도 있다.

#### 집합 연산
수학 집합 연산
- | 수학 기호 | 파이썬 연산자 | 메서드                                   | 설명                                                                     |
  |:---------:|:-------------:|:-----------------------------------------|:-------------------------------------------------------------------------|
  | `S ∩ Z`   | `s & z`       | `s.__and__(z)`                           | `s`와 `z`의 교집합                                                       |
  |           | `z & s`       | `s.__rand__(z)`                          | 역순 `&`연산자                                                           |
  |           |               | `s.intersection(it, ...)`                | 반복 가능한 `it`로 만들어진 집합과 `s`의 교집합                          |
  |           | `s &= z`      | `s.__iand__(z)`                          | `s`와 `z`의 교집합으로 `s`를 갱신한다.                                   |
  |           |               | `s.intersection_update(it, ...)`         | 반복 가능한 `it`로 만들어진 집합과 `s`의 교집합으로 `s`를 갱신한다.      |
  | `S ∪ Z`   | `s \| z`      | `s.__or__(z)`                            | `s`와 `z`의 합집합                                                       |
  |           | `z \| s`      | `s.__ror__(z)`                           | 역순 `\|` 연산자                                                         |
  |           |               | `s.union(it, ...)`                       | 반복 가능한 `it`로 만들어진 집합과 `s`의                                 |
  |           | `s \|= z`     | `s.__ior__(z)`                           | `s`와 `z`의 합집합으로 `s`를 갱신한다.                                   |
  |           |               | `s.update(it, ...)`                      | 반복 가능한 `it`로 만들어진 집합과 `s`합집합으로 `s`를 갱신한다.         |
  | `S \ Z`   | `s - z`       | `s.__sub__(z)`                           | `s`에서 `z`를 뺀 차집합                                                  |
  |           | `z - s`       | `s.__rsub__(z)`                          | 역순 `-`연산자                                                           |
  |           |               | `s.difference(it, ...)`                  | `s`에서 반복 가능한 `it`로 만들어진 집합을 뺀 차집합                     |
  |           | `s -= z`      | `s.__isub__(z)`                          | `s`에서 `z`를 뺀 차집합으로 `s`를 갱신한다.                              |
  |           |               | `s.difference_update(it, ...)`           | `s`에서 반복 가능한 `it`로 만들어진 집합을 뺀 차집합으로 `s`를 갱신한다. |
  |           |               | `s.symmetric_difference(it, ...)`        | `s & set(it)`의 여집합                                                   |
  | `S ∆ Z`   | `s ^ z`       | `s.__xor__(z)`                           | 대칭자(`s & z`의 여집합)                                                 |
  |           | `z ^ s`       | `s.__rxorv__(z)`                         | 역순 `^` 연산자                                                          |
  |           |               | `s.symmetric_difference_update(it, ...)` | 반복 가능한 `it`로 만들어진 집합과 `s`의 대칭자로 `s`를 갱신한다.        |
  |           | `s ^= z`      | `s.v_ixorv_(z)`                          | `s`와 `z`의 대칭자로 `s`를 갱신한다.                                     |

불리언형을 반환하는 비교 연산자와 메서드
- | 수학 기호 | 파이썬 연산자 | 메서드                                   | 설명                                                                     |
  |:---------:|:-------------:|:-----------------------------------------|:-------------------------------------------------------------------------|
  |           |               | `s.indisjoint(z)`                        | `s`와 `z`의 공통 요소가 없다.                                            |
  | `e ∊ S`   | `e in s`      | `s.__contains__(e)`                      | `e`가 `s`의 요소이다.                                                    |
  | `S ⊆ Z`   | `s <= z`      | `s.__le__(z)`                            | `s`가 `z`의 부분집합이다.                                                |
  |           |               | `s.issubset(it)`                         | `s`가 반복 가능한 `it`로 생성한 집합의 부분집합이다.                     |
  | `S ⊂ Z`   | `s < z`       | `s.__lt__(z)`                            | `s`가 `z`의 진부분집합이다.                                              |
  | `S ⊇ Z`   | `s >= z`      | `s.__gev_(z)`                            | `s`가 `z`의 상위집합이다.                                                |
  |           |               | `s.issuperset(it)`                       | `s`가 반복 가능한 `it`로 생성한 집합의 상위집합이다.                     |
  | `S ⊃ Z`   | `s > z`       | `s.__gt__(z)`                            | `s`가 `z`의 진상위집합이다.                                              |

그 외 집합 메서드
- | 메서드         | set | frozenset | 설명                                                                           |
  |:---------------|:---:|:---------:|:-------------------------------------------------------------------------------|
  | `s.add(e)`     | o   |           | `e`요소를 `s`에 추가한다.                                                      |
  | `s.clear()`    | o   |           | `s`에 들어있는 요소를 모두 제거한다.                                           |
  | `s.copy()`     | o   | o         | `s`의 얕은 복사                                                                |
  | `s.discard(e)` | o   |           | `s`안에 `e`요소가 있으면 제거한다.                                             |
  | `s.__iter__()` | o   | o         | `s`의 반복자를 반환한다.                                                       |
  | `s.__len__()`  | o   | o         | `len(s)`                                                                       |
  | `s.pop()`      | o   |           | `s`에서 항목 하나를 제거하고 반환한다. `s`가 공집합이면 `KeyError`가 발생한다. |
  | `s.remove(e)`  | o   |           | `s`에서 `e`항목을 제거한다. `s`에 `e`가 없으면 `KeyError`가 발생한다.          |

### `dict`와 `set`의 내부 구조
- 파이썬 `dict`와 `set`은 얼마나 효율적인가?
  - `in` 연산자로 1000개의 키를 검색하는 데 걸린 시간.(`found = len(needles & haystack)`)
    - | `haystack`의 크기 | 계수    | `dict`시간 | 계수  | `set`시간 | 계수  | `set&`시간 | 계수  | `list`시간 | 계수      |
      |:------------------|:--------|-----------:|:------|----------:|:------|-----------:|:------|-----------:|:----------|
      | 1,000             | 1x      | 0.000202s  | 1.00x | 0.000143s | 1.00x | 0.000087s  | 1.00x | 0.010556s  | 1.00x     |
      | 10,000            | 10x     | 0.000140s  | 0.69x | 0.000147s | 1.03x | 0.000092s  | 1.06x | 0.086586s  | 8.20x     |
      | 100,000           | 10x     | 0.000228s  | 1.13x | 0.000241s | 1.69x | 0.000163s  | 1.87x | 0.871560s  | 82.57x    |
      | 1,000,000         | 1,000x  | 0.000290s  | 1.44x | 0.000332s | 2.32x | 0.000250s  | 2.87x | 9.189616s  | 870.56x   |
      | 10,000,000        | 10,000x | 0.000337s  | 1.67x | 0.000387s | 2.71x | 0.000314s  | 3.61x | 97.948056s | 9,278.90x |

- 왜 순서가 없을까?
- `dict`의 키와 `set`항목에 파이썬의 모든 객체를 사용할 수 없는 이유는 무엇인가?
  - `dict`와 `set`은 해시 테이블에 기반해 동작한다. 따라서 해시 가능한 객체만 사용할 수 있다.
- `dict`의 키와 `set`항목의 순서가 왜 삽입 순서에 따라 달라지며, 객체 수명주기 동안 이 순서가 바뀔 수 있는 이유는 무엇일까?
  - `dict`와 `set`은 해시 테이블에 기반해 동작한다. 따라서 해시 충돌이 발생할 경우 키의 순서가 달라지기 때문에 항목의 순서가 삽입 순서에 따라 달라지며, 항목을 추가할 때 마다 해시 테이블의 크기를 늘릴지 판단(버킷의 1/3 여유공간을 갖기 위해)하고, 크기를 늘릴 경우 새 공간에 새 테이블을 만들어서 할당하므로 이 과정 동안 해시 충돌이 발생해서 새 해시 테이블의 키 순서가 달라질 수 있다.
- 딕셔너리와 집합을 반복하는 동안 항목을 추가하면 왜 안될까?
  - `dict`와 `set`은 해시 테이블에 기반해 동작한다. 따라서 항목을 추가하면 항목의 순서가 달라질 수 있으므로, 반복하는 동안 항목을 추가해서는 안된다.