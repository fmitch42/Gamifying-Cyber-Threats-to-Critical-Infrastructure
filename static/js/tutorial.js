// Tutorial text pages
const tutorialPages = [
    `Let's start by finding the topology.

    When this page was loaded, a new window should have been opened on your desktop.
    
    Find and inspect this, then click next.`,

    `In this new window, you will find the topology for the network for the given scenario.
    
    Each component is represented by an icon labelled with its name ("e.g. PC1 for a computer, s1 for a switch)`,

    `You may also notice that a CLI (Command line interface) has been opened in the main terminal where the app is running.
    
    We will cover this in a later tutorial, so don't worry about this for now`,

    `The aim of this game is to determine what type of attack is being carried out on the network and decide what actions would best counter it.
    
    The game will be offered in 2 formats: basic and advanced. These differ in the way you interact with the network:

    - In the basic version of the game, you will be offered a few buttons and interactions to allow you to analyse the behaviour of the attack.
    
    - The advanced version offers input through a CLI and so gives you more control and allows more specific, detailed information to be gathered.`,

    `A Wiki covering each type of attack you could be faced with is provided on the home page, with some hints and tips if you get stuck!
    
    It also has a section on the actions/buttons in the game for reference.`,
    
    `Important note: Before closing each level (including this tutorial!), you must manually close the topology window to ensure that mininet closes properly,
    otherwise the app won't work properly. 
    
    You have now completed the tutorial! You may come back to this section at any time.`
];


let currentPage = 0;

// Function to update tutorial content
function updateContent() {
    document.getElementById("content-text").innerText = tutorialPages[currentPage];

    // Get button elements
    const prevBtn = document.getElementById("prev-btn");
    const nextBtn = document.getElementById("next-btn");
    const finishBtn = document.getElementById("finish-btn");

    // Disable "Previous" button if on the first page
    prevBtn.disabled = (currentPage === 0);

    // Show "Next" button only if NOT on the last page
    nextBtn.style.display = (currentPage === tutorialPages.length - 1) ? "none" : "inline-block";

    // Show "Finish" button only if on the last page
    finishBtn.style.display = (currentPage === tutorialPages.length - 1) ? "inline-block" : "none";
}

// Navigate to the previous page
function prevPage() {
    if (currentPage > 0) {
        currentPage--;
        updateContent();
    }
}

// Navigate to the next page
function nextPage() {
    if (currentPage < tutorialPages.length - 1) {
        currentPage++;
        updateContent();
    }
}

// Handle finish button click
function finishTutorial() {
    window.location.href = "/"; 
}

// Initialize content on page load
document.addEventListener("DOMContentLoaded", updateContent);
