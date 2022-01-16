const cheerups = document.getElementsByClassName('cheerup');

function moreDetails(event) {
    const userDetails = event.target.parentElement.children[3];
    console.log(userDetails)
    let currentState = userDetails.style.display
    if (currentState == "flex") {
        userDetails.style.display = "none"
    } else {
        userDetails.style.display = "flex"
    }
}

const moreDetailsButtons = document.getElementsByClassName('find-out-more');
for (buttons of moreDetailsButtons) {
    buttons.addEventListener('click', moreDetails);
}
