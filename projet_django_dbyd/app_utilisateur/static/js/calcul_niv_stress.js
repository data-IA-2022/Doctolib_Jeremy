function calculerScore() {
    var score = 0;
    var selects = document.querySelectorAll('select');
    for (var i = 0; i < selects.length; i++) {
        if (selects[i].value) {
            score += parseInt(selects[i].value, 10);
        }
    }

    var maxScore = 43 * 10; // 43 questions x 10 points max
    var pourcentage = (score / maxScore) * 100;

    var scoreElement = document.getElementById('scoreTotal');
    if (scoreElement) {
        scoreElement.textContent = 'Le stress a-t-il un impact significatif sur votre vie ? ' + pourcentage.toFixed(2) + '%';
        updateScoreColor(scoreElement, pourcentage);
    }

    var impactStressField = document.getElementById('impact_stress');
    if (impactStressField) {
        impactStressField.value = score; // Mettre à jour le score total
    }
}

function updateScoreColor(element, pourcentage) {
    if (pourcentage <= 33) {
        element.style.color = 'green';
    } else if (pourcentage <= 66) {
        element.style.color = 'orange';
    } else {
        element.style.color = 'red';
    }
}

window.onload = function() {
    var selects = document.querySelectorAll('select');
    for (var i = 0; i < selects.length; i++) {
        selects[i].addEventListener('change', calculerScore);
    }
    calculerScore(); // Calcul initial du score
};