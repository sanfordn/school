;;
;; FILE:     homework05-tests.rkt
;; AUTHOR:   NICK SANFORD
;; DATE:     28 FEBRUARY 2019
;; COMMENT:  This file loads "homework05.rkt" and runs tests on its
;;           publicly-defined functions.
;;
;; MODIFIED: 
;; CHANGE:   
;;

#lang racket
(require rackunit)
(require "homework05.rkt")

;; --------------------------------------------------------------------------
;; Problem 1                                           (structural recursion)
;; --------------------------------------------------------------------------

(check-false (list-of? number? '(1 2 3 "Eugene" 4 5)))
(check-true (list-of? number? '(1 2 3 4 5)))

;; --------------------------------------------------------------------------
;; Problem 2                                               (mutual recursion)
;; --------------------------------------------------------------------------

(check-equal? (nlist-* '(1 2 3 4 5 6 7 8)
                      '(8 7 6 5 4 3 2 1))
              '(8 14 18 20 20 18 14 8))
(check-equal? (nlist-* '((((((1 -2 (3 -4)) 5 ((7 (-8) 9 -10))) 11 -12)) 13 -14))
                       '((((((4  2 (2 -1)) 6 ((3 ( 2) 5 -10)))  7  -8))  9 -10)))
              '((((((4 -4 (6 4)) 30 ((21 (-16) 45 100))) 77 96)) 117 140)))


;; --------------------------------------------------------------------------
;; Problem 3                                               (mutual recursion)
;; --------------------------------------------------------------------------

(check-equal? (string-lengths '("Write" "a" "mutually" "recursive" "function"
                               ("max-length" "str-list")
                               "that" "takes" "one" "argument"
                               ("a" "string-list")))
              '(5 1 8 9 8 (10 8) 4 5 3 8 (1 11)))

(check-equal? (string-lengths '("Nicholas" ("Steven") "Steven" ("James")
                               "Austin" ("James") "Shelly" ("Ann")))
              '(8 (6) 6 (5) 6 (5) 6 (3)))

;; --------------------------------------------------------------------------
;; Problem 4                                               (mutual recursion)
;; --------------------------------------------------------------------------

(check-true (n-list? '(2019 2015 2011)))

(check-true (n-list? '(1 (2 (3 4) 5) 6)))

(check-false (n-list? '(1 (2 (3 a) 5) 6)))

(check-false (n-list? '(((((((a)))))) (b) 2)))

(check-true (n-list? '(((((((((((((((( (3) )))))))) (3) ))))))))))


;; --------------------------------------------------------------------------
;; Problem 5                                               (mutual recursion)
;; --------------------------------------------------------------------------

(check-equal? (prefix->infix '(+ 4 5)) '(4 + 5))

(check-equal? (prefix->infix '(* (+ 4 5)
                                 (+ 7 6))) '((4 + 5) * (7 + 6)))
(check-equal? (prefix->infix '(+ (+ 3 (+ 1 2)) (* 7 (/ 9 8))))
                             '((3 + (1 + 2)) + (7 * (9 / 8))))

;; --------------------------------------------------------------------------

