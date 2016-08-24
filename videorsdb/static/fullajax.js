function full_ajax(url_ajax, metodo, datos){
        $.ajax({         
            url: url_ajax,
            type : metodo,
            data : datos,
            success : function(data){
                if(data){
                    location.href = data
                }else{
                alert('hola')
                }
                
            }
        });
    }