//1
function solution(progresses, speeds) {
    var answer = [];
    for (let i = 0; i < progresses.length; i++) {
        let a = []
        let b = []
        a.push(Math.ceil((100 - progresses[i]) / speeds[i]))
        // 이중 for문보단 filter가 좋아 보이는데,,
        if (a[i] === a[i + 1]) {
            b.push(a[i])
            answer.push(b.length)
        }
        // a 중복되면 중복끼리 묶어서
        // a 중복 안되면 앞에 기능이랑 묶어서
        console.log(a, '1');
    }
    return answer;
}

// console.log(solution([93, 30, 55], [1, 30, 5]));

//
function solution_1(progresses, speeds) {
    const answer = [];
    const days = progresses.map((progress, index) =>
        Math.ceil((100 - progress) / speeds[index])
    );
    let count = 1;
    let maxDay = days[0];

    for (let i = 1; i < days.length; i++) {
        if (days[i] <= maxDay) {
            count++;
        } else {
            maxDay = days[i];
            answer.push(count);
            count = 1;
        }
    }

    answer.push(count);

    return answer;
}
console.log(solution_1([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1]));