// Get the element that contains the text to be typed
const textElement = document.querySelector('.para');

// Set the initial text content to an empty string
let text = '';

// Define the text that needs to be typed
const targetText = "We are a team of music enthusiasts who love sharing our passion for music with the world. Our mission is to bring you the best music from around the globe and provide a platform for up-and-coming artists to showcase their talents.";

// Define the typing speed (in milliseconds)
const typingSpeed = 50;

// Define a function to start typing
function startTyping() {
  let i = 0;
  const intervalId = setInterval(() => {
    text += targetText[i];
    textElement.textContent = text;
    i++;
    if (i === targetText.length) {
      clearInterval(intervalId);
    }
  }, typingSpeed);
}

// Call the startTyping function to begin the typing effect
startTyping();
