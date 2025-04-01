// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id "red_header"
  const redHeader = document.getElementById('red_header');

  // Add a click event listener to the element
  redHeader.addEventListener('click', () => {
    // Select the <header> element
    const header = document.querySelector('header');

    // Add the "red" class to the <header> element
    header.classList.add('red');
  });
});
