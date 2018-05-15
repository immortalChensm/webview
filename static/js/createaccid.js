window.addEventListener("load",function () {

    //创建账号
    document.getElementById("register").addEventListener("click",function (e) {

        var data = {}
        data['accid'] = document.getElementsByName("accid")[0].value;
        data['name']  = document.getElementsByName("name")[0].value;
        data['mobile']= document.getElementsByName("mobile")[0].value;

        xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function (ev) {
            if(xhr.readyState==4){
                if (xhr.status==200){
                    alert(xhr.responseText);
                }
            }

        };

        xhr.onerror = function (ev) {
            alert("ajax请求错误");
        };
        xhr.open("post","http://127.0.0.1:8090/createaccid",true);
        xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded;charset=utf-8");
        xhr.send("accid="+data['accid']+"&name="+data['name']+"&mobile="+data['mobile']);

    })

})