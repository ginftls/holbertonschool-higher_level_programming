document.addEventListener('DOMContentLoaded', () => {
  // Define the URL to fetch the movie data
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

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
      // Extract the array of movies from the data
      const movies = data.results;

      // Select the <ul> element with id "list_movies"
      const listMovies = document.getElementById('list_movies');

      // Loop through the movies and create <li> elements for each title
      movies.forEach((movie) => {
        // Create a new <li> element
        const listItem = document.createElement('li');

        // Set the text content of the <li> element to the movie's title
        listItem.textContent = movie.title;

        // Append the <li> element to the <ul> element
        listMovies.appendChild(listItem);
      });
    })
    .catch((error) => {
      // Handle any errors that occur during the fetch
      console.error('Error fetching movie data:', error);

      // Optionally, display an error message in the <ul>
      const listMovies = document.getElementById('list_movies');
      const errorMessage = document.createElement('li');
      errorMessage.textContent = 'Failed to load movie data';
      listMovies.appendChild(errorMessage);
    });
});
