const cheerups = document.getElementsByClassName('cheerup');

function moreDetails(event) {
    const userDetails = event.target.parentElement.children[2];
    let currentState = userDetails.style.display
    if (currentState == "block") {
        userDetails.style.display = "none"
    } else {
        userDetails.style.display = "block"
    }
}

const moreDetailsButtons = document.getElementsByClassName('find-out-more');
for (buttons of moreDetailsButtons) {
    buttons.addEventListener('click', moreDetails);
}
