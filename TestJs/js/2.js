function myFunction() {
    var x;
    x = document.getElementById("demo");
    if (x.innerHTML.match("source")) {
        x.innerHTML = "change code";
    }
    else {
        x.innerHTML = "source code"
    }
}