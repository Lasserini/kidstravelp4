// Function to toggle Navigation bar on/off for small screen devices
function navBarToggle() {
    var x = document.getElementById("nav_links");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
        }
    }

// Functions that produce a confirmation box before any deletion is done
// Delete Experience
const modal = document.getElementById("deleteExpModal");

let ExpDeleteCheck = document.querySelector("#ExpModalBtn");
if (ExpDeleteCheck) {
    ExpDeleteCheck.onclick = () => {
        modal.style.display = "block";
    }
}

// Delete Reviews
const modal2 = document.getElementById("deleteReviewModal");

let ReviewDeleteCheck = document.querySelectorAll("#ReviewModalBtn");
for(var i=0; i<ReviewDeleteCheck.length; i++){
    ReviewDeleteCheck[i].onclick = () => {
        modal2.style.display = "block";
    }
}

// Closing the modals functionality
let closeModal = document.querySelector(".close");
if (closeModal) {
    closeModal.onclick = () => {
        modal.style.display = "none";
    }
}

let closeModal2 = document.querySelector(".close2");
if (closeModal2) {
    closeModal2.onclick = () => {
        modal2.style.display = "none";
    }
}

window.onclick = (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
    else if (event.target == modal2) {
        modal2.style.display = "none";
      }
}