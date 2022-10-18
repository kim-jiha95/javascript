//문자열 정렬하기
function solution(my_string) {
    var answer = [];
    const regex = /[^0-9]/g;
    const test = my_string.replace(regex, '')
    const numChunks = Math.ceil(test.length / 1);
    for (let i = 0, o = 0; i < numChunks; ++i, o += 1) {
        answer[i] = parseInt(test.substr(o, 1));
    }
    return answer.sort();
}