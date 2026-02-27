def filtrar_vocales(cadena, bandera):
    # Err code header
    cadenaError = -100
    symbolError = -200
    emptyError = -300
    lenghtError = -400
    boolError = -500
    successCode = 0

    vowelAscii = [
        ord("A"),
        ord("E"),
        ord("I"),
        ord("O"),
        ord("U"),
        ord("a"),
        ord("e"),
        ord("i"),
        ord("o"),
        ord("u"),
    ]  # //Ascii a interpretar como vocal

    # //Sanity check de acuerdo a lo solicitado
    if isinstance(cadena, str) is False:
        return (cadenaError, None)

    if (
        cadena.isascii() is False
    ):  # Si el string no se puede convertir a
        # ascii contiene caracteres no alphanumericos
        return (symbolError, None)

    if len(cadena) > 30:
        return (lenghtError, None)

    if cadena == "":
        return (emptyError, None)

    if isinstance(bandera, bool) is False:
        return (boolError, None)

    # Containers para ambos casos, la bandera se evalua
    # al final dirigiendo cual de estos se retorna,
    # manteniendo O(n)
    vowels = ""
    conson = ""
    for i in cadena:
        strcode = ord(i)
        # Ascii representando el Rango A-Z
        if strcode > 64 and strcode < 91:
            if strcode in vowelAscii:
                # Comparacion respecto a la lista de vocales
                vowels += i
            else:
                conson += i
        # Ascii representando el rango a-z
        elif strcode > 96 and strcode < 123:
            # Comparacion respecto a la lista de vocales
            if strcode in vowelAscii:
                vowels += i
            else:
                conson += i

        else:
            return (
                symbolError,
                None,
            )  # Por exclusion cualquier Ascii
            # fuera de estos rangos no es alfanumerico

    # Evaluacion de la bandera dirige que container retornar
    if bandera is True:
        return (successCode, vowels)
    else:
        return (successCode, conson)


# ---------------------------------
#           Method Break!
# ---------------------------------


def encontrar_extremos(numlist):
    # Err code header
    typeError = -600
    emptyError = -800
    lenghtError = -900
    numTypeError = -700
    successCode = 0

    # Sanity Check
    if isinstance(numlist, list) is False:
        return (typeError, None, None)

    if len(numlist) == 0:
        return (emptyError, None, None)

    if len(numlist) > 15:
        return (lenghtError, None, None)

    nmin = numlist[
        0
    ]
    # Containers para min y max, initializados al primer elemento de la lista
    nmax = numlist[0]  # para simplificar edge cases
    for i in numlist:
        if (
            type(i) is not int and type(i) is not float
        ):  # Check logico respecto a los tipos aceptados
            return (numTypeError, None, None)

        # Si el error anterior no es levantado
        # la ejecucion continua y se evaluan los min-max
        if (
            i > nmax
        ):
            nmax = i
        elif i < nmin:
            nmin = i

    return (successCode, nmin, nmax)
