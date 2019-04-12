;;  ------------------------------------------------------------------------
;; |   FILE           :  syntax-procs.rkt                                   |
;; |   AUTHOR         :  Eugene Wallingford                                 |
;; |   CREATION DATE  :  2019/03/07                                         |
;; |   DESCRIPTION    :  These functions implement syntax procedures for    |
;; |                     a language grammar consisting only of variable     |
;; |                     references, lambda expressions, function           |
;; |                     applications, and let expressions.                 |
;;  ------------------------------------------------------------------------

#lang racket
(provide exp?
         varref?
         lambda? lambda->param lambda->body
         app?    app->proc     app->arg
         let?    let->var      let->val      let->body)

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

;;  ------------------------------------------------------------------------
;;  general type predicate

(define exp?
  (lambda (exp)
    (or (varref? exp)
        (lambda? exp)
        (app?    exp)
        (let?    exp))))

;;  ------------------------------------------------------------------------
;;  varrefs

(define varref? symbol?)

;;  ------------------------------------------------------------------------
;;  lambda expressions

(define lambda?
  (lambda (exp)
    (and (list? exp)
         (= (length exp) 3)
         (eq? (car exp) 'lambda)
         (varref? (caadr exp))
         (exp? (third exp)))))

(define lambda->param caadr)
(define lambda->body  third)

;;  ------------------------------------------------------------------------
;;  application expressions  ("apps")

(define app?
  (lambda (exp)
    (and (list? exp)
         (= (length exp) 2)
         (exp? (first exp))
         (exp? (second exp)))))

(define app->proc first)
(define app->arg  second)

;;  ------------------------------------------------------------------------
;;  let expressions

(define let?
  (lambda (exp)
    (and (list? exp)
         (= (length exp) 3)
         (eq? 'let (first exp))
         (binding? (second exp))
         (exp? (third exp)))))

(define binding?
  (lambda (exp)
    (and (list? exp)
         (= (length exp) 2)
         (varref? (first exp))
         (exp? (second exp)))))

(define let->var
  (lambda (let-exp)
    (first (second let-exp))))

(define let->val
  (lambda (let-exp)
    (second (second let-exp))))

(define let->body third)

;; ----- END OF FILE -----