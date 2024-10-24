
    <script>
        const redirectUrl = "{{ url_for('view_all') }}";
    </script>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();

            const predefinedUsername = 'admin ceat';
            const predefinedPasswords = ['admin@123', 'admin@456', 'admin@789'];

            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            const errorMessage = document.getElementById('errorMessage');

            if (username === predefinedUsername && predefinedPasswords.includes(password)) {
                alert('Login successful!');
                // Redirect to another page or perform another action here
                window.location.href = redirectUrl; // Use the rendered URL
            } else {
                errorMessage.classList.remove('d-none');
                errorMessage.textContent = 'Invalid username or password.';
            }
        });
    </script>
