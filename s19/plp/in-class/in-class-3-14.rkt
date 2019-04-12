#lang racket
(lexical-address
 (lambda (exp)
   (cond
     (varref? )
     (lambda? (make-lambda ))
     (app? (cons (lexical-address (app->proc exp))
                 (lexical-address (app->args exp))))
     (if? (make-if (lexical-address (if->test exp))
                   (lexical-address (if->then exp))
                   (lexical-address (if->else exp))))
     )))