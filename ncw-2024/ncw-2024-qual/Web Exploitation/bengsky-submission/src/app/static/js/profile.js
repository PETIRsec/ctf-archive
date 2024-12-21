export function updateProfile() {
    try {
        document.getElementById('profile-pic-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const profilePicURL = document.getElementById('profile_pic').value;
        
            const response = await fetch('/profile', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ profile_pic: profilePicURL })
            });
        
            if (response.ok) {
                alert('Profile picture updated successfully!');
                location.reload(); 
            } else {
                const errorMessage = await response.text();
                alert(`Error: ${errorMessage}`);
            }
        });
    } catch (error) {
        console.error('Error:', error.message);
    }
  }