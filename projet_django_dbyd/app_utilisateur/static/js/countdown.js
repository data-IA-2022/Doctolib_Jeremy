function updateCountdown() {
    var countdownElement = document.getElementById('countdown');

    // Obtenez la date actuelle en JavaScript
    var now = new Date();

    // Calculez la date du 1er du mois suivant à 00:01
    var nextMonth = now.getMonth() + 1;
    var nextYear = now.getFullYear();
    if (nextMonth === 12) {
        nextMonth = 0;
        nextYear += 1;
    }
    var nextSubmissionDate = new Date(nextYear, nextMonth, 1, 0, 1);

    // Calculez la différence entre les deux dates
    var timeUntilNextSubmission = nextSubmissionDate - now;

    // Calculez le nombre de jours, d'heures, de minutes et de secondes restants
    var days = Math.floor(timeUntilNextSubmission / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeUntilNextSubmission % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeUntilNextSubmission % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeUntilNextSubmission % (1000 * 60)) / 1000);

    // Affichez le compte à rebours dans l'élément HTML
    countdownElement.innerHTML = days + " jours, " + hours + " heures, " + minutes + " minutes, " + seconds + " secondes";

    // Mettez à jour le compte à rebours toutes les 1 seconde
    setTimeout(updateCountdown, 1000);
}

// Appeler la fonction pour la première fois
updateCountdown();
