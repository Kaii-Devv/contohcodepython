const gbk = (player1,player2)=> {
    const listgbk = ['gunting','batu','kertas'];
    if ((player1==listgbk[0] && player2==listgbk[1])|| (player1==listgbk[1] && player2==listgbk[2]) || (player1==listgbk[2] && player2==listgbk[0])){
        console.log('player ke 2 menang')
    }else if(player1==player2){
        console.log('permainan seri')
    }else{
        console.log('player ke 1 menang')
    }
}

class Person {
    constructor (name,age){
        this.name = name
        this.age = age
    }
    eat (){
        console.log(this.name +  ' iis eating')
    }
}
const person = new Person('muhajir',17)
console.log(person.name)
console.log(person.age)
person.eat()

class smartphone {
    constructor (model, color, brand){
        this.model = model
        this.color = color
        this.brand = brand
    }
    charging (){
        for (let x= 0;x<=100;x++){
            console.log('smartphone charging in ' + x +'%')
        }
    }
}

const sm = new smartphone('galaxy j3','red','samsung')
// console.log(sm.brand)
// console.log(sm.color)
// console.log(sm.model)

// sm.charging()

class Android extends smartphone{
    splitsc(){
        console.log('layar sudah di bagi')
    }
}
let and = new Android('galaxy j3','red','samsung')
and.splitsc()