document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const predefinedUsername = 'admin ceat';
    const predefinedPassword = 'admin@123';
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('errorMessage');
    
    if (username === predefinedUsername && password === predefinedPassword) {
        alert('Login successful!');
        // Redirect to another page or perform another action here
        window.location.href = "/dashboard"; // Example redirection
    } else {
        errorMessage.classList.remove('d-none');
        errorMessage.textContent = 'Invalid username or password.';
    }
});
