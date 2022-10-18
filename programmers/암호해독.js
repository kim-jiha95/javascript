//암호해독
function solution_3(cipher, code) {
    var answer = [];
    // cipher에서 code의 n번째 문자열 구하기
    // 합쳐서 push
    // 공백도 고려해야 됨
    for (let i = code - 1; i < cipher.length; i += code) {
        answer += cipher[i]
    }
    return answer;
}