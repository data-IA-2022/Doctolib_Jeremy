// Lorsque l'utilisateur clique sur l'icône d'œil...
document.querySelector(".toggle-password").addEventListener('click', function (e) {
    // on récupère le champ de mot de passe
    var passwordField = document.querySelector('#password');
    
    // Si le mot de passe est caché, l'afficher
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        this.classList.toggle('fa-eye-slash');
    } else { // Sinon, le cacher
        passwordField.type = 'password';
        this.classList.toggle('fa-eye-slash');
    }
    });