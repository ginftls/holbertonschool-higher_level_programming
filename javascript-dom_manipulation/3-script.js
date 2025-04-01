// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id "toggle_header"
  const toggleHeader = document.getElementById('toggle_header');

  // Add a click event listener to the element
  toggleHeader.addEventListener('click', () => {
    // Select the <header> element
    const header = document.querySelector('header');

    // Check if the current class is "red" or "green"
    if (header.classList.contains('red')) {
      // If the class is "red", switch to "green"
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      // If the class is "green", switch to "red"
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});
