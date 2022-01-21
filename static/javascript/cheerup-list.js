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

function editCheerup(event) {
    let cheerup = event.target.parentNode.parentNode.childNodes[3].children[0];
    let edit = event.target.parentNode.parentNode.childNodes[3].children[1];
    console.log(cheerup.style.display)

    if (cheerup.style.display != 'none') {
        cheerup.style.display = 'none';
        edit.style.display = 'flex'
        event.target.innerText = 'Cancel Edit' 
    } else {
        edit.style.display = 'none';
        event.target.innerText = 'Edit' 
        cheerup.style.display = 'block';
    }
}

let moreDetailsButtons = document.getElementsByClassName('find-out-more');
for (buttons of moreDetailsButtons) {
    buttons.addEventListener('click', moreDetails);
}

let editButtons = document.getElementsByClassName('edit-button');
for (button of editButtons) {
    button.addEventListener('click', editCheerup);
}
