#lang racket

(require file/md5)

(define lowest-number
   (lambda (key n-zeros)
      (lowest-number-iter key 1 n-zeros)))

(define lowest-number-iter
   (lambda (key num n-zeros)
      (cond
         ((has-n-zeros? key num n-zeros) num)
         (else (lowest-number-iter key (+ 1 num) n-zeros)))))

(define has-n-zeros?
   (lambda (key num n-zeros)
      (equal? (substring 
                  (bytes->string/utf-8 (md5 (string-append 
                     key
                     (number->string num)))) 
                     0 n-zeros)
               (make-string n-zeros #\0))))

(lowest-number "ckczppom" 5)
(lowest-number "ckczppom" 6)