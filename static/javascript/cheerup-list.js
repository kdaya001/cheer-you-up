const cheerups_list = document.getElementsByClassName('cheerup');

function moreDetails(event) {
    let userDetails = "";
    userDetails = event.target.parentElement.children[1]

    console.log(event.target.parentElement.children.length)
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
