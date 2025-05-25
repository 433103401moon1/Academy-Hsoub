// تاريخ الهدف
const targetDate = new Date("2025-02-01T00:00:00");

// حساب الفرق بين التاريخ الحالي وتاريخ الهدف
function updateCountdown() {
  const now = new Date();
  const diff = targetDate.getTime() - now.getTime();
  
  // حساب الأشهر والأيام والساعات والدقائق والثواني
  const months = Math.floor(diff / (1000 * 60 * 60 * 24 * 30));
  const days = Math.floor(diff / (1000 * 60 * 60 * 24)) % 30;
  const hours = Math.floor(diff / (1000 * 60 * 60)) % 24;
  const minutes = Math.floor(diff / (1000 * 60)) % 60;
  const seconds = Math.floor(diff / 1000) % 60;

  // تحديث قيم العناصر في HTML
  document.getElementById("months").textContent = months;
  document.getElementById("days").textContent = days;
  document.getElementById("hours").textContent = hours;
  document.getElementById("minutes").textContent = minutes;
  document.getElementById("seconds").textContent = seconds;
}

// حفظ تاريخ البدء في localStorage
if (!localStorage.getItem("countdownStartDate")) {
  localStorage.setItem("countdownStartDate", new Date().getTime());
}

// حساب الفرق بين تاريخ البدء وتاريخ الهدف
const startDate = new Date(parseInt(localStorage.getItem("countdownStartDate")));
const initialDiff = targetDate.getTime() - startDate.getTime();

// تحديث العداد كل ثانية
setInterval(updateCountdown, 1000);

// تحديث العداد عند تحميل الصفحة
updateCountdown();

(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()