document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id "add_item"
  const addItemButton = document.getElementById('add_item');

  // Add a click event listener to the element
  addItemButton.addEventListener('click', () => {
    // Create a new <li> element
    const newListItem = document.createElement('li');

    // Set the text content of the new <li> element
    newListItem.textContent = 'Item';

    // Select the <ul> element with class "my_list"
    const list = document.querySelector('.my_list');

    // Append the new <li> element to the <ul> element
    list.appendChild(newListItem);
  });
});