#lang racket
(define nth
  (lambda (l n)
    (if (zero? n)
        (first l)
        (nth (rest l) (sub1 n)))))
(define sub1
  (lambda (n)
    (- n 1)))
