//음양 더하기
function plusminus(absolutes, signs) {
    var answer = 0;
    for (let i = 0; i < signs.length; i++) {
        if (signs[i] === true) {
            answer += absolutes[i]
        }
        else {
            answer -= absolutes[i]
        }
    }
    return answer
}

console.log(plusminus([4, 7, 12], [true, false, true]));