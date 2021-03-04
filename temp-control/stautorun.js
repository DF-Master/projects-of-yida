var cmd=require('node-cmd');

    cmd.get(
        'notepad',//画图板
    function(data){
        console.log("data")
        }
    );

    cmd.get(
        'C:\\Windows\\System32\\Calc.exe', //计算器
    function(data){
        console.log("cacul")
    }
);