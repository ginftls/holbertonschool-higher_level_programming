document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id "update_header"
  const updateHeaderButton = document.getElementById('update_header');

  // Add a click event listener to the element
  updateHeaderButton.addEventListener('click', () => {
    // Select the <header> element
    const header = document.querySelector('header');

    // Update the text content of the <header> element
    header.textContent = 'New Header!!!';
  });
});
