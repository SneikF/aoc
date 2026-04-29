#lang racket

(require "01-1.rkt")

(define (get-basement movements)
   (get-basement-iter movements 1))

(define get-basement-iter
   (lambda (movements position)
      (cond
         ((eq? (get-floor (take movements position)) -1)
            position)
         (else (get-basement-iter movements (+ 1 position))))))
   
(get-basement movs)