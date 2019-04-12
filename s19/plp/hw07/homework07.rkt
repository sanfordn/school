;;  ------------------------------------------------------------------------
;; |   FILE           :  homework07.rkt                                     |
;; |   AUTHOR         :  Nick Sanford                                 |
;; |   CREATION DATE  :  2019/03/14                                         |
;; |   DESCRIPTION    :  a preprocessor for our little language             |
;; |                     and functions that analyze programs in the core    |
;;  ------------------------------------------------------------------------
;; |   MODIFIED BY    :  ??????????                                         |
;; |   CREATION DATE  :  2019/03/??                                         |
;; |   DESCRIPTION    :  [ what you added and changed ]                     |
;;  ------------------------------------------------------------------------

#lang racket
(require "syntax-procs.rkt")
(provide (all-defined-out))   ; exports every function defined in the file

;;  ------------------------------------------------------------------------
;;   This code works with the following grammar:
;;
;;                       --------------------------- CORE FEATURES
;;        <exp>      ::= <varref>
;;                     | ( lambda ( <var> ) <exp> )
;;                     | ( <exp> <exp> )
;;                       --------------------------- ABSTRACTIONS
;;                     | ( let (<exp> <exp>) <exp> )
;;  ------------------------------------------------------------------------

;; --------------------------------------------------------------------------
;; preprocess :: full-exp -> core-exp
;; --------------------------------------------------------------------------

(define preprocess
  (lambda (exp)
    (cond
      ( (varref? exp) exp)
      ( (lambda? exp)
        (list 'lambda (list (lambda->param exp))
              (preprocess (lambda->body exp))) )
      ( (app? exp)
        (list (preprocess (app->proc exp))
              (preprocess (app->arg  exp))) )
      ( else  ;; let
        (let ((var  (let->var  exp))
              (val  (let->val  exp))
              (body (let->body exp)))
          (list (list 'lambda (list var) (preprocess body))
                (preprocess val)) ) ))))

;; --------------------------------------------------------------------------
;; functions that analyze expressions in the core language
;; --------------------------------------------------------------------------

;; occurs-bound? :: core-exp -> boolean

(define occurs-bound?
  (lambda (s exp)
    (cond ((varref? exp) #f)
          ((app? exp)    (or (occurs-bound? s (app->proc exp))
                             (occurs-bound? s (app->arg  exp))))
          ((lambda? exp) (or (occurs-bound? s (lambda->body exp))
                             (and (eq? s (lambda->param exp))
                                  (occurs-free? s (lambda->body exp)))))
          (else (error 'occurs-bound? "invalid exp ~a" exp)))))

;; occurs-free? :: core-exp -> boolean

(define occurs-free?
  (lambda (s exp)
    (cond ((varref? exp) (eq? s exp))
          ((app? exp)    (or (occurs-free? s (app->proc exp))
                             (occurs-free? s (app->arg  exp))))
          ((lambda? exp) (and (not (eq? s (lambda->param exp)))
                              (occurs-free? s (lambda->body exp))))
          (else (error 'occurs-free? "invalid exp ~a" exp)))))

;; --------------------------------------------------------------------------
;; functions you write for Homework 7 go below
;; --------------------------------------------------------------------------

;; --------------------------------------------------------------------------
;; Problem 1
;; --------------------------------------------------------------------------

(define max-digit
  (lambda (n)
    (if (digit? n)
        n
        (max (remainder n 10) (max-digit (quotient n 10))))))

(define digit?
  (lambda (n)
    (and (>= n 0) (< n 10))))

;; --------------------------------------------------------------------------
;; Problem 2
;; --------------------------------------------------------------------------

(define set-add
  (lambda (sym S)
    (if (member sym S)
        S
        (cons sym S))))

(define set-union
  (lambda (s1 s2)
    (if (null? s1)
        s2
        (set-union (rest s1) (set-add (first s1) s2)))))

;; --------------------------------------------------------------------------
;; Problem 3
;; --------------------------------------------------------------------------

(define declared-vars
  (lambda (exp)
    (cond ((varref? exp)
           '())
          ((app? exp)
           (set-union (declared-vars (app->proc exp))
                      (declared-vars (app->arg exp))))
          ((lambda? exp)
           (if (symbol? (lambda->param exp))
               (set-add (lambda->param exp)
                        (declared-vars (lambda->body exp)))
               (set-union (lambda->param exp)
                          (declared-vars (lambda->body exp)))))
          ((let? exp)
           (declared-vars (preprocess exp))))))

;; --------------------------------------------------------------------------
;; Problem 4
;; --------------------------------------------------------------------------

(define free-vars
  (lambda (exp)
    (free-vars-helper exp '())))


(define free-vars-helper
  (lambda (exp declared-vars)
    (cond ((varref? exp)
           (if (symbol? declared-vars)
               (if (eq? declared-vars exp)
                   '()
                   (list exp))
               (if (member exp declared-vars)
                   '()
                   (list exp))))
          ((app? exp)
           (set-union (free-vars-helper (app->proc exp) declared-vars)
                      (free-vars-helper (app->arg exp) declared-vars)))
          ((lambda? exp)
           (if (symbol? (lambda->param exp))
               (free-vars-helper (lambda->body exp)
                                 (set-add (lambda->param exp) declared-vars))
               (free-vars-helper (lambda->body exp)
                                 (set-union (lambda->param exp) declared-vars))))
          ((let? exp)
           (free-vars-helper (preprocess exp))))))