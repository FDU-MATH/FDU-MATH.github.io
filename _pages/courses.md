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
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH010001.01'>MATH010001.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH010001'>预科数学（上）</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/肖晓'>肖晓</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH110001.01'>MATH110001.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH110001'>数学概论</a></td>
                    <td>2</td>
                    <td><a href='https://fdu-math.github.io/teachers/杭国明'>杭国明</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH115001.01'>MATH115001.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH115001'>天才引导的历程——数学史上的重大发现</a></td>
                    <td>1</td>
                    <td><a href='https://fdu-math.github.io/teachers/杨翎'>杨翎</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120003.01'>MATH120003.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120003'>高等数学B(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/陆立强'>陆立强</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120003.02'>MATH120003.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120003'>高等数学B(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/石磊'>石磊</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120003.03'>MATH120003.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120003'>高等数学B(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/张仑'>张仑</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120003.04'>MATH120003.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120003'>高等数学B(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/任汝飞'>任汝飞</a></td>
                    <td>青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120005.02'>MATH120005.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120005'>高等数学C(上）</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/朱慧敏'>朱慧敏</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120007.01'>MATH120007.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120007'>高等数学D</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/许虹'>许虹</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120007.02'>MATH120007.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120007'>高等数学D</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/张静'>张静</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120007.05'>MATH120007.05</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120007'>高等数学D</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/王珺'>王珺</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120010.01'>MATH120010.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120010'>解析几何</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/莫景科'>莫景科</a></td>
                    <td>青年研究员</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120010.02'>MATH120010.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120010'>解析几何</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/杨翎'>杨翎</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120011.01'>MATH120011.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120011'>高等代数Ⅰ</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/朱胜林'>朱胜林</a><br /><a href='https://fdu-math.github.io/teachers/齐子豪'>齐子豪</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120011.02'>MATH120011.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120011'>高等代数Ⅰ</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/朱胜林'>朱胜林</a><br /><a href='https://fdu-math.github.io/teachers/齐子豪'>齐子豪</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120011.03'>MATH120011.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120011'>高等代数Ⅰ</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/谢启鸿'>谢启鸿</a><br /><a href='https://fdu-math.github.io/teachers/冯鸽'>冯鸽</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120011.04'>MATH120011.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120011'>高等代数Ⅰ</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/谢启鸿'>谢启鸿</a><br /><a href='https://fdu-math.github.io/teachers/冯鸽'>冯鸽</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120011.05'>MATH120011.05</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120011'>高等代数Ⅰ</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/李骏'>李骏</a><br /><a href='https://fdu-math.github.io/teachers/韩京俊'>韩京俊</a><br /><a href='https://fdu-math.github.io/teachers/江辰'>江辰</a><br /><a href='https://fdu-math.github.io/teachers/周杨'>周杨</a></td>
                    <td>教授<br />青年研究员<br />青年研究员<br />青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120011.06'>MATH120011.06</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120011'>高等代数Ⅰ</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/李骏'>李骏</a><br /><a href='https://fdu-math.github.io/teachers/韩京俊'>韩京俊</a><br /><a href='https://fdu-math.github.io/teachers/江辰'>江辰</a><br /><a href='https://fdu-math.github.io/teachers/周杨'>周杨</a></td>
                    <td>教授<br />青年研究员<br />青年研究员<br />青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120012.01'>MATH120012.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120012'>微积分（上）</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/张建国'>张建国</a></td>
                    <td>副教授</td>
                    <td>基础医学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120014.01'>MATH120014.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120014'>数学分析AI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/严金海'>严金海</a><br /><a href='https://fdu-math.github.io/teachers/王丽丹'>王丽丹</a></td>
                    <td>副教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120014.02'>MATH120014.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120014'>数学分析AI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/严金海'>严金海</a><br /><a href='https://fdu-math.github.io/teachers/王丽丹'>王丽丹</a></td>
                    <td>副教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120014.03'>MATH120014.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120014'>数学分析AI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/吴昊'>吴昊</a><br /><a href='https://fdu-math.github.io/teachers/翟剑'>翟剑</a></td>
                    <td>教授<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120014.04'>MATH120014.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120014'>数学分析AI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/吴昊'>吴昊</a><br /><a href='https://fdu-math.github.io/teachers/翟剑'>翟剑</a></td>
                    <td>教授<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.02'>MATH120016.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/张巍'>张巍</a></td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.03'>MATH120016.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/张守志'>张守志</a></td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.04'>MATH120016.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/郭跃飞'>郭跃飞</a></td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.05'>MATH120016.05</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/王勇'>王勇</a></td>
                    <td>讲师</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.06'>MATH120016.06</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/应坚刚'>应坚刚</a></td>
                    <td>教授</td>
                    <td>经济学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.07'>MATH120016.07</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/官辉琪'>官辉琪</a></td>
                    <td>讲师</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.08'>MATH120016.08</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/严金海'>严金海</a></td>
                    <td>副教授</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.09'>MATH120016.09</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/徐禛'>徐禛</a></td>
                    <td>讲师</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.10'>MATH120016.10</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/谢锡麟'>谢锡麟</a></td>
                    <td>正高级讲师</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.11'>MATH120016.11</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/谢锡麟'>谢锡麟</a></td>
                    <td>正高级讲师</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120016.12'>MATH120016.12</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120016'>数学分析BI</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/吴汉忠'>吴汉忠</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120020.02'>MATH120020.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120020'>线性代数（理工类）</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/蔡志杰'>蔡志杰</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120021.01'>MATH120021.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120021'>高等数学A(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/徐惠平'>徐惠平</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120021.02'>MATH120021.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120021'>高等数学A(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/范恩贵'>范恩贵</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120021.03'>MATH120021.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120021'>高等数学A(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/刘旭胜'>刘旭胜</a></td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120021.04'>MATH120021.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120021'>高等数学A(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/黄昭波'>黄昭波</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120021.05'>MATH120021.05</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120021'>高等数学A(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/张永前'>张永前</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120021.08'>MATH120021.08</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120021'>高等数学A(上）</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/刘进'>刘进</a></td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120044.01'>MATH120044.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120044'>线性代数</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/杭国明'>杭国明</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.01'>MATH120045.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/杭国明'>杭国明</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.02'>MATH120045.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/肖晓'>肖晓</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.03'>MATH120045.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/秦振云'>秦振云</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.04'>MATH120045.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/贺丹青'>贺丹青</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.05'>MATH120045.05</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/黄耿耿'>黄耿耿</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.06'>MATH120045.06</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/曲鹏'>曲鹏</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.07'>MATH120045.07</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/朱慧敏'>朱慧敏</a></td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH120045.08'>MATH120045.08</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH120045'>高等数学C I</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/王剑波'>王剑波</a></td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130001.01'>MATH130001.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130001'>数学分析III</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/李洪全'>李洪全</a><br /><a href='https://fdu-math.github.io/teachers/杨志伟'>杨志伟</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130001.02'>MATH130001.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130001'>数学分析III</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/李洪全'>李洪全</a><br /><a href='https://fdu-math.github.io/teachers/杨志伟'>杨志伟</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130001.03'>MATH130001.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130001'>数学分析III</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/肖体俊'>肖体俊</a><br /><a href='https://fdu-math.github.io/teachers/姚鹿鸣'>姚鹿鸣</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130001.04'>MATH130001.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130001'>数学分析III</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/肖体俊'>肖体俊</a><br /><a href='https://fdu-math.github.io/teachers/姚鹿鸣'>姚鹿鸣</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130004.01'>MATH130004.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130004'>常微分方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/林伟'>林伟</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130004.02'>MATH130004.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130004'>常微分方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/张国华'>张国华</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130004.03'>MATH130004.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130004'>常微分方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/严军'>严军</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130004.04'>MATH130004.04</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130004'>常微分方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/林伟'>林伟</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130005.01'>MATH130005.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130005'>抽象代数</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/王庆雪'>王庆雪</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130005.02'>MATH130005.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130005'>抽象代数</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/李志远'>李志远</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130005.03'>MATH130005.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130005'>抽象代数</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/陈猛'>陈猛</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130006.01'>MATH130006.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130006'>复变函数</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/陈伯勇'>陈伯勇</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130009.01'>MATH130009.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130009'>概率论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/许明宇'>许明宇</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130009h.01'>MATH130009h.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130009'>概率论(H)</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/谢践生'>谢践生</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130011.01'>MATH130011.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130011'>泛函分析</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/徐胜芝'>徐胜芝</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130011.02'>MATH130011.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130011'>泛函分析</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/王凯'>王凯</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130011h.01'>MATH130011h.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130011'>泛函分析(H)</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/姚一隽'>姚一隽</a><br /><a href='https://fdu-math.github.io/teachers/章嘉雯'>章嘉雯</a><br /><a href='https://fdu-math.github.io/teachers/伊泽霖'>伊泽霖</a></td>
                    <td>教授<br />青年副研究员<br />高等学校教师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130012.02'>MATH130012.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130012'>数理方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/王志强'>王志强</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130012h.01'>MATH130012h.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130012'>数理方程（H）</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/雷震'>雷震</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130013.01'>MATH130013.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130013'>微分几何</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/嵇庆春'>嵇庆春</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130013.02'>MATH130013.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130013'>微分几何</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/谢纳庆'>谢纳庆</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130017h.01'>MATH130017h.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130017'>微分流形(H)</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/东瑜昕'>东瑜昕</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130018.01'>MATH130018.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130018'>小波分析</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/张德志'>张德志</a></td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130022.01'>MATH130022.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130022'>应用偏微分方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/王利彬'>王利彬</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130026.01'>MATH130026.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130026'>生物数学</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/李春贺'>李春贺</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130027.01'>MATH130027.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130027'>数学金融学</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/张奇'>张奇</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130030.01'>MATH130030.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130030'>专题讨论</a></td>
                    <td>2</td>
                    <td><a href='https://fdu-math.github.io/teachers/李春贺'>李春贺</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130032.01'>MATH130032.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130032'>动力系统</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/梁振国'>梁振国</a><br /><a href='https://fdu-math.github.io/teachers/张国华'>张国华</a></td>
                    <td>副教授<br />教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130033.01'>MATH130033.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130033'>利息理论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/李荣敏'>李荣敏</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130036.01'>MATH130036.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130036'>计算方法</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/高卫国'>高卫国</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130043.01'>MATH130043.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130043'>数论基础</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/任汝飞'>任汝飞</a></td>
                    <td>青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130052.01'>MATH130052.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130052'>Fourier分析</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/李洪全'>李洪全</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130055.01'>MATH130055.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130055'>非寿险精算数学</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/李荣敏'>李荣敏</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130056.01'>MATH130056.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130056'>复分析</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/邱维元'>邱维元</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130057.01'>MATH130057.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130057'>控制理论基础</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/许亚善'>许亚善</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130059.01'>MATH130059.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130059'>数据结构</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/朱松'>朱松</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130067.01'>MATH130067.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130067'>时间序列分析</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/赵冬华'>赵冬华</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130068.01'>MATH130068.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130068'>抽象代数续论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/吴泉水'>吴泉水</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130072.01'>MATH130072.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130072'>数值逼近</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/苏仰锋'>苏仰锋</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130073.01'>MATH130073.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130073'>数值代数</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/薛军工'>薛军工</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130074.01'>MATH130074.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130074'>积分方程数值解法</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/张云新'>张云新</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130080.01'>MATH130080.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130080'>科学计算</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/魏益民'>魏益民</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130091.01'>MATH130091.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130091'>数学分析原理</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/周子翔'>周子翔</a><br /><a href='https://fdu-math.github.io/teachers/邵杰'>邵杰</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130091.02'>MATH130091.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130091'>数学分析原理</a></td>
                    <td>5</td>
                    <td><a href='https://fdu-math.github.io/teachers/周子翔'>周子翔</a><br /><a href='https://fdu-math.github.io/teachers/邵杰'>邵杰</a></td>
                    <td>教授<br />Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130108.01'>MATH130108.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130108'>反问题的正则化理论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/陆帅'>陆帅</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130111.01'>MATH130111.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130111'>流形的拓扑学</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/马继明'>马继明</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130112.01'>MATH130112.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130112'>拓扑学Ⅱ</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/马继明'>马继明</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130112h.01'>MATH130112h.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130112'>代数拓扑(H)</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/吕志'>吕志</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130113.01'>MATH130113.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130113'>几何拓扑选讲</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/李平'>李平</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130114.01'>MATH130114.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130114'>泛函分析续论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/郭坤宇'>郭坤宇</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130121.01'>MATH130121.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130121'>现代偏微分方程</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/周忆'>周忆</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130126.01'>MATH130126.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130126'>遍历论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/田学廷'>田学廷</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130130.01'>MATH130130.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130130'>代数几何初步</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/江智'>江智</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130133.01'>MATH130133.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130133'>解析数论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/石荣刚'>石荣刚</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130137.01'>MATH130137.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130137'>线性与非线性规划</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/杨卫红'>杨卫红</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130139.01'>MATH130139.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130139'>几何测度论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/华波波'>华波波</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130141.01'>MATH130141.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130141'>图论初步</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/吴河辉'>吴河辉</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130143h.03'>MATH130143h.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130143'>现代代数学II(H)</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/王庆雪'>王庆雪</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130152.01'>MATH130152.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130152'>经典数学思想I</a></td>
                    <td>2</td>
                    <td><a href='https://fdu-math.github.io/teachers/傅吉祥'>傅吉祥</a><br /><a href='https://fdu-math.github.io/teachers/沈维孝'>沈维孝</a><br /><a href='https://fdu-math.github.io/teachers/姚一隽'>姚一隽</a></td>
                    <td>教授<br />教授<br />教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130154.01'>MATH130154.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130154'>数学分析I（英才班）</a></td>
                    <td>6</td>
                    <td><a href='https://fdu-math.github.io/teachers/楼红卫'>楼红卫</a><br /><a href='https://fdu-math.github.io/teachers/蔡圆'>蔡圆</a></td>
                    <td>教授<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130154.02'>MATH130154.02</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130154'>数学分析I（英才班）</a></td>
                    <td>6</td>
                    <td><a href='https://fdu-math.github.io/teachers/楼红卫'>楼红卫</a><br /><a href='https://fdu-math.github.io/teachers/蔡圆'>蔡圆</a></td>
                    <td>教授<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130154.03'>MATH130154.03</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130154'>数学分析I（英才班）</a></td>
                    <td>6</td>
                    <td><a href='https://fdu-math.github.io/teachers/楼红卫'>楼红卫</a><br /><a href='https://fdu-math.github.io/teachers/蔡圆'>蔡圆</a></td>
                    <td>教授<br />青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130159.01'>MATH130159.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130159'>现代概率论基础I</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/Elie_Francis_AIDEKON'>Elie Francis AIDEKON</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130162.01'>MATH130162.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130162'>独立学习I</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/姚一隽'>姚一隽</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130163.01'>MATH130163.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130163'>独立学习Ⅱ</a></td>
                    <td>4</td>
                    <td><a href='https://fdu-math.github.io/teachers/王志强'>王志强</a></td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130166.01'>MATH130166.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130166'>经典物理选讲</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/周子翔'>周子翔</a><br /><a href='https://fdu-math.github.io/teachers/梁振国'>梁振国</a><br /><a href='https://fdu-math.github.io/teachers/陈曦'>陈曦</a></td>
                    <td>教授<br />副教授<br />青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td><a href='https://fdu-math.github.io/courses/course-id/MATH130167.01'>MATH130167.01</a></td>
                    <td><a href='https://fdu-math.github.io/courses/MATH130167'>Current理论</a></td>
                    <td>3</td>
                    <td><a href='https://fdu-math.github.io/teachers/丁琪'>丁琪</a></td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
            </tbody>
        </table>
    </small>
</div>
## 2022-2023学年第1学期（研究生）
