// Function to toggle Navigation bar on/off for small screen devices
function navBarToggle() {
    var x = document.getElementById("nav_links");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
        }
    }


// Function to hide hero image & display search results upon a search
const searchClick = document.getElementById("search_btn");
searchClick.addEventListener("click", hideImgShowResults);

function hideImgShowResults() {
    document.getElementById("hero_image").style.display = "none";
    document.getElementById("search_result").style.display = "inline-block";
}