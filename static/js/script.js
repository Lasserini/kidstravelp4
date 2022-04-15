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
let topButton = document.querySelector(".top_button");
topButton.onclick = () => window.scrollTo({ top: 0, behavior: "smooth" });

// Functionality for Results page, Scroll to Bottom button
let bottomButton = document.querySelector(".bottom_button");
bottomButton.onclick = () => window.scrollTo({ top: 10000, behavior: "smooth" });

// Functions that produce a confirmation box before any deleting is done
function deleteConfirm(){
    var deleteButton= document.getElementById("delete_review");
    if (confirm("Confirm Review Deletion")){
        deleteButton.click();
        alert("Review Deleted!");
    }
}

function deleteConfirmTwo(){
    var deleteButton= document.getElementById("delete_experience");
    if (confirm("Careful! Confirm Experience Deletion??")){
        deleteButton.click();
        alert("Experience Deleted!");
    }
}