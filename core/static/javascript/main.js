function dispositions(){
    h = document.getElementById('menu').offsetHeight
    document.getElementById('pag').style.marginTop = (h)+"px"
}
function format_value(){
    s = document.getElementById('value2').value
    a = []
    a = s.split(',')
    if(a.length==2){
        document.getElementById('value2').value = a[0]+'.'+a[1]
    }
}

function valida_form_aluno(i){
    if(document.getElementById('pass').value == document.getElementById('pass2').value){
        if(i == 0)window.location.href="submit"
        else window.location.href="submit"
    }else alert('Senhas Diferentes !')
}

function update_input_select_prod(){
    s = document.getElementById('prod').value
    s = s.split(',')
    id = s[0]
    p = s[1]
    document.getElementById('price').value = p
    update_value()
    //document.getElementById(id).value = document.getElementById('price').value
}

function update_value(){
    price = document.getElementById('price').value
    price = parseFloat(price)
    qtd =  document.getElementById('amount').value
    qtd = parseInt(qtd)
    value = (price*qtd)
    document.getElementById('value2').innerHTML = 'R$ '+value
    document.getElementById('value').value = value
}