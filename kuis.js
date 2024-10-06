class Animal{

    constructor (name,age,isMammal){
        this.age = age;
        this.name = name;
        this.isMammal = isMammal;
    }
}
class Rabbit extends Animal{
    constructor (name,age,isMammal){
        super(name,age,isMammal)
        this.isMammal = true
    }
    eat(){
        return `${this.name} sedang makan!`
    }
}
class Eagle extends Animal{
    constructor(name,age,isMammal){
        super(name,age,isMammal)
        this.isMammal = false
    }

    fly(){
        return `${this.name} sedang terbang!`
    }
}
const myRabbit = new Rabbit('Labi',2)

const myEagle = new Eagle('Elo',4)