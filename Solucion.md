Unico Recurso, nombre del recurso calculator.
Metodo GET sobre el recurso: 
	Nos devuelve un 200 OK y en el cuerpo la ultima operacion con su resultado.
Metodo PUT sobre el recurso: 
	Cuerpo del PUT: oper1=X&oper2=Y&operacion=suma (diferentes valores de operacion: suma
	resta, multiplicacion y division).
	Si el cuerpo del PUT es valido nos devolvera un 200 OK y en el cuerpo la operacion 		con el resultado.
	Si el cuerpo del PUT es inavlido nos devolvera un 400 Error y en el cuerpo Error in 
	parameters for operation
Cualquier otro metodo sobre el recuso calculator nos devorlvera un 400 Error
