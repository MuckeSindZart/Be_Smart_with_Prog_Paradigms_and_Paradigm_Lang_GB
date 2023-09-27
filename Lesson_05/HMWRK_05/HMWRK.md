- [Prolog](https://swish.swi-prolog.org/) Онлайн - [swish.swi-prolog.org](https://swish.swi-prolog.org/) 

```Prolog
% Сумма пустого списка равна 0.
sum_list([], 0).

% Сумма списка равна голове списка плюс сумма хвоста - Рекурсивное.
sum_list([Head|Tail], Sum) :-
    sum_list(Tail, TailSum),
    Sum is Head + TailSum.
```

> ?- sum_list([1, 2, 3, 4, 5], X).  
> Output: X = 15
