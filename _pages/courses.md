---
title: "课程清单"
layout: single
permalink: /courses/
author_profile: true
toc: true
toc_label: 'Semesters'
toc_sticky: true
---

**站务提示:** 只提供近一学年的课程清单, 之前学期的课程清单参见<a href='https://fdu-math.github.io/courses-archived' style='color: blue; text-decoration: underline;'>此处</a>, 但2022-2023学年之前的课程清单暂不提供.
{: .notice}

<div class="notice--warning">
  <p><i><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /> The content of this webpage is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.</i></p>
</div>

## 2022-2023学年第1学期（本科）
<script type="text/javascript">
document.onkeyup = function(e){
    var theEvent = e || window.event;
    var code = theEvent.keyCode || theEvent.which || theEvent.charCode;
    if (code == 13) {
        var storeId = document.getElementById('undergrad2223F_table');
        searchColFunc(storeId, document.getElementById("keySearchCourseNumber2223F"), 0, true);
        searchColFunc(storeId, document.getElementById("keySearchCourseName2223F"), 1, false);
        searchColFunc(storeId, document.getElementById("keySearchTeacherName2223F"), 3, false);
    }
};
function searchColFunc(storeId, keyId, searchCol, refreshBool){
    var key = keyId.value;
    var rowsLength = storeId.rows.length;
    var nullSelection = true;
    for(var i=1;i<rowsLength;i++){
        if(storeId.rows[i].style.display == ''){
            nullSelection = false;
            break
        }
    }
    for(var i=1;i<rowsLength;i++){
        var searchText = storeId.rows[i].cells[searchCol].innerHTML;
        if(nullSelection||refreshBool){
            storeId.rows[i].style.display = '';
        }
        if(searchText.match(key)){
            if(storeId.rows[i].style.display == 'none'){// Do Nothing
            }else{
                storeId.rows[i].style.display = '';
            }
        }else{
            storeId.rows[i].style.display = 'none';
        }
    }
}
</script>
<div style='text-align: center;' id='undergrad2223F'> 
    <small>
        <table id='undergrad2223F_table'>
            <thead>
                <tr>
                    <td>课程序号 <input type="text" id="keySearchCourseNumber2223F" value="" /></td>
                    <td>课程名称 <input type="text" id="keySearchCourseName2223F" value="" /></td>
                    <td>学分</td>
                    <td>教师 <input type="text" id="keySearchTeacherName2223F" value="" /></td>
                    <td>职称</td>
                    <td>开课院系</td>
                    <td>课程大纲</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH010001.01'>MATH010001.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH010001'>MATH010001</a></td>
                    <td>4</td>
                    <td>肖晓</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH110001.01'>MATH110001.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH110001'>MATH110001</a></td>
                    <td>2</td>
                    <td>杭国明</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH115001.01'>MATH115001.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH115001'>MATH115001</a></td>
                    <td>1</td>
                    <td>杨翎</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120003.01'>MATH120003.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120003'>MATH120003</a></td>
                    <td>5</td>
                    <td>陆立强</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120003.02'>MATH120003.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120003'>MATH120003</a></td>
                    <td>5</td>
                    <td>石磊</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120003.03'>MATH120003.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120003'>MATH120003</a></td>
                    <td>5</td>
                    <td>张仑</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120003.04'>MATH120003.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120003'>MATH120003</a></td>
                    <td>5</td>
                    <td>任汝飞</td>
                    <td>青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120005.02'>MATH120005.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120005'>MATH120005</a></td>
                    <td>4</td>
                    <td>朱慧敏</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120007.01'>MATH120007.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120007'>MATH120007</a></td>
                    <td>4</td>
                    <td>许虹</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120007.02'>MATH120007.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120007'>MATH120007</a></td>
                    <td>4</td>
                    <td>张静</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120007.05'>MATH120007.05</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120007'>MATH120007</a></td>
                    <td>4</td>
                    <td>王珺</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120010.01'>MATH120010.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120010'>MATH120010</a></td>
                    <td>3</td>
                    <td>莫景科</td>
                    <td>青年研究员</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120010.02'>MATH120010.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120010'>MATH120010</a></td>
                    <td>3</td>
                    <td>杨翎</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120011.01'>MATH120011.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120011'>MATH120011</a></td>
                    <td>5</td>
                    <td>朱胜林,齐子豪</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120011.02'>MATH120011.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120011'>MATH120011</a></td>
                    <td>5</td>
                    <td>朱胜林,齐子豪</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120011.03'>MATH120011.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120011'>MATH120011</a></td>
                    <td>5</td>
                    <td>谢启鸿,冯鸽</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120011.04'>MATH120011.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120011'>MATH120011</a></td>
                    <td>5</td>
                    <td>谢启鸿,冯鸽</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120011.05'>MATH120011.05</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120011'>MATH120011</a></td>
                    <td>5</td>
                    <td>李骏,韩京俊,江辰,周杨</td>
                    <td>教授，<br />青年研究员，<br />青年研究员，<br />青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120011.06'>MATH120011.06</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120011'>MATH120011</a></td>
                    <td>5</td>
                    <td>李骏,韩京俊,江辰,周杨</td>
                    <td>教授，<br />青年研究员，<br />青年研究员，<br />青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120012.01'>MATH120012.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120012'>MATH120012</a></td>
                    <td>4</td>
                    <td>张建国</td>
                    <td>副教授</td>
                    <td>基础医学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120014.01'>MATH120014.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120014'>MATH120014</a></td>
                    <td>5</td>
                    <td>严金海,王丽丹</td>
                    <td>副教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120014.02'>MATH120014.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120014'>MATH120014</a></td>
                    <td>5</td>
                    <td>严金海,王丽丹</td>
                    <td>副教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120014.03'>MATH120014.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120014'>MATH120014</a></td>
                    <td>5</td>
                    <td>吴昊,翟剑</td>
                    <td>教授，<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120014.04'>MATH120014.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120014'>MATH120014</a></td>
                    <td>5</td>
                    <td>吴昊,翟剑</td>
                    <td>教授，<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.02'>MATH120016.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>张巍</td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.03'>MATH120016.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>张守志</td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.04'>MATH120016.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>郭跃飞</td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.05'>MATH120016.05</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>王勇</td>
                    <td>讲师</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.06'>MATH120016.06</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>应坚刚</td>
                    <td>教授</td>
                    <td>经济学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.07'>MATH120016.07</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>官辉琪</td>
                    <td>讲师</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.08'>MATH120016.08</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>严金海</td>
                    <td>副教授</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.09'>MATH120016.09</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>徐禛</td>
                    <td>讲师</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.10'>MATH120016.10</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>谢锡麟</td>
                    <td>正高级讲师</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.11'>MATH120016.11</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>谢锡麟</td>
                    <td>正高级讲师</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120016.12'>MATH120016.12</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120016'>MATH120016</a></td>
                    <td>5</td>
                    <td>吴汉忠</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120020.02'>MATH120020.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120020'>MATH120020</a></td>
                    <td>3</td>
                    <td>蔡志杰</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120021.01'>MATH120021.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120021'>MATH120021</a></td>
                    <td>5</td>
                    <td>徐惠平</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120021.02'>MATH120021.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120021'>MATH120021</a></td>
                    <td>5</td>
                    <td>范恩贵</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120021.03'>MATH120021.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120021'>MATH120021</a></td>
                    <td>5</td>
                    <td>刘旭胜</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120021.04'>MATH120021.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120021'>MATH120021</a></td>
                    <td>5</td>
                    <td>黄昭波</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120021.05'>MATH120021.05</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120021'>MATH120021</a></td>
                    <td>5</td>
                    <td>张永前</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120021.08'>MATH120021.08</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120021'>MATH120021</a></td>
                    <td>5</td>
                    <td>刘进</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120044.01'>MATH120044.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120044'>MATH120044</a></td>
                    <td>3</td>
                    <td>杭国明</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.01'>MATH120045.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>杭国明</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.02'>MATH120045.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>肖晓</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.03'>MATH120045.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>秦振云</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.04'>MATH120045.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>贺丹青</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.05'>MATH120045.05</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>黄耿耿</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.06'>MATH120045.06</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>曲鹏</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.07'>MATH120045.07</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>朱慧敏</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH120045.08'>MATH120045.08</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH120045'>MATH120045</a></td>
                    <td>5</td>
                    <td>王剑波</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130001.01'>MATH130001.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130001'>MATH130001</a></td>
                    <td>5</td>
                    <td>李洪全,杨志伟</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130001.02'>MATH130001.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130001'>MATH130001</a></td>
                    <td>5</td>
                    <td>李洪全,杨志伟</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130001.03'>MATH130001.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130001'>MATH130001</a></td>
                    <td>5</td>
                    <td>肖体俊,姚鹿鸣</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130001.04'>MATH130001.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130001'>MATH130001</a></td>
                    <td>5</td>
                    <td>肖体俊,姚鹿鸣</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130004.01'>MATH130004.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130004'>MATH130004</a></td>
                    <td>3</td>
                    <td>林伟</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130004.02'>MATH130004.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130004'>MATH130004</a></td>
                    <td>3</td>
                    <td>张国华</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130004.03'>MATH130004.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130004'>MATH130004</a></td>
                    <td>3</td>
                    <td>严军</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130004.04'>MATH130004.04</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130004'>MATH130004</a></td>
                    <td>3</td>
                    <td>林伟</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130005.01'>MATH130005.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130005'>MATH130005</a></td>
                    <td>3</td>
                    <td>王庆雪</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130005.02'>MATH130005.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130005'>MATH130005</a></td>
                    <td>3</td>
                    <td>李志远</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130005.03'>MATH130005.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130005'>MATH130005</a></td>
                    <td>3</td>
                    <td>陈猛</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130006.01'>MATH130006.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130006'>MATH130006</a></td>
                    <td>3</td>
                    <td>陈伯勇</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130009.01'>MATH130009.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130009'>MATH130009</a></td>
                    <td>3</td>
                    <td>许明宇</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130009h.01'>MATH130009h.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130009'>MATH130009</a></td>
                    <td>4</td>
                    <td>谢践生</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130011.01'>MATH130011.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130011'>MATH130011</a></td>
                    <td>3</td>
                    <td>徐胜芝</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130011.02'>MATH130011.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130011'>MATH130011</a></td>
                    <td>3</td>
                    <td>王凯</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130011h.01'>MATH130011h.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130011'>MATH130011</a></td>
                    <td>4</td>
                    <td>姚一隽,章嘉雯,伊泽霖</td>
                    <td>教授，<br />青年副研究员，<br />高等学校教师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130012.02'>MATH130012.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130012'>MATH130012</a></td>
                    <td>3</td>
                    <td>王志强</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130012h.01'>MATH130012h.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130012'>MATH130012</a></td>
                    <td>4</td>
                    <td>雷震</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130013.01'>MATH130013.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130013'>MATH130013</a></td>
                    <td>3</td>
                    <td>嵇庆春</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130013.02'>MATH130013.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130013'>MATH130013</a></td>
                    <td>3</td>
                    <td>谢纳庆</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130017h.01'>MATH130017h.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130017'>MATH130017</a></td>
                    <td>4</td>
                    <td>东瑜昕</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130018.01'>MATH130018.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130018'>MATH130018</a></td>
                    <td>3</td>
                    <td>张德志</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130022.01'>MATH130022.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130022'>MATH130022</a></td>
                    <td>3</td>
                    <td>王利彬</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130026.01'>MATH130026.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130026'>MATH130026</a></td>
                    <td>3</td>
                    <td>李春贺</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130027.01'>MATH130027.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130027'>MATH130027</a></td>
                    <td>3</td>
                    <td>张奇</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130030.01'>MATH130030.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130030'>MATH130030</a></td>
                    <td>2</td>
                    <td>李春贺</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130032.01'>MATH130032.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130032'>MATH130032</a></td>
                    <td>3</td>
                    <td>梁振国,张国华</td>
                    <td>副教授，<br />教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130033.01'>MATH130033.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130033'>MATH130033</a></td>
                    <td>3</td>
                    <td>李荣敏</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130036.01'>MATH130036.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130036'>MATH130036</a></td>
                    <td>3</td>
                    <td>高卫国</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130043.01'>MATH130043.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130043'>MATH130043</a></td>
                    <td>3</td>
                    <td>任汝飞</td>
                    <td>青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130052.01'>MATH130052.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130052'>MATH130052</a></td>
                    <td>3</td>
                    <td>李洪全</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130055.01'>MATH130055.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130055'>MATH130055</a></td>
                    <td>3</td>
                    <td>李荣敏</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130056.01'>MATH130056.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130056'>MATH130056</a></td>
                    <td>3</td>
                    <td>邱维元</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130057.01'>MATH130057.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130057'>MATH130057</a></td>
                    <td>3</td>
                    <td>许亚善</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130059.01'>MATH130059.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130059'>MATH130059</a></td>
                    <td>3</td>
                    <td>朱松</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130067.01'>MATH130067.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130067'>MATH130067</a></td>
                    <td>3</td>
                    <td>赵冬华</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130068.01'>MATH130068.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130068'>MATH130068</a></td>
                    <td>3</td>
                    <td>吴泉水</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130072.01'>MATH130072.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130072'>MATH130072</a></td>
                    <td>3</td>
                    <td>苏仰锋</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130073.01'>MATH130073.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130073'>MATH130073</a></td>
                    <td>3</td>
                    <td>薛军工</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130074.01'>MATH130074.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130074'>MATH130074</a></td>
                    <td>3</td>
                    <td>张云新</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130080.01'>MATH130080.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130080'>MATH130080</a></td>
                    <td>3</td>
                    <td>魏益民</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130091.01'>MATH130091.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130091'>MATH130091</a></td>
                    <td>5</td>
                    <td>周子翔,邵杰</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130091.02'>MATH130091.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130091'>MATH130091</a></td>
                    <td>5</td>
                    <td>周子翔,邵杰</td>
                    <td>教授，<br /></td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130108.01'>MATH130108.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130108'>MATH130108</a></td>
                    <td>3</td>
                    <td>陆帅</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130111.01'>MATH130111.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130111'>MATH130111</a></td>
                    <td>3</td>
                    <td>马继明</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130112.01'>MATH130112.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130112'>MATH130112</a></td>
                    <td>3</td>
                    <td>马继明</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130112h.01'>MATH130112h.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130112'>MATH130112</a></td>
                    <td>4</td>
                    <td>吕志</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130113.01'>MATH130113.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130113'>MATH130113</a></td>
                    <td>3</td>
                    <td>李平</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130114.01'>MATH130114.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130114'>MATH130114</a></td>
                    <td>3</td>
                    <td>郭坤宇</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130121.01'>MATH130121.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130121'>MATH130121</a></td>
                    <td>3</td>
                    <td>周忆</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130126.01'>MATH130126.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130126'>MATH130126</a></td>
                    <td>3</td>
                    <td>田学廷</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130130.01'>MATH130130.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130130'>MATH130130</a></td>
                    <td>3</td>
                    <td>江智</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130133.01'>MATH130133.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130133'>MATH130133</a></td>
                    <td>3</td>
                    <td>石荣刚</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130137.01'>MATH130137.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130137'>MATH130137</a></td>
                    <td>3</td>
                    <td>杨卫红</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130139.01'>MATH130139.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130139'>MATH130139</a></td>
                    <td>3</td>
                    <td>华波波</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130141.01'>MATH130141.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130141'>MATH130141</a></td>
                    <td>3</td>
                    <td>吴河辉</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130143h.03'>MATH130143h.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130143'>MATH130143</a></td>
                    <td>4</td>
                    <td>王庆雪</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130152.01'>MATH130152.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130152'>MATH130152</a></td>
                    <td>2</td>
                    <td>傅吉祥,沈维孝,姚一隽</td>
                    <td>教授，<br />教授，<br />教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130154.01'>MATH130154.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130154'>MATH130154</a></td>
                    <td>6</td>
                    <td>楼红卫,蔡圆</td>
                    <td>教授，<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130154.02'>MATH130154.02</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130154'>MATH130154</a></td>
                    <td>6</td>
                    <td>楼红卫,蔡圆</td>
                    <td>教授，<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130154.03'>MATH130154.03</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130154'>MATH130154</a></td>
                    <td>6</td>
                    <td>楼红卫,蔡圆</td>
                    <td>教授，<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130159.01'>MATH130159.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130159'>MATH130159</a></td>
                    <td>3</td>
                    <td>Elie Francis AIDEKON</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130162.01'>MATH130162.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130162'>MATH130162</a></td>
                    <td>4</td>
                    <td>姚一隽</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130163.01'>MATH130163.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130163'>MATH130163</a></td>
                    <td>4</td>
                    <td>王志强</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130166.01'>MATH130166.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130166'>MATH130166</a></td>
                    <td>3</td>
                    <td>周子翔,梁振国,陈曦</td>
                    <td>教授，<br />副教授，<br />青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='fdu-math.github.io/courses/class-id/MATH130167.01'>MATH130167.01</a></td>
                    <td><a href='fdu-math.github.io/courses/MATH130167'>MATH130167</a></td>
                    <td>3</td>
                    <td>丁琪</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
            </tbody>
        </table>
    </small>
</div>
## 2022-2023学年第1学期（研究生）
