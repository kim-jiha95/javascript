var a = [2, 5, -1, 7, -3, 6, 9];
for(var i = 0, sum = 0; i < a.length; i++){
    if( a[i] < 0) continue;
    sum += a[i]
}
console.log(sum);