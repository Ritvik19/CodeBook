document.getElementById("code").innerHTML = "Get your code here"
document.getElementById("code-btn").disabled = true;
var clipboard = new ClipboardJS('.copy-button');

function snackbarDisplay()
{
  var x = document.getElementById("snackbar");
  x.className = "show";
  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

function loadPrograms() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var dataObj = JSON.parse(this.responseText);
      program_name = dataObj['Program']
      platform = dataObj['Category']
      extension = dataObj['Language']
      var i =0;
      HTMLcontent = ''
      while(typeof program_name[i] !== "undefined")
      {
        // loadCode(\''+platform[i]+'\', \''+program_name[i]+'\', \''+extension[i]+'\')
        HTMLcontent += '<li class="w3-padding-8 program" onclick="loadCode(\''+platform[i]+'\', \''+program_name[i]+'\', \''+extension[i]+'\')"><span class="w3-large">'+program_name[i]+'</span><br><span>'+platform[i]+'</span></li>'
        i ++;
      }
      document.getElementById("postlist").innerHTML += HTMLcontent;
    }
  };
  xhttp.open("GET", "data/ProgramList.json", true);
  xhttp.send();
}

function listFilter(inputEl, listEl, element) {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById(inputEl);
    filter = input.value.toUpperCase();
    ul = document.getElementById(listEl);
    li = ul.getElementsByTagName("li");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName(element)[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function loadCode(p, q, e)
{
  var xhttp = new XMLHttpRequest();
  var filepath = '../data/'+p+'/'+q+'.'+e
  console.log(filepath)
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
     code = this.responseText;
     code = code.replace(/</g,"&lt;")
     code = code.replace(/>/g,"&gt;")
     document.getElementById("code").innerHTML = code;
     document.getElementById("code-btn").disabled = false;
     // document.getElementById("prob-btn").disabled = false;
    }
    else{
      document.getElementById("code").innerHTML = 'Get your code here';
      document.getElementById("code-btn").disabled = true;
      // document.getElementById("prob-btn").disabled = true;
    }
  };
  xhttp.open("GET", filepath, true);
  xhttp.send();
}

function loadDoc(p, q, e){
  window.open('../data/'+p+'/'+q+'.'+e)
}

loadPrograms();
