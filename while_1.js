function fact(n){
    var k = 1, i = 1;
    while( i < 5){
        k += (++i)
    }
    return k;
}
fact(5);
console.log(fact(5));

function linearSearch(x, a){
    var i =0;
    var n = a.length;
    while(i < n && x > a[i]) i++;
    if( x ==a[i]) return i;
    return null
}
var a = [2,4,7,12,15,21,34,35,46,57,70,86,86,92,99];
console.log(linearSearch(35, a));

function fact1(n) {
    var k = 1, i = n;
    do {
        k += i--;

    }while( i >0);
    return k;
}
fact1(5)
console.log(fact1(5));