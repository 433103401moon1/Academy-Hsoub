import "../node_modules/@fortawesome/fontawesome-free/js/all.min.js";
import "../node_modules/bootstrap/dist/js/bootstrap.min.js";
import "../node_modules/bootstrap/dist/css/bootstrap.rtl.min.css";
import "./main.css";
import "./sass/main.scss";

const menuItems = document.querySelectorAll("header a.nav-link");
menuItems.forEach((item) => {
  item.addEventListener("click", () => {
    menuItems.forEach((el) => el.classList.remove("active"));

    item.classList.add("active");
  });
});

document.querySelectorAll(".add-to-cart-btn").forEach((item) => {
  item.addEventListener("click", () => {
    alert("تم الإضافة إلى العربة!");
  });
});

document.getElementById("copyright").innerHTML = "جميع الحقوق محفوظة للمتجر سنة " + new Date().getFullYear();

document.querySelectorAll('.size-option input[type="radio"]').forEach(item => {
    item.addEventListener('change', () => {
        document.querySelectorAll('.size-option').forEach(i => {
            i.classList.remove('active')
        })
        item.parentNode.parentNode.classList.add('active')
    })
})

document.querySelectorAll('.color-option input[type="radio"]').forEach(item => {
    item.addEventListener('change', () => {
        document.querySelectorAll('.color-option').forEach(i => {
            i.classList.remove('active')
        })
        item.parentNode.parentNode.classList.add('active')
    })
})