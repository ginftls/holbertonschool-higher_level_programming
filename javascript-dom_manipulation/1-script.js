// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
  // Select the element with id "red_header"
  const redHeader = document.getElementById('red_header');

  // Add a click event listener to the element
  redHeader.addEventListener('click', () => {
    // Select the <header> element
    const header = document.querySelector('header');

    // Change the text color of the <header> element to red (#FF0000)
    header.style.color = '#FF0000';
  });
});
