#lang racket

(define is-very-nice?
   (lambda (word)
      (if (and 
               (double-pair? word)
               (between-repeat? word))
         1 0)))

(define double-pair?
   (lambda (word)
      (cond
         ((null? (cdr (cdr word))) #f)
         ((is-repeat?
                  (car word)
                  (car (cdr word))
                  (cdr (cdr word))) #t)
         (else (double-pair? (cdr word))))))

(define is-repeat?
   (lambda (a b word)
      (cond
         ((null? word) #f)
         ((null? (cdr word)) #f)
         ((and 
            (equal? a (car word))
            (equal? b (car (cdr word)))) #t)
         (else (is-repeat? a b (cdr word))))))
   
(define between-repeat?
   (lambda (word)
      (cond
         ((null? (cdr (cdr (cdr word)))) #f)
         ((equal? (car word) (car (cdr (cdr word)))) #t)
         (else (between-repeat? (cdr word))))))

(define counter
   (lambda (words)
      (cond
         ((null? words) 0)
         (else (+ (is-very-nice? (car words)) (counter (cdr words)))))))

(define aux
   (string-split 
      (list->string 
         (string->list 
            (file->string "05.in"))) "\n"))

(define words-list
   (lambda (words)
      (cond
         ((null? words) (list ))
         (else (cons (string->list (car words)) 
                     (words-list (cdr words)))))))

(counter (words-list aux))