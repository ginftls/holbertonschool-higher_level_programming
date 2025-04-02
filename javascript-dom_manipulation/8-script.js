document.addEventListener('DOMContentLoaded', () => {
  // Define the URL to fetch the translation
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Use the Fetch API to retrieve the data
  fetch(url)
    .then((response) => {
      // Check if the response is successful
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json(); // Parse the JSON response
    })
    .then((data) => {
      // Extract the "hello" value from the data
      const helloTranslation = data.hello;

      // Select the <div> element with id "hello"
      const helloDiv = document.getElementById('hello');

      // Update the text content of the <div> with the translation
      helloDiv.textContent = helloTranslation;
    })
    .catch((error) => {
      // Handle any errors that occur during the fetch
      console.error('Error fetching translation:', error);

      // Optionally, display an error message in the <div>
      const helloDiv = document.getElementById('hello');
      helloDiv.textContent = 'Failed to load translation';
    });
});
