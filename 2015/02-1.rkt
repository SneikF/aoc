#lang racket

(provide (all-defined-out))

(define paper
   (lambda (list-dim)
      (sum 
         wrapping-paper 
         min
         list-dim)))

(define sum
   (lambda (meth1 meth2 list-dim)
      (if (null? list-dim)
         0
         (+
            (meth1 (car list-dim)) 
            (meth2 (car list-dim))
            (sum meth1 meth2 (cdr list-dim))))))

(define wrapping-paper
   (lambda (dimensions)
      (* 2
         (apply + dimensions))))

(define order-list
   (lambda (list)
      (cond
         ((null? list) (list ))
         (else (cons
                  (min list)
                  (order-list (rember (min list) list)))))))

(define rember
   (lambda (a list)
      (cond
         ((null? list) '())
         ((eq? a (car list)) (cdr list))
         (else (cons (car list) (rember a (cdr list)))))))

(define min
   (lambda (list)
      (cond
         ((null? (cdr list)) (car list))
         ((< (car list) (min (cdr list))) (car list))
         (else (min (cdr list))))))

(define aux
   (string-split 
      (list->string 
         (string->list 
            (file->string "02.in"))) "\n"))

(define aux2 (map (lambda (list) (string-split list "x")) aux))

(define lengths
   (lambda (dimensions)
      (list
         (* (car dimensions) (cadr dimensions))
         (* (cadr dimensions) (caddr dimensions))
         (* (caddr dimensions) (car dimensions)))))

(define list-dim (map (lambda (list) (lengths (map string->number list))) aux2))

(define list-dim2 (map (lambda (list) (map string->number list)) aux2))

(paper list-dim)