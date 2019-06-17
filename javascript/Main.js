document.getElementById("code").innerHTML = "Your code appears here"

var clipboard = new ClipboardJS('.copy-button');

function snackbarDisplay() {
  // Get the snackbar DIV
  var x = document.getElementById("snackbar");

  // Add the "show" class to DIV
  x.className = "show";

  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

// function clearCode(){
//   document.getElementById('code').innerHTML = '';
// }

function loadCode(){
  var xhttp = new XMLHttpRequest();
  var filepath = '../programs/'+document.getElementById('problem').value+'.py'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("code").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", filepath, true);
  xhttp.send();
}

function loadDoc(){
  window.open('../programs/'+document.getElementById('problem').value+'.py')
}
