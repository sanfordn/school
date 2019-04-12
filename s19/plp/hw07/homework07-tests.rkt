;;
;; FILE:     homework07-tests.rkt
;; AUTHOR:   NICK SANFORD
;; DATE:     15 MARCH 2019
;; COMMENT:  This file loads "homework07.rkt" and runs tests on its
;;           publicly-defined functions.
;;
;; MODIFIED: 
;; CHANGE:   
;;

#lang racket
(require rackunit)
(require "homework07.rkt")

;; -----------------------------------------------------------------------------
;; Problem 1 Tests
;; -----------------------------------------------------------------------------
(check-equal? (max-digit 2019) 9)
(check-equal? (max-digit 262) 6)
(check-equal? (max-digit 32632453245) 6)

;; -----------------------------------------------------------------------------
;; Problem 2 Tests
;; -----------------------------------------------------------------------------

(check-equal? (set-add 3 '(4 64432 56 3)) '(4 64432 56 3))
(check-equal? (set-add 3 '(4 6 66 56)) '(3 4 6 66 56))
(check-equal? (set-union '(2 3 4 5) '(5 6 7 8)) '(4 3 2 5 6 7 8))
(check-equal? (set-union '(1 2 3 4) '(5 6 7 8)) '(4 3 2 1 5 6 7 8))

;; -----------------------------------------------------------------------------
;; Problem 3 Tests
;; -----------------------------------------------------------------------------

(check-equal? (declared-vars 'x)
              '())
(check-equal? (declared-vars '(square x))
              '())
(check-equal? (declared-vars '(lambda (y) (x y)))
              '(y))
(check-equal? (declared-vars '((lambda (y) (y x))
                               (lambda (y) (z y))))
              '(y))
(check-equal? (declared-vars (preprocess '(let (a b)
                                            (let (c (lambda (d) a))
                                              (c a)))))
              '(d c a))

;; -----------------------------------------------------------------------------
;; Problem 4 Tests
;; -----------------------------------------------------------------------------

(check-equal? (free-vars 'x) '(x))
(check-equal? (free-vars '(square x)) '(square x))
(check-equal? (free-vars '((lambda (y) (y (square x)))
                           (lambda (y) (f y))))
              '(x square f))
(check-equal? (free-vars (preprocess '(let (a b)
                                        (let (c (lambda (d) a))
                                          (c a)))))
              '(b))