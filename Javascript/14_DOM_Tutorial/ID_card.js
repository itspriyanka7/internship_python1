// Student data
const student = {
  name: "Priyanka Prashant Desale",
  age: 18,
  course: "Information Technology",
  Blood_Group: "B-",
  photo: "priya.jpg" // Replace with the actual image path
};

// Card
let card = document.createElement("div");
card.style.width = "250px";
card.style.margin = "50px auto";
card.style.border = "2px solid black";
card.style.textAlign = "center";
card.style.padding = "10px";
card.style.backgroundColor= '#e8f4fd';
document.body.appendChild(card);

// Title
let title = document.createElement("h2");
title.textContent = "MET Institute of Polytechnic";
title.style.backgroundColor = "red";
title.style.color = "white";
title.style.margin = "0";
title.style.padding = "10px";
card.appendChild(title);

// Photo
let img = document.createElement("img");
img.src = student.photo;
img.style.margin = "10px 0";
img.style.height = "100px";
img.style.width = "105px"
img.style.borderRadius = '50%';
img.style.borderWidth = "200px";
card.appendChild(img);

// Name
let name = document.createElement("p");
name.textContent = "Name: " + student.name;
card.appendChild(name);

// Age
let age = document.createElement("p");
age.textContent = "Age: " + student.age;
card.appendChild(age);

// Course
let course = document.createElement("p");
course.textContent = "Course: " + student.course;
card.appendChild(course);

// ID
let Blood_Group = document.createElement("p");
Blood_Group.textContent = "Blood Group: " + student.Blood_Group;
card.appendChild(Blood_Group);

// Label
let label = document.createElement("div");
label.textContent = "STUDENT";
label.style.backgroundColor = "blue";
label.style.color = "white";
label.style.padding = "5px";
card.appendChild(label);