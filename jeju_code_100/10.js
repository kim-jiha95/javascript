// for (let i = 1; i <= n; i++) {
//   let answer = ""
//   for (let k = 0; k < n - 1; k++) {
//     answer += " "
//   }

//   for (let j = 0; j < 2 * i - 1; j++) {
//     answer += "*"
//   }
//   console.log(answer)
// }

// 답안

const level = 5
let tree = ""

for (let i = 1; i <= level; i++) {
  let tree = ""
  for (let k = 1; k <= level - i; k++) {
    tree = tree + " "
  }
  for (let j = 1; j <= i * 2 - 1; j++) {
    tree = tree + "*"
  }
  console.log(tree)
}
