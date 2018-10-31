function openPage(pageName, elmnt, color="#f1f1f1") {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }

    // Show the specific tab content
    document.getElementById(pageName).style.display = "block";

    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();



// Get the container element
var tablinkContainer = document.getElementById("buttons");

// Get all buttons with class="tablink" inside the container
var tablink = tablinkContainer.getElementsByClassName("tablink");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < tablink.length; i++) {
  tablink[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}


function test(element) {
var newTab = window.open();
setTimeout(function(){newTab.document.body.innerHTML = element.innerHTML;
},500);

  return false;

}
