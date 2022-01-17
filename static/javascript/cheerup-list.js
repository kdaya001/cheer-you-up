const cheerups_list = document.getElementsByClassName('cheerup');

function moreDetails(event) {
    const userDetails = event.target.parentElement.children[3];
    let currentState = userDetails.style.display
    if (currentState == "flex") {
        userDetails.style.display = "none"
    } else {
        userDetails.style.display = "flex"
    }
}

let moreDetailsButtons = document.getElementsByClassName('find-out-more');
for (buttons of moreDetailsButtons) {
    buttons.addEventListener('click', moreDetails);
}
