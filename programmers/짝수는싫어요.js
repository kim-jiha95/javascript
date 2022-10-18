//짝수는 싫어요
function solution(n) {
    var answer = [];
    for (let i = 1; i < n + 1; i += 2) {
        answer.push(`${i}`)
    }
    // n 이하의 홀수 나열 + 오름차순
    // answer에 push
    return answer;
}