const cheerups_list = document.getElementsByClassName('cheerup');

function moreDetails(event) {
    let userDetails = "";

    console.log(event)

    // if(event.target.parentElement.children.length > 4) {
    //     userDetails = event.target.parentElement.children[5];
    // }
    // else {
    //     userDetails = event.target.parentElement.children[3];
    // }

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
