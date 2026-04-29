#lang racket

(provide (all-defined-out))

(define get-floor
   (lambda (movements)
      (cond
         ((null? movements) 0)
         ((equal? (car movements) #\() 
            (+ 1 (get-floor (cdr movements))))
         (else (+ -1 (get-floor (cdr movements)))))))

(define movs (string->list (file->string "01.in")))

(get-floor movs)