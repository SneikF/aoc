#lang racket

(require "02-1.rkt")

(define ribbon
   (lambda (list)
      (sum smallest-perimeter mistery-volume list)))

(define smallest-perimeter
   (lambda (list)
      (+ (* 2 (min list)) (* 2 (min (rember (min list) list))))))

(define mistery-volume
   (lambda (list)
      (apply * list)))

(ribbon list-dim2)