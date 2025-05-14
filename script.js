document.addEventListener('DOMContentLoaded', function() {
    // Garante que sempre tem um card expandido
    let currentExpanded = document.querySelector('.card.expanded');
    if (!currentExpanded) {
        currentExpanded = document.querySelector('.card');
        if (currentExpanded) {
            currentExpanded.classList.add('expanded');
        }
    }

    const allCards = document.querySelectorAll('.card');
    allCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            if (card !== currentExpanded) {
                currentExpanded.classList.remove('expanded');
                card.classList.add('expanded');
                currentExpanded = card;
            }
        });
    });
});
