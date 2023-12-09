// Sample data (can be retrieved from an API or server)
const catalogItems = [
    { name: 'Item 1', price: 10 },
    { name: 'Item 2', price: 20 },
    { name: 'Item 3', price: 15 },
    // Add more items as needed...
];

// Function to render items dynamically
function renderItems() {
    const itemsContainer = document.getElementById('items-container');

    catalogItems.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('item');
        itemElement.innerHTML = `
            <h3>${item.name}</h3>
            <p>Price: $${item.price}</p>
        `;
        itemsContainer.appendChild(itemElement);
    });
}

// Render items when the page loads
window.onload = function() {
    renderItems();
};
