document.getElementById("code").innerHTML = "Get your code served here"
document.getElementById("code-btn").disabled = true;
var clipboard = new ClipboardJS('.copy-button');

function snackbarDisplay()
{
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}


function loadCode()
{
  var xhttp = new XMLHttpRequest();
  filename = document.getElementById('problem').value
  var filepath = '../programs/'+filename+'.py'
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     document.getElementById("code").innerHTML = this.responseText;
     document.getElementById("prob-link").setAttribute('href', 'https://www.codechef.com/problems/'+filename)
     document.getElementById("code-btn").disabled = false;
     document.getElementById("prob-btn").disabled = false;
    }
    else{
      document.getElementById("code").innerHTML = 'Ingredients for this recepie are not on the shelf';
      document.getElementById("prob-link").setAttribute('href', '#')
      document.getElementById("code-btn").disabled = true;
      document.getElementById("prob-btn").disabled = true;
    }
  };
  xhttp.open("GET", filepath, true);
  xhttp.send();
}

function loadDoc(){
  window.open('../programs/'+document.getElementById('problem').value+'.py')
}
