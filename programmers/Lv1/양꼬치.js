function solution(n, k) {
    var answer = 0;
    if (n / 10 > 0) {
        answer = n * 12000 + (k - parseInt(n / 10)) * 2000
    }
    else {
        answer = n * 12000 + k * 2000
    }

    return answer;
}
console.log(solution(64, 6));