#lang racket
(define count-occurences
  (lambda (ch lst)
    (if (null? lst)
        0
        (+ (count-occurences-se ch (first lst))
           (count-occurences ch (rest lst))))))

(define count-occurences-se
  (lambda (s se)
         (if (symbol? se)
             (if (eq? s se) 1 0)
             (count-occurences s se))))