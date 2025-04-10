// Refined Cart Management Script
let cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];

const cartContainer = document.querySelector('.cart-items');
const totalPriceElement = document.getElementById('total-price');
const checkoutBtn = document.querySelector('.checkout-btn');

// Function to render cart items in the HTML
function renderCart() {
    cartContainer.innerHTML = ''; // Clear previous items
    let total = 0;

    // Check if there are items in the cart
    if (cartItems.length === 0) {
        cartContainer.innerHTML = `<p class="empty-cart">Your cart is empty.</p>`;
        totalPriceElement.textContent = `$0.00`;
        return;
    }

    // Render each item in the cart
    cartItems.forEach((item, index) => {
        // Convert item.price to a valid number
        let itemPrice = parseFloat(item.price);
        
        // Validate itemPrice
        if (isNaN(itemPrice) || typeof itemPrice !== 'number') {
            console.error(`Invalid price for item: ${item.name}`);
            itemPrice = 0; // Set to 0 if invalid
        }

        // Update total
        total += itemPrice * item.quantity;

        // Create cart item element
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}" class="cart-item-image">
            <div class="cart-item-details">
                <h3>${item.name}</h3>
                <p>Price: $${itemPrice.toFixed(2)}</p>
                <label>Quantity:</label>
                <input type="number" value="${item.quantity}" min="1" data-index="${index}" class="quantity">
                <button class="remove-btn" data-index="${index}">Remove</button>
            </div>
        `;
        cartContainer.appendChild(cartItem);
    });

    // Update total price display
    totalPriceElement.textContent = `$${total.toFixed(2)}`;
}

// Handle quantity updates
cartContainer.addEventListener('input', (e) => {
    if (e.target.classList.contains('quantity')) {
        const index = e.target.getAttribute('data-index');
        cartItems[index].quantity = parseInt(e.target.value);
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        renderCart();
    }
});

// Handle item removal
cartContainer.addEventListener('click', (e) => {
    if (e.target.classList.contains('remove-btn')) {
        const index = e.target.getAttribute('data-index');
        cartItems.splice(index, 1); // Remove item from the cart
        localStorage.setItem('cartItems', JSON.stringify(cartItems));
        renderCart();
    }
});

// Handle checkout button click
if (checkoutBtn) {
    checkoutBtn.addEventListener('click', function () {
        if (cartItems.length > 0) {
            window.location.href = 'checkout.html';
        } else {
            alert("Your cart is empty! Add items before checking out.");
        }
    });
}

// Initial render
renderCart();
