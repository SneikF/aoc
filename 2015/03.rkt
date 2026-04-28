#lang racket

(define (file-contents filename)
    (port->string (open-input-file filename) #:close? #t))

(define houses-provided
    (lambda (inst)
        (houses-provided-iter inst '(0 0) '((0 0)))))

(define houses-provided-iter
    (lambda (inst position houses)
        (cond
            ((null? inst) houses)
            (else (houses-provided-iter 
                    (cdr inst) 
                    (update-position position (car inst)) 
                    (update-houses houses (update-position position (car inst))))))))

(define update-position
    (lambda (position direction)
        (cond
            ((eq? direction #\^) (cons (car position) (list (+  1 (car (cdr position))))))
            ((eq? direction #\v) (cons (car position) (list (+ -1 (car (cdr position))))))
            ((eq? direction #\>) (cons (+  1 (car position)) (list (car (cdr position)))))
            ((eq? direction #\<) (cons (+ -1 (car position)) (list (car (cdr position))))))))

(define update-houses
    (lambda (houses new-house)
        (cond
            ((member? houses new-house) houses)
            (else (cons new-house houses)))))

(define member?
    (lambda (lat a)
        (cond
            ((null? lat) #f)
            ((equal? (car lat) a) #t)
            (else (member? (cdr lat) a)))))

(define santa-instructions
    (lambda (instructions)
        (cond
            ((null? instructions) '())
            (else (cons
                    (car instructions)
                    (santa-instructions (cdr (cdr instructions))))))))

(define robosanta-instructions
    (lambda (instructions)
        (cond
            ((null? instructions) '())
            (else (cons
                    (car (cdr instructions))
                    (robosanta-instructions (cdr (cdr instructions))))))))

(define instructions (string->list (file-contents "03.in")))

(define union
    (lambda (a b)
        (cond
            ((null? b) a)
            ((member? a (car b)) (union a (cdr b)))
            (else (union (cons (car b) a) (cdr b))))))

(length (houses-provided instructions))

(length (union
    (houses-provided (santa-instructions instructions))
    (houses-provided (robosanta-instructions instructions))))