function solution(arr) {
    var answer = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== arr[i + 1]) {
            answer.push(arr[i])
        }
    }
    return answer;
}

console.log(solution([4, 4, 4, 3, 3,]));

//filter 
function solution(arr) {
    return arr.filter((val, index) => val != arr[index + 1]);
}