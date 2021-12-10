function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

const MIN_NUMBER = 1;
const MAX_NUMBER = 45;

getRandomNumber(MIN_NUMBER, MAX_NUMBER);

```
1. 최소값과 최대값을 다룬다.
2. 최소값과 최대값 포함 여부를 결정해야 한다.
3. 네이밍에 최소값과 최대값 포함 여부 명시 
```