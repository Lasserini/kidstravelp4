// Function to toggle Navigation bar on/off for small screen devices
function navBarToggle() {
    var x = document.getElementById("nav_links");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
        }
    }

// Functionality for Results page Scroll Buttons
const topButton = document.getElementsByClassName("top_button");
topButton.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });

const bottomButton = document.getElementsByClassName("bottom_button");
bottomButton.onclick = () => window.scrollTo({ top: 10000, behavior: "smooth" });


// Functions that produce a confirmation box before any deletion is done
const modal = document.getElementById("deleteExpModal");
const modal2 = document.getElementById("deleteReviewModal");
const btn = document.getElementById("ExpModalBtn");
const btn2 = document.getElementById("ReviewModalBtn");
const closeModal = document.getElementsByClassName("close")[0];
const closeModal2 = document.getElementsByClassName("close2")[0];

btn.onclick = () => {
    modal.style.display = "block";
}

btn2.onclick = () => {
    modal2.style.display = "block";
}

closeModal.onclick = () => {
    modal.style.display = "none";
}

closeModal2.onclick = () => {
    modal2.style.display = "none";
}

window.onclick = (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
    else if (event.target == modal2) {
        modal2.style.display = "none";
      }
}