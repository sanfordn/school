;;
;; FILE:     homework05.rkt
;; AUTHOR:   NICK SANFORD
;; DATE:     28 FEB 2019
;; COMMENT:  This module defines the five functions specified in
;;           Homework 5 as an importable module.  Notice how each
;;           each function has a body and returns a default value.
;;           Writing stubs of this sort enables us to load the file
;;           and run tests, even if the tests fail.
;;
;; MODIFIED: 
;; CHANGE:   
;;

#lang racket
(provide list-of? nlist-* string-lengths n-list? prefix->infix)

;; --------------------------------------------------------------------------
;; Problem 1                                           (structural recursion)
;; --------------------------------------------------------------------------

(define list-of?
  (lambda (type? lst)
    (if (null? lst)
        #t
        (and (type? (first lst)) (list-of? type? (rest lst))))))

;; --------------------------------------------------------------------------
;; Problem 2                                               (mutual recursion)
;; --------------------------------------------------------------------------

(define nlist-*
  (lambda (nlst1 nlst2)
    (if (null? nlst1)
        '()
        (cons (numberexp-* (first nlst1) (first nlst2))
              (nlist-* (rest nlst1) (rest nlst2))))))

(define numberexp-*
  (lambda (nexpr1 nexpr2)
    (if (number? nexpr1)
        (* nexpr1 nexpr2)
        (nlist-* nexpr1 nexpr2))))

;; --------------------------------------------------------------------------
;; Problem 3                                               (mutual recursion)
;; --------------------------------------------------------------------------

(define string-lengths
  (lambda (str-lst)
    (if (null? str-lst)
        '()
        (if (string? (first str-lst))
            (cons (string-length (first str-lst)) (string-lengths (rest str-lst)))
            (cons (string-lengths-se (first str-lst)) (string-lengths (rest str-lst)))))))

(define string-lengths-se
  (lambda (se)
    (if (null? se)
        '()
        (if (string? (first se))
            (cons (string-length (first se)) (string-lengths-se (rest se)))
            (cons (string-lengths-se (first se)) (string-lengths-se (rest se)))))))

;; --------------------------------------------------------------------------
;; Problem 4                                               (mutual recursion)
;; --------------------------------------------------------------------------

(define n-list?
  (lambda (obj)
    (if (null? obj)
        #t
        (if (number? (first obj))
            (n-list? (rest obj))
            (and (num-expr? (first obj)) (n-list? (rest obj)))))))

(define num-expr?
  (lambda (numexp)
    (if (pair? numexp)
        (n-list? numexp)
        (if (null? numexp)
            #t
            (if (number? numexp)
                #t
                #f)))))

;; --------------------------------------------------------------------------
;; Problem 5                                               (mutual recursion)
;; --------------------------------------------------------------------------

(define prefix->infix
  (lambda (binary-exp)
    (if (null? binary-exp)
        '()
        (list (number-expr->infix (second binary-exp))
              (number-expr->infix (first binary-exp))
              (number-expr->infix (third binary-exp))))))

(define number-expr->infix
  (lambda (binary-exp)
    (if (pair? binary-exp)
        (prefix->infix binary-exp)
        binary-exp)))

;; --------------------------------------------------------------------------
