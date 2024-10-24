document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll('.action-button');
    buttons.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.boxShadow = "0 10px 20px rgba(0, 0, 0, 0.3)";
        });
        button.addEventListener('mouseout', () => {
            button.style.boxShadow = "none";
        });
    });
});
