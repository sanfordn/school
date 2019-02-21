#lang racket
(define map-nlist
  (lambda (f nlist)
    (if (null? nlist)
        '()
        (cons (map-numexp f (first nlist))
              (map-nlist f (rest nlist))))))

(define map-numexp
  (lambda (f numexp)
    (if (number? numexp)
        (f numexp)
        (map-nlist f numexp))))
