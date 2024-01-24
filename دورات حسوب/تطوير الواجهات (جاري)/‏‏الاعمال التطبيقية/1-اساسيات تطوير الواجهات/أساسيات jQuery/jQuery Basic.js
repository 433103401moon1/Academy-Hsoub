// // document.write("الطريقة2 لوضع جافاسكربت في الصفحة");
function print_person_category(){
    let age = document.getElementById("age").value;
    // document.write("your age is :" + age);
    // console.log("your age is :" + age);
    document.getElementById("result").innerHTML = "Your age is :" + age;
}
// // احضار العنصر باستخدام المعرف
// document.getElementById("age");
// // احضار العنصر باستخدام اسم العنصر في HTML
// let p = document.getElementsByTagName("p");
// document.write(p[0]);
// // احضار العنصر باستخدام الكلاس للعنصر في HTML
// document.getElementsByClassName("class");

// let age = document.getElementById("age").value;

// انشاء عنصر جديد في HTML
let x = document.createElement("p");
// اضافة كود HTML على احد العنصر + يمكن اضافة التنسيقات وغيرها تماما كما تكتب كود HTML
let value_x = x.innerHTML = '<b style="color:green;">this is x </b>' + '<b style="color:green;">1</b>';
// اضافة عتصر الى عنصر اخر مثل div
let div = document.getElementById("div");
div.appendChild(x);
document.write(value_x);
