function openModel_info(evt, modelName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("modelContent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.querySelectorAll("#modelName")
  console.log(tablinks)
  for (i = 0; i < tablinks.length; i++) {
    console.log(tablinks[i].className)
    console.log(i)
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(modelName).style.display = "block";
  evt.currentTarget.className += " active";
}