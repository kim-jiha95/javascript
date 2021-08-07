const productList = [
  1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
]
let sum = 0

for (const price of productList) {
  sum += price
}
const avg = sum / productList.length
console.log(`합계: ${sum}, 평균: ${avg}`)
