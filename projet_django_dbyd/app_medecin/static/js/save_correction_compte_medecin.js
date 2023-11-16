var countdownElement = document.getElementById('countdown');
var countdown = 5; // Compte à rebours initialisé à 5 secondes

var intervalId = setInterval(function() {
    countdown -= 1;
    countdownElement.textContent = countdown; // Mettre à jour le texte du compte à rebours
    
    if (countdown <= 0) {
        clearInterval(intervalId); // Arrête le compte à rebours
        window.location.href = "http://127.0.0.1:8000/medecin/compte_medecin"; // Redirection
    }
}, 1000); // Exécuter le code toutes les secondes