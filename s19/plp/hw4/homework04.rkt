;;
;; FILE:     homework04.rkt
;; AUTHOR:   YOUR NAME
;; DATE:     YOUR DATE
;; COMMENT:  This module defines the five functions specified in
;;           Homework 4 as an importable module.
;;
;; MODIFIED: 
;; CHANGE:   
;;

#lang racket
(require rackunit)      ; enables you to use rackunit tests
(provide string*        ; exports your functions to client code
         collect        ;      You must define a function with
         drop           ;      each name, even if the function
         digit-sum      ;      only returns a default value!
         positions-of)

;; --------------------------------------------------------------------------
;; Problem 1                                              (counted recursion)
;; --------------------------------------------------------------------------

(define string*
  (lambda (str n)
     (if (zero? (sub1 n))
         str
         (string-append (string* str (sub1 n)) str))))

(define sub1
  (lambda (n)
    (- n 1)))

;; --------------------------------------------------------------------------
;; Problem 2                                           (structural recursion)
;; --------------------------------------------------------------------------

(define square
  (lambda (n)
    (* n n)))

(define collect
  (lambda (f lst)
    (if (null? lst)
        '()
        (cons (f (first lst)) (collect f (rest lst))))))

;; --------------------------------------------------------------------------
;; Problem 3                                              (counted recursion)
;; --------------------------------------------------------------------------

(define drop
  (lambda (n lst)
    (if (zero? n)
        lst
        (drop (sub1 n) (rest lst)))))

;; --------------------------------------------------------------------------
;; Problem 4                                           (structural recursion)
;; --------------------------------------------------------------------------

(define digit-sum
  (lambda (n)
      (if (zero? n)
          n
          (+ (remainder n 10) (digit-sum (quotient n 10))))))

;; --------------------------------------------------------------------------
;; Problem 5                   (structural recursion and interface procedure)
;; --------------------------------------------------------------------------

(define helper
  (lambda (s los n)
    'unimplemented))
        

(define positions-of
  (lambda (s los)
    (helper s los 0)))

;; --------------------------------------------------------------------------

