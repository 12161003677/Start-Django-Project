function format_value(){
    s = document.getElementById('value').value
    a = []
    a = s.split(',')
    if(a.length==2){
        document.getElementById('value').value = a[0]+'.'+a[1]
    }
}

function valida_form_aluno(i){
    if(document.getElementById('pass').value == document.getElementById('pass2').value){
        if(i == 0)window.location.href="submit"
        else window.location.href="submit"
    }else alert('Senhas Diferentes !')
}