// Function to toggle Navigation bar on/off for small screen devices
function navBarToggle() {
    var x = document.getElementById("nav_links");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
        }
    }

// Functionality for Results page, Scroll to Top button
// let topButton = document.querySelector(".top_button");
// topButton.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });

// Functionality for Results page, Scroll to Bottom button
// let bottomButton = document.querySelector(".bottom_button");
// bottomButton.onclick = () => window.scrollTo({ top: 10000, behavior: "smooth" });

// Functions that produce a confirmation box before any deletion is done
var modal = document.getElementById("deleteExpModal");
var modal2 = document.getElementById("deleteReviewModal");
var btn = document.getElementById("ExpModalBtn");
var btn2 = document.getElementById("ReviewModalBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

btn2.onclick = function() {
    modal2.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
}