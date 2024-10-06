class rumah{
    #ukuran = 60;
    constructor (tembok,atap,milik){
        this.catTembok = tembok;
        this.atap = atap;
        this.pemilik = milik;
    }
    get ukuran(){
        return this.#ukuran
    }
    bukaPintu (){
        console.log(`pintu rumah ${this.pemilik} sudah di buka`)
    }
    bukaJendela(){
        console.log(`jendela rumah ${this.pemilik} sudah di buka`)
    }
    gantiCat(warna){
        this.catTembok = warna;
        console.log(`warna tembok ${this.pemilik} sudah di ubah menjadi warna${this.catTembok}`)
    }
}

class rumahLoteng extends rumah {
    naikTangga (){
        console.log(`${this.pemilik} naik ke lantai dua`)
    }
    turunTangga(){
        console.log(`${this.pemilik} turun ke lantai satu`)
    }
}

const home = new rumah('biru','genteng','adi')
console.log(home)
home.gantiCat('merah')
home.#ukuran = 1
console.log(home.ukuran)
