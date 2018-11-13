function calculate(){
    var num1=document.getElementById("op1").value;
    var num2=document.getElementById("op2").value;
    var x=parseInt(num1);
    var y=parseInt(num2);
    var op=document.getElementById("operation");
    var calculate=op.options[op.selectedIndex].value;
    if(calculate=="Addition")
    {
     var num3=x+y;
    }
   else if(calculate=="Substraction")
   {
       var num3=x-y;
   }
   else if(calculate=="Multiplication")
   {
       var num3=x*y;
   }
   else{
       var num3=x/y;
   }
   console.log(num3);
}
function largest(){
    var num1=document.getElementById("op1").value;
    var num2=document.getElementById("op2").value;
    var num3=document.getElementById("op3").value;
    var x=parseInt(num1);
    var y=parseInt(num2);
    var z=parseInt(num3);
    if(x>y){
        if(x>z){
            var res=x;
            console.log(x+"is larger");
        }
        else{
           var res=z;
            console.log(z+"is larger");
        }
    }
    else{
        if(y>z){
            var res=y;
            console.log(y+"is larger");
        }
        else{
            var res=z;
            console.log(z+"is larger");
        }
    }
    document.getElementById("result").innerHTML=res;
}
function smallest(){
    var num1=document.getElementById("op1").value;
    var num2=document.getElementById("op2").value;
    var num3=document.getElementById("op3").value;
    var x=parseInt(num1);
    var y=parseInt(num2);
    var z=parseInt(num3);
    if(x<y){
        if(x<z){ 
            var res=x;
            console.log(x+"is smaller");
        }
        else{
            var res=z;
            console.log(z+"is smaller");
        }
    }
    else{
        if(y<z){
            var res=y;
            console.log(y+"is smaller");
        }
        else{
            var res=z;
            console.log(z+"issmaller");
        }
    }
    document.getElementById("result").innerHTML="<table class='table'><tr><td>Result is : </td> <td>"+res+"</td></tr></table>";
}
