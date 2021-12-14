#lang sicp

(define (closure msg)
  (let ([private_msg msg])
    (define (print)
      (display private_msg)
      (newline))
    (define (update m)
      (set! private_msg m))
    (define (reset)
      (update msg))
    (define (dispatch m)
      (cond
        [(eq? m "print") print]
        [(eq? m "update") update]
        [(eq? m "reset") reset]
        [else (error "Unknown op" m)]))
    dispatch))

(define a (closure "a"))
((a "print"))
((a "update") "a: secret msg")
((a "print"))
(define b (closure "b"))
((b "print"))
((a "reset"))
((a "print"))
