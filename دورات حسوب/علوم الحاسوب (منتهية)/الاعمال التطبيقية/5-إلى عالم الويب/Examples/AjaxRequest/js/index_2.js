$(document).ready(function(){
  $(document).ajaxStart(function(){
    $("#wait").css("display", "block");
  });
  $(document).ajaxComplete(function(){
    $("#wait").css("display", "none");
  });
  $("button").click(function(){
    $("#ajax-content").load("http://127.0.0.1:5500/5-%D8%A5%D9%84%D9%89%20%D8%B9%D8%A7%D9%84%D9%85%20%D8%A7%D9%84%D9%88%D9%8A%D8%A8/Examples/AjaxRequest/hsoubAjax.html");
  });
});
