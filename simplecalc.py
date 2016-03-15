#!/usr/bin/python

#
# Simple calculator: add, subs, mult, div
# Can only perform one operation "at a time"
# (well, one of each of the operations"
#
# Copyright Jesus M. Gonzalez-Barahona 2009
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# October 2009
#

import webappmulti
import urlparse

def decorateHTML (text):

    return ("<html><body>" + text + "</body></html>")

class calculator (webappmulti.app):
    """Cuerpo del PUT en el campo operacion introducir la operacion con letras
        no con simbolos"""
    def operate (self, oper1, oper2,ope):
        if ope == "suma":
            return oper1 + oper2
        elif ope == "resta":
            return oper1 - oper2
        elif ope == "multiplicacion":
            return oper1 * oper2
        elif ope == "division":
            if oper2 == 0:
                return "indeterminacion"
            else:
                return oper1 / oper2
        else:
            return "operacion invalida"

    def sign (self,ope):
        if ope == "suma":
            return "+"
        elif ope == "resta":
            return "-"
        elif ope == "multiplicacion":
            return "*"
        elif ope == "division":
            return "/"
        else:
            return "campo operacion invalido"

    def parse (self, request, rest):

        verb = request.split(' ',1)[0]
        parts = request.split('\r\n\r\n',1)
        if len (parts) == 2:
            body = parts[1]
        else:
            body = ""
        return (verb, body)

    def process (self, (verb, body)):

        if verb == 'PUT':
            params = urlparse.parse_qs(body)
            try:
                self.oper1 = int(params['oper1'][0])
                self.oper2 = int(params['oper2'][0])
                self.ope = str(params['operacion'][0])
                self.result = self.operate (self.oper1, self.oper2, self.ope)
                success = True
            except:
                success = False
                (error, message) = ("400 Error",
                                    "Error in parameters for operation")
        elif verb == 'GET':
            success = True
        else:
            success = False
            (error, message) = ("400 Error",
                                "HTTP verb " + verb + " not supported")

        if success:
            return ("200 OK", decorateHTML(str(self.oper1) + self.sign(self.ope) +
                                           str(self.oper2) +
                                           "=" + str(self.result)))
        else:
            return (error, decorateHTML(message))

    def __init__ (self):

        self.oper1 = 0
        self.oper2 = 0
        self.ope = "suma"
        self.result = 0


if __name__ == "__main__":
    calcObj = calculator()
    multiCalc = webappmulti.webApp ("localhost", 1234,
                                    {'/calculator': calcObj,})
