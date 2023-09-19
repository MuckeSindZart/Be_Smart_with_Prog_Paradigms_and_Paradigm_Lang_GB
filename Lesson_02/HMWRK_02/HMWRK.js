// ---------------Task1--------------- //

// Таблица умножения
// - Условие
// На вход подается число n.
// - Задача
// Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
// Обоснуйте выбор парадигм.


// Для создания таблицы умножения всех чисел от 1 до n можно использовать императивную парадигму,
//  так как задача заключается в выполнении повторяющихся действий (вывод строк таблицы).

function multiplicationTable(n) {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= 9; j++) {
      const result = i * j;
      console.log(`${i} * ${j} = ${result}`);
    }
  }
}

//

multiplicationTable(5);

// В этом коде используется два вложенных цикла for. 
// Внешний цикл перебирает числа от 1 до n, 
// а внутренний цикл перебирает числа от 1 до 9 
// для каждого числа от 1 до n. Для каждой пары 
// чисел выполняется умножение, и результат выводится на экран.

// Этот императивный подход подходит, потому что задача
// требует выполнения конкретных действий для каждой 
// комбинации чисел в таблице умножения, а циклы 
// являются естественным способом управления этими действиями.
