const sqlite3 = require("sqlite3").verbose(); // متطلبات
let dbName = "test.db"
let db = new sqlite3.Database(dbName, (err) => { // الاتصال مع قاعدة البيانات
  if (err) return console.error(err.message);

  console.log("Connected to " + dbName + " SQlite database");
});

// يستخدم الامر run في كل العمليات الا عملية الاستعلام فنستعمل معها الامر all
db.run("CREATE TABLE category ( categoryID INTEGER PRIMARY KEY, name TEXT)", (err) => {
  if (err) return console.error(err.message);
  console.log("Table one created");
});

db.run('CREATE TABLE product ( productID INTEGER PRIMARY KEY, name TEXT, categoryID INTEGER, FOREIGN KEY (categoryID) REFERENCES category (categoryID))', (err) => {
    if (err) return console.error(err.message);
    console.log('Table two created');
});

db.run('INSERT INTO category (name, categoryID) VALUES' +
'("category1",1),'+
'("category2",2),'+
'("category3",3)', (err) => {
    if (err) return console.error(err.message);
    console.log('Table category inserted');
});

db.run('INSERT INTO product (name, productID, categoryID) VALUES' +
'("product1",1,1),'+
'("product2",2,3),'+
'("product3",3,3),'+
'("product3",4,3),'+'("product3",5,2)', (err) => {
    if (err) return console.error(err.message);
    console.log('Table product inserted');
});

db.all(`SELECT product.name AS product, category.name AS category FROM product
        JOIN category ON product.categoryID = category.categoryID`, (err, result) => {
  if (err) return console.error(err.message);
  console.log(result);
});

db.close((err) => {
  if (err) return console.error(err.message);
  console.log("Closed the " + dbName + " database connection");
});
