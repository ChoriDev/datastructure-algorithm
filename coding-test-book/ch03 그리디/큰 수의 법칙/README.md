## 문제 내용

- 문제에서 정의한 큰 수의 법칙운 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
- 이때 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해서 더해질 수 없음
- 그리고 서로 다른 인덱스에 해당하는 수가 같은 경우에는 서로 다른 것으로 간주
- 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과 출력

### 입력 조건

- 첫째 줄에 N, M, K의 자연수가 주어지며 각 자연수는 공백으로 구분
- 둘째 줄에 N개의 자연수가 주어지며 각 자연수는 공백으로 구분
- 입력으로 주어지는 K는 항상 M보다 작거나 같음

### 출력 조건

- 큰 수의 법칙에 따라 더해진 답을 첫째 줄에 출력

### 입력 예시

``` shell
5 8 3
2 4 5 4 6
```

### 출력 예시

``` shell
46
```

---

## 문제 해설

- 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 됨
- 연속으로 더할 수 있는 횟수는 최대 K번이므로 **가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산**을 반복

### 다른 풀이

- 수학적 아이디어를 이용해 더 효율적으로 문제를 해결할 수 있음
- 반복되는 수열에 대한 이해가 필요
- 이 문제는 가장 큰 수와 두 번째로 큰 수가 더해질 때 특정한 수열 형태로 반복해서 더해지는 특징이 있음
- 반복되는 수열의 길이는 (K + 1)
- 따라서 M을 (K + 1)로 나눈 몫이 수열이 반복되는 횟수이며 다시 여기에 K를 곱하면 가장 큰 수가 등장하는 횟수가 됨
- M이 (K + 1)로 나누어떨어지지 않는 경우도 고려해야 하는데 그럴 때는 M을 (K + 1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해져야 함
- 즉 가장 큰 수가 더해지는 횟수는 `int(M / (K + 1)) * K + M % (K + 1)`
- 위 식으로 가장 큰 수가 더해지는 횟수를 구한 다음, 이를 이용해 두 번째로 큰 수가 더해지는 횟수까지  구할 수 있음