// const computer = {
//     name:'macbook',
//     price:200000,
//     printInfo: function(){
//         console.log(`name: ${this.name}, price:${this.price}`)
//     }
// }

// computer.printInfo()
class MineCm {
    constructor(color,price,size){
        this.color = color
        this.price = price
        this.size = size
    }
    printCm(){
        console.log(`color:${this.color}, price:${this.price}, size::${this.size}`)
    }
}
const cloth = new MineCm('blue', 50000, 'L') 
cloth.printCm()

const Mycm ={
    color: 'red',
    price: 20000,
    size: 'XL',
    printInfo: function(){
        console.log(`color: ${this.color}, price:${this.price}, size:${this.size}`)
    }

    
}
Mycm.printInfo()