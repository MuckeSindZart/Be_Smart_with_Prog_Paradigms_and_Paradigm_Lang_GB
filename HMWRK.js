// ---------------Task1--------------- //

//Задача №1
//Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
//сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

function bubbleSortDescending(numbers) {
    var n = numbers.length;
    var swapped;
  
    do {
      swapped = false;
      for (var i = 0; i < n - 1; i++) {
        if (numbers[i] < numbers[i + 1]) {
          var temp = numbers[i];
          numbers[i] = numbers[i + 1];
          numbers[i + 1] = temp;
          swapped = true;
        }
      }
    } while (swapped);
  
    return numbers;
  }
  
  //
  
  var numbers = [5, 2, 9, 1, 5, 6];
  bubbleSortDescending(numbers);
  console.log(numbers); // Вывод: [9, 6, 5, 5, 2, 1]
  
  // ---------------Task2--------------- //
  
  //Задача №2
  //Написать точно такую же процедуру, но в декларативном стиле
  
  function sortDescending(numbers) {
    return numbers.sort((a, b) => b - a);
  }
  
  //
  
  var numbers = [5, 2, 9, 1, 5, 6];
  sortDescending(numbers);
  console.log(numbers); // Вывод: [9, 6, 5, 5, 2, 1]