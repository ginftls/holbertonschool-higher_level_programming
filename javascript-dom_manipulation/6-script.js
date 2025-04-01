// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', () => {
  // Define the URL to fetch the character data
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

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
      // Extract the character's name from the data
      const characterName = data.name;

      // Select the <div> element with id "character"
      const characterDiv = document.getElementById('character');

      // Update the text content of the <div> with the character's name
      characterDiv.textContent = characterName;
    })
    .catch((error) => {
      // Handle any errors that occur during the fetch
      console.error('Error fetching character data:', error);

      // Optionally, display an error message in the <div>
      const characterDiv = document.getElementById('character');
      characterDiv.textContent = 'Failed to load character data';
    });
});
