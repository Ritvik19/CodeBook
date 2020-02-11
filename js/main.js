function loadPrograms() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var dataObj = JSON.parse(this.responseText);
            program_name = dataObj['Program']
            platform = dataObj['Category']
            extension = dataObj['Language']
            var i = 0;
            HTMLcontent = ''
            featuredContent = ''
            while (typeof program_name[i] !== "undefined") {
                HTMLcontent += '<a href="/terminal/?p=' + platform[i] + '&q=' + program_name[i] + '&e=' + extension[i] + '"><li class="w3-padding-8"><span class="w3-large">' + program_name[i] + '</span><br><span>' + platform[i] + '</span></li></a>'
                if (platform[i] == 'Featured') {
                    featuredContent += '<a href="/terminal/?p=' + platform[i] + '&q=' + program_name[i] + '&e=' + extension[i] + '"><li class="w3-padding-8"><span class="w3-large">' + program_name[i] + '</span><br><span>' + platform[i] + '</span></li></a>'
                }
                i++;
            }
            document.getElementById("postlist").innerHTML += HTMLcontent;
            document.getElementById("featured").innerHTML += featuredContent;
            document.getElementsByClassName("badge")[0].innerHTML = i;
        }
    };
    xhttp.open("GET", "data/ProgramList.json", true);
    xhttp.send();
}
loadPrograms();


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