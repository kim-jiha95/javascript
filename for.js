function sumArray(a) {
    var sum = 0;
    for(var i=0; i < a.length; i++) {
        sum += a[i];
    }
    return sum
}
var a = [3,5,7,9,11];
console.log(sumArray(a)); 


var obj = {a:1, b:2, c:3};
for(var p in obj) {
    console.log("p =" + p);
}