const sampleProducts = [
    { id: 1, name: 'Laptop', category: 'Electronics', price: 1000 },
    { id: 2, name: 'Phone', category: 'Electronics', price: 500 },
    { id: 3, name: 'Shirt', category: 'Apparel', price: 50 },
    { id: 4, name: 'Shoes', category: 'Apparel', price: 80 },
    { id: 5, name: 'Watch', category: 'Accessories', price: 200 },
  ];
console.log()
function getProductsByCategory(products, category) {
    return [...products].filter((prod)=> prod.category==category)

/**
 * TODO:
 * Gunakan metode array immutable untuk mengembalikan array produk yang termasuk dalam kategori yang diberikan.
 */
}

function findProductById(products, id) {
    return [...products].find((ids)=>ids['id']==id)
/**
 * TODO:
 * Gunakan metode array immutable untuk mengembalikan produk dengan ID yang cocok.
 */
}

function calculateTotalPrice(products) {
    let jumlah = 0;
    [...products].forEach(element => {
        jumlah = jumlah + element.price
    });
    return jumlah
/**
 * TODO:
 * Gunakan metode array immutable untuk menghitung total harga semua produk.
 */
}

function applyDiscount(products, discount) {
    return [...products].map((nama)=>{
        return {...nama,price:nama.price*(1-(discount/100))}
    })
/**
 * TODO:
 * Gunakan metode array immutable untuk mengembalikan array baru,
 * di mana setiap produk memiliki harga yang sudah dikurangi dengan diskon yang diberikan.
 */
}

console.log(getProductsByCategory(sampleProducts, 'Electronics')); // Should return products with id 1 and 2
console.log(calculateTotalPrice(sampleProducts)); // Should return 1830
console.log(applyDiscount(sampleProducts, 10)); // Should return products with prices reduced by 10%
console.log(findProductById(sampleProducts, 3)); // Should return the product with id 3
