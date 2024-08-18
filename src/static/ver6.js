const form = document.querySelector('form');
const searchInput = document.querySelector('#search');
const resultsDiv = document.querySelector('#results');

form.addEventListener('submit', function(event) {
	event.preventDefault();

	const searchTerm = searchInput.value;

	fetch(`https://itunes.apple.com/search?term=${searchTerm}&entity=song&limit=10`)
		.then(response => response.json())
		.then(data => {
			resultsDiv.innerHTML = '';
			data.results.forEach(result => {
				const resultDiv = document.createElement('div');
				resultDiv.classList.add('result');

				const image = document.createElement('img');
				image.src = result.artworkUrl100;
				resultDiv.appendChild(image);

				const title = document.createElement('h3');
				title.textContent = result.trackName;
				resultDiv.appendChild(title);

				const artist = document.createElement('p');
				artist.textContent = result.artistName;
				resultDiv.appendChild(artist);

				const audio = document.createElement('audio');
				audio.controls = true;
				audio.src = result.previewUrl;
				resultDiv.appendChild(audio);

				resultsDiv.appendChild(resultDiv);
			});
		})
		.catch(error => console.log(error));
});
