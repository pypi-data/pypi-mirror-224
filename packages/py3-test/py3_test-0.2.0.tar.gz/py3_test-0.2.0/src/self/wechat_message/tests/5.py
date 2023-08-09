"""
@Time   : 2019/5/20
@author : lijc210@163.com
@Desc:  : 功能描述。
"""


def quick_reply():
    html = """

<link href='https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css' rel='stylesheet'>
<style type='text/css'>
    table.gridtable {
        font-family: verdana, arial, sans-serif;
        font-size: 11px;
        color: #333333;
        border-width: 1px;
        border-color: #666666;
        border-collapse: collapse;
    }

    table.gridtable th {
        border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #666666;
        background-color: #dedede;
    }

    table.gridtable td {
    {#word-break: break-all;#} border-width: 1px;
        padding: 8px;
        border-style: solid;
        border-color: #666666;
        background-color: #ffffff;
    }

    table.gridtable td a {
        display: inline;
    }
</style>
<body>

<div style='width:300px;height:400px;overflow-y:scroll;float: right;margin-top: 100px;margin-right: 100px'>
    <!-- CSS goes in the document HEAD or added to your external stylesheet -->


    <!-- Table goes in the document BODY -->
    <table class='gridtable'>
        <tr>
            <th>单击编辑，双击发送
                <a href='http://127.0.0.1:8000/wechat/statistics.html' target='_blank'>统计</a>
                <a href='http://127.0.0.1:8000/wechat/search.html' target='_blank'>搜索</a>
            </th>
            <th>操作</th>
        </tr>

        <tr>
            <td id=1 onfocusout='save(this)' contentEditable='true' ondblclick='send(this)'>aaaaaaaaaaaaaaa</td>
            <td nowrap>
                <a class='btn btn-danger' href='#' onclick='level_down(this)'><i class='fa fa-level-down fa-lg'></i>
                </a>&nbsp;
                <a class='btn btn-danger' href='#' onclick='level_up(this)'><i class='fa fa-level-up fa-lg'></i> </a>&nbsp;
                <a class='btn btn-danger' href='#' onclick='remove1(this)'><i class='fa fa-trash-o fa-lg'></i> </a>
            </td>
        </tr>
        <tr>
            <td><a onclick='add(this)' class='btn btn-danger' href='#'><i class='fa fa-plus fa-lg'></i> </a></td>
        </tr>
    </table>
</div>
    """
    return html.replace("\n", "")


def get_script():
    script = """
<script>
    function send(obj) {
        document.querySelector('#editArea').innerText=obj.innerText;
    };

    function save(obj) {
        var data = {
            'id': obj.id,
            'content': obj.innerText
        };
        var httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', 'save', true);
        httpRequest.setRequestHeader('Content-type', 'application/json');
        httpRequest.send(JSON.stringify(data));
        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                var json = httpRequest.responseText;
                console.log(json);
            }
        };
    };

    function level_down(obj) {
        var len = $(obj).length;
        var $tr = $(obj).parents('tr');
        if ($tr.index() != len - 2) {
            $tr.fadeOut().fadeIn();
            $tr.next().after($tr);
        }
    };

    function level_up(obj) {
        var $tr = $(obj).parents('tr');
        if ($tr.index() != 0) {
            $tr.fadeOut().fadeIn();
            $tr.prev().before($tr);
        };
    };

    function remove1(obj) {
        var id = $(obj).parent().prev().attr('id');
        var httpRequest = new XMLHttpRequest();
        httpRequest.open('GET', '/remove?id='+id, true);
        httpRequest.send();
        httpRequest.onreadystatechange = function () {
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {
                var json = httpRequest.responseText;
                console.log(json);
                $(obj).parent().parent().remove();
            }
        };
    };

</script>
    """
    return script.replace("\n", "")


if __name__ == "__main__":
    print(quick_reply())
    print(get_script())
