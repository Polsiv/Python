document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });
    if (response.ok) {
        const data = await response.json();
        const myHeaders = new Headers();
        // Store the JWT in local storage
        localStorage.setItem('jwt', data.access_token);
        token = localStorage.getItem("jwt");
        myHeaders.set('Content-Type', 'application/json');
        myHeaders.set('Authorization', `Bearer ${token}`);
        // Redirect to the numbers route
        window.location.href = '/numbers/';
    } else {
        alert('Login failed!');
    }
});

// get JWT token from local storage
function getJWTToken() {
    return localStorage.getItem('jwt');
}

// make authenticated requests to protected routes
async function fetchProtectedRoute(url) {
    const token = localStorage.getItem('jwt');
    if (!token) {
        console.error('JWT token not found in local storage');
        return;
    }

    try {
        console.log('Token:', token);
        console.log('URL:', url);
        
        const response = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${token}`,
            }
        });

        if (response.ok) {
            const data = await response.json();
            console.log(data); // Handle response data accordingly
        } else {
            console.error('Failed to fetch protected route:', response.status, response.statusText);
        }
    } catch (error) {
        console.error('Error fetching protected route:', error);
    }
}