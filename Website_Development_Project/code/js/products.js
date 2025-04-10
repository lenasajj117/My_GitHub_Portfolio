document.addEventListener('DOMContentLoaded', () => {
    displayProduct(currentProductIndex); // Ensures the first product displays only after DOM loads
    updateCartCount(); // Updates cart count on page load
});

// Product data
const products = [
    {
        name: "Tech iRobot",
        description: "Elegant, innovative design crafted for the discerning modern user.",
        price: "$299",
        image: "images/tech-irobot 2.webp"
    },
    {
        name: "Future eBike",
        description: "Luxury meets performance in this exquisite piece.",
        price: "$899",
        image: "images/future-ebike.webp"
    },
    {
        name: "Smart Helmet",
        description: "Crafted for those who value sophistication and technology.",
        price: "$699",
        image: "images/smart-helmet.jpg"
    },
    {
        name: "Stellar Hoverboard",
        description: "Merging high-performance technology with sleek, contemporary aesthetics.",
        price: "$359",
        image: "images/stellar hoverboard.jpeg"
    },
    {
        name: "Spark of Music",
        description: "Designed for the modern connoisseur who appreciates elegance and cutting-edge technology.",
        price: "$299",
        image: "images/bose headphones.jpg"
    },
    {
        name: "Realtime Generative AI",
        description: "For the discerning user who seeks both functionality and refined design.",
        price: "$679",
        image: "images/amazon ai.jpg"
    },
    {
        name: "Future Backpack",
        description: "For the connoisseur who desires seamless functionality paired with refined design.",
        price: "$779",
        image: "images/backpack.jpg"
    },
    {
        name: "Descent Eclipse-Wear",
        description: "Tailored for those who demand both performance and a touch of luxury in design.",
        price: "$779",
        image: "images/eclipse wear.jpg"
    }
];

let currentProductIndex = 0;

// Function to display a product
function displayProduct(index) {
    const product = products[index];
    document.getElementById("product-image").src = product.image;
    document.getElementById("product-name").innerText = product.name;
    document.getElementById("product-description").innerText = product.description;
    document.getElementById("product-price").innerText = product.price;

    // Add the event listener only if the button exists and only once
    const addToCartBtn = document.getElementById("add-to-cart-btn");
    if (addToCartBtn && !addToCartBtn.hasListener) {
        addToCartBtn.addEventListener("click", addToCart);
        addToCartBtn.hasListener = true;
    }

    // Fade-in effect
    const displayElement = document.querySelector('.product-display');
    displayElement.classList.remove('fade-in');
    setTimeout(() => displayElement.classList.add('fade-in'), 10);
}

// Function to navigate to the next product
function nextProduct() {
    currentProductIndex = (currentProductIndex + 1) % products.length;
    displayProduct(currentProductIndex);
}

// Function to navigate to the previous product
function previousProduct() {
    currentProductIndex = (currentProductIndex - 1 + products.length) % products.length;
    displayProduct(currentProductIndex);
}

// Update cart count from localStorage
function updateCartCount() {
    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const cartCount = cartItems.reduce((count, item) => count + item.quantity, 0);
    document.getElementById("cart-count").innerText = cartCount;
}

// Function to add the current product to the cart
function addToCart() {
    const currentProduct = products[currentProductIndex];
    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const existingItem = cartItems.find(item => item.name === currentProduct.name);

    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cartItems.push({
            name: currentProduct.name,
            price: currentProduct.price,
            image: currentProduct.image,
            quantity: 1
        });
    }

    localStorage.setItem('cartItems', JSON.stringify(cartItems));
    alert(`${currentProduct.name} added to cart!`);
    updateCartCount();
}

// Initial display of the first product
displayProduct(currentProductIndex);
updateCartCount();
