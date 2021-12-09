function fact(n) {
    if( n < 1) return 1;
    return n*fact(n-1);
}
fact(5);
console.log(fact(5));