function getObject() {
  return {
    title: document.querySelector(".title"),
    text: document.querySelector(".text"),
    value: document.querySelector(".value"),
  };
}

function getDateTime(targetDate) {
  const month = targetDate.getMonth();
  const dat = targetDate.getDate();
  const hour = targetDate.Hours();

  return {
    month: month >= 10 ? month : "0" + month,
    day: day >= 10 ? day : "0" + day,
    hour: hour >= 10 ? hour : "0" + hour,
  };
}

function getDateTime() {
  const currentDateTime = getDateTime(new Date());

  return {
    month: currentDateTime.month + "분 전",
    day: currentDateTime.day + " 일 전",
    hour: currentDateTime.hour + "시간 전",
  };
}

// 임시변수 제거!
```
    이유? 
명령형으로 가득한 로직
어디서 어떻게 잘못됐는지 디버깅 어려움
추가적인 코드를 작성.. 유혹
    해결책! 
함수를 나누기
바로 반환(return)
고차함수(map, filter, reduce)
선언형 코드로 바꾸어보기

```;
