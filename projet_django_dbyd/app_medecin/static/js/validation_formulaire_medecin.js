        // Afficher la fenêtre modale
        function showModal() {
            document.getElementById('confirmationModal').style.display = 'block';
        }
    
        // Cacher la fenêtre modale
        function closeModal() {
            document.getElementById('confirmationModal').style.display = 'none';
        }
    
        // Quand l'utilisateur clique sur (x), fermer la fenêtre modale
        var closeBtn = document.getElementsByClassName("close")[0];
        closeBtn.onclick = function() {
            closeModal();
        }
    
        // Quand l'utilisateur clique sur "Annuler", fermer la fenêtre modale et ne rien faire
        var cancelBtn = document.getElementById("cancelSubmit");
        cancelBtn.onclick = function() {
            closeModal();
        }
    
        // Quand l'utilisateur clique sur "Confirmer", soumettre le formulaire
        var confirmBtn = document.getElementById("confirmSubmit");
        confirmBtn.onclick = function() {
            document.querySelector('form').submit();
        }
    
        // Quand l'utilisateur clique n'importe où en dehors de la fenêtre modale, la fermer
        window.onclick = function(event) {
            var modal = document.getElementById('confirmationModal');
            if (event.target == modal) {
                closeModal();
            }
        }