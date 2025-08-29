// Wait until the page is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // 1. Grab the form
    const form = document.querySelector(".contact-form");

    // 2. Grab the popup box
    const popup = document.querySelector(".popup");

    // 3. Grab the close button inside popup
    const closeBtn = document.querySelector(".popup button");

    // 4. Listen for form submission
    form.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent page reload

        // Show popup message
        popup.style.display = "flex";
    });

    // 5. Listen for close button click
    closeBtn.addEventListener("click", () => {
        popup.style.display = "none"; // Hide popup
    });
});