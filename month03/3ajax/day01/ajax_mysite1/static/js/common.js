function createXhr(){
    if (window.XMLHttpRequest){
        <!--支持 XMLHttpRequest-->
        var xhr = new XMLHttpRequest();
        console.log(xhr);
    }else{
        var xhr = new ActiveXObject('Microsoft.XMLHTTP');
    }
    return xhr;
}