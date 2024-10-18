function operaciones ()
{
    let n1=parseInt(document.getElementById("n1").value);
    let n2=parseInt(document.getElementById("n2").value);
    let op=document.getElementById("tipo").value;

    if (isnumber(n1) && isnumber(n2))
    {
        switch(op)
        {
            case "+":
                ope=n1+n2;break;
            case "-":
                ope=n1-n2;break;
            case "*":
                ope=n1*n2;break;
            case "/":
                ope=n1/n2;break;  
        }


        let respuesta=document.getElementById("resultado").innerHTML=`<h3><hr>  ${n1}  ${op}  ${n2} = ${ope}`;
    }
    else
    {
        // let respuesta=document.getElementById("resultado")
        // respuesta.innerHTML=`Ingresa solo numeros por favor`;
        let respuesta=document.getElementById("resultado").innerHTML=`Ingresa solo numeros porfavor...`;
        alert("Ingresa solo numeros porfavor");
        
    }
}

function isnumber(n)
{
    return !isNaN(parseInt(n) && isFinite(n));
}