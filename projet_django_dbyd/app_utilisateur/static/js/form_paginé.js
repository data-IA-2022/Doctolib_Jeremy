function showNext(sectionId) {
    // Cacher toutes les sections
    const sections = document.getElementsByClassName('tabcontent');
    for (let i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }

    // Afficher la section suivante
    document.getElementById(sectionId).style.display = 'block';
}

function showPrevious(sectionId) {
    // Même logique que showNext
    showNext(sectionId);
}