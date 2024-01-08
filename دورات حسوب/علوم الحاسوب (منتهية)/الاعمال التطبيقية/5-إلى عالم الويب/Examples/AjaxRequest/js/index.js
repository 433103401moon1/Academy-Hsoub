
function sendAJAXReq() {
    var myRequest = new XMLHttpRequest();
    myRequest.open('GET', 'http://127.0.0.1:5500/5-%D8%A5%D9%84%D9%89%20%D8%B9%D8%A7%D9%84%D9%85%20%D8%A7%D9%84%D9%88%D9%8A%D8%A8/Examples/AjaxRequest/hsoubAjax.html');
    myRequest.onreadystatechange = function () { 
        if (myRequest.readyState === 4) {
        document.getElementById('ajax-content').innerHTML = myRequest.responseText;
        }
    };
    myRequest.send();
    document.getElementById('reveal').style.display = 'none';
}

