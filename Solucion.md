<p>Unico Recurso, nombre del recurso calculator.</p>
<h3>Metodo GET sobre el recurso:</h3>
	<p>Nos devuelve un 200 OK y en el cuerpo la ultima operacion con su resultado.</p>
<h3>Metodo PUT sobre el recurso:</h3>
	<p>Cuerpo del PUT: oper1=X&oper2=Y&operacion=suma (diferentes valores de operacion: suma
	<p>resta, multiplicacion y division).</p>
	<p>Si el cuerpo del PUT es valido nos devolvera un 200 OK y en el cuerpo la operacion con el resultado.</p>
	<p>Si el cuerpo del PUT es inavlido nos devolvera un 400 Error y en el cuerpo Error in 
	parameters for operation.</p>
<h4>Cualquier otro metodo sobre el recuso calculator nos devorlvera un 400 Error</h4>
