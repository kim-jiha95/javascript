
/*
function solution(array, commands) {
    var answer = [];
    var bag = [];
    for (let i = commands[0] - 1; i < (commands[1] - commands[0] + 2); i++) {
        bag.push(array[i])
    }
    bag.sort()
    answer.push(bag[commands[2]] - 1)
    console.log(answer);
    return answer;
}
solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3]])
*/

//
function k(array, commands) {

    const answer = [];
    let i = 0;
    let j = 0;
    let k = 0;
    for (let m = 0; m < commands.length; m++) {
        i = commands[m][0]
        j = commands[m][1]
        k = commands[m][2]

        let sliced = array.slice(i - 1, j)
        let sorted = sliced.sort((a, b) => a - b)

        answer.push(sorted[k - 1])
    }
    return answer
}
console.log(k([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]));