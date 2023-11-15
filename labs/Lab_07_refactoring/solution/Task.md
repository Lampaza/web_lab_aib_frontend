# Лабораторная работа №7.

В данной лабораторной работе рефакторить код написанный на javascript

### Задание 1. level stone

```js
let firstVariable = prompt('var one');
let secondVariable= prompt('var two');
if (firstVariable === secondVariable) 
    console.log('equally')
else 
    console.log('not equally');
let stringVariable = 'world'; 
firstVariable += stringVariable;
```

### Задание №2. level iron

```js
const fruitsArray = [
    'apple',
    'strawberry',
    'blueberry',
    'raspberry',
    'lemon'
];
console.log(fruitsArray);
for (let index = 0; index < fruitsArray.length; index++) {
    if (fruitsArray[index] === 'apple') console.log('apple green');
    if (fruitsArray[index] === 'strawberry') console.log('strawberry red');
    if (fruitsArray[index] === 'blueberry') console.log('blueberry blue');
    if (fruitsArray[index] === 'raspberry') console.log('raspberry light red');
    if (fruitsArray[index] === 'lemon') console.log('lemon yellow');
}
```

### Задание 3. level gold

```js
let countPeople = 0;
let salary = 0;
while (countPeople === 0) {
    let inputCount = prompt('Введите кол-во человек:', undefined);
    countPeople = parseFloat(inputCount);
}
while (salary === 0) {
    let inputSalary = prompt('Введите зарплату на человека:', undefined);
    salary = parseFloat(inputSalary);
}
let totalCost = countPeople * salary;
console.log('Затраты: ' + totalCost);
```

### Задание 4.

```js
const classroom = [
    {fullName:'Петров А.А.', assessment:5},
    {fullName:'Иванов Б.Б.', assessment:3.4},
    {fullName:'Сидоров Г.Г.', assessment:9},
    {fullName:'Немолодой Д.Д', assessment:2},
    {fullName:'Молодой Е.Е', assessment:3.4}
];
let sum = 0;
let count = 0;
let badStudent = [];
for (let index = 0; index < classroom.length; index++) {
    let student = classroom[index];
    let { fullName, assessment } = student;
    if (assessment > 5 || assessment < 0) {
        console.log('Это значение учитываться не будет, оно не соответствует допустимым значениям');
        continue;
    }
    if (assessment < 4)
        badStudent.push(student);

    sum += assessment;
    count += 1;
}
let averageGrade = sum / count;
console.log('Средняя оценка: ' + averageGrade.toFixed(2));
console.log('Плохие студенты:');
if (badStudent.length === 0) {
    console.log('Неуспевающих нет');
} else {
    badStudent.forEach((student) => {
    console.log('ФИО: ' + student.fullName + '; Оценка: ' + student.assessment);
    });
}
```
