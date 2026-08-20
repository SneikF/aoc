#lang racket

(define member?
   (lambda (atom list)
      (cond
         ((null? list) #f)
         ((equal? atom (car list)) #t)
         (else (member? atom (cdr list))))))

(define is-nice?
   (lambda (word)
      (if (and
               (three-vowels? word)
               (double? word)
               (allow? word))
            1 0)))

(define vowel-number
   (lambda (list)
      (cond
         ((null? list) 0)
         ((vowel? (~a (car list))) (+ 1 (vowel-number (cdr list))))
         (else (vowel-number (cdr list))))))

(define vowel?
   (lambda (atom)
      (member? atom (list "a" "e" "i" "o" "u"))))

(define three-vowels?
   (lambda (word)
      (cond
         ((>= (vowel-number word) 3) #true)
         (else #false))))

(define double?
   (lambda (word)
      (cond
         ((null? (cdr word)) #f)
         ((equal? (~a (car word)) (~a (car (cdr word)))) #t)
         (else (double? (cdr word))))))

(define allow?
   (lambda (word)
      (cond
         ((null? (cdr word)) #t)
         ((member? (string-append (~a (car word)) (~a (car (cdr word))))
                     (list "ab" "cd" "pq" "xy"))
               #f)
         (else (allow? (cdr word))))))

(define counter
   (lambda (words)
      (cond
         ((null? words) 0)
         (else (+ (is-nice? (car words)) (counter (cdr words)))))))

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