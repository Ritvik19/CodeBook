document.getElementById("code").innerHTML = "Get your code served here"
document.getElementById("code-btn").disabled = true;
var clipboard = new ClipboardJS('.copy-button');

function snackbarDisplay()
{
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

function loadCode()
{
  var xhttp = new XMLHttpRequest();
  var filepath = '../programs/'+document.getElementById('problem').value+'.py'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("code").innerHTML = this.responseText;
     document.getElementById("code-btn").disabled = false;
    }
    else{
      document.getElementById("code").innerHTML = 'Ingredients for this recepie are not on the shelf';
      document.getElementById("code-btn").disabled = true;
    }
  };
  xhttp.open("GET", filepath, true);
  xhttp.send();
}

function loadDoc(){
  window.open('../programs/'+document.getElementById('problem').value+'.py')
}
