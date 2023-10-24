#lang racket

; Return 7 with cdr / car combinations

; Lists
(define lista1 (list 1 3 (list 5 7) 9))
(define lista2 (list (list 7)))
(define lista3 (list 1 (list 2 (list 3 (list 4 (list 5 (list 6 7)))))))

; Combinations
(car (cdr (car (cdr (cdr lista1)))))
(car (car lista2))
(car (cdr (car (cdr (car (cdr (car (cdr (car (cdr (car (cdr lista3))))))))))))