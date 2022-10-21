// 점의 위치 구하기
function solution(dot) {
    var answer = 0;
    if (dot[0] > 0 && dot[1] > 0) {
        answer = 1
    }
    else if (dot[0] < 0 && dot[1] > 0) {
        answer = 2
    }
    else if (dot[0] < 0 && dot[1] < 0) {
        answer = 3
    }
    else if (dot[0] > 0 && dot[1] < 0) {
        answer = 4
    }
    return answer;
}

// 다른 풀이 : 삼항연산자

function solution(dot) {
    return dot[0] > 0 ? dot[1] > 0 ? 1 : 4 : dot[1] > 0 ? 2 : 3;
}


//JadenCase 문자열 만들기
function JadenCase(s) {
    var answer = '';
    if (typeof s[0] === 'int') {
        console.log(s);
        return s
    }
    return s;
}
const test = [3 + "people"]
console.log(JadenCase(test));