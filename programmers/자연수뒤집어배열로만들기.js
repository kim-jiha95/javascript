
// lv0. 자연수 뒤집어 배열로 만들기
function solution_5(n) {
    var answer = []
    let result = n.toString()
    for (let i = result.length - 1; i >= 0; i--) {
        answer.push(parseInt(result[i]));
    }
    return answer
}