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
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH010001.01'&gt;MATH010001.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH010001'&gt;预科数学（上）&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/肖晓'&gt;肖晓&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH110001.01'&gt;MATH110001.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH110001'&gt;数学概论&lt;/a&gt;</td>
                    <td>2</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/杭国明'&gt;杭国明&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH115001.01'&gt;MATH115001.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH115001'&gt;天才引导的历程——数学史上的重大发现&lt;/a&gt;</td>
                    <td>1</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/杨翎'&gt;杨翎&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120003.01'&gt;MATH120003.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120003'&gt;高等数学B(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/陆立强'&gt;陆立强&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120003.02'&gt;MATH120003.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120003'&gt;高等数学B(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/石磊'&gt;石磊&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120003.03'&gt;MATH120003.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120003'&gt;高等数学B(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张仑'&gt;张仑&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120003.04'&gt;MATH120003.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120003'&gt;高等数学B(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/任汝飞'&gt;任汝飞&lt;/a&gt;</td>
                    <td>青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120005.02'&gt;MATH120005.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120005'&gt;高等数学C(上）&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/朱慧敏'&gt;朱慧敏&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120007.01'&gt;MATH120007.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120007'&gt;高等数学D&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/许虹'&gt;许虹&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120007.02'&gt;MATH120007.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120007'&gt;高等数学D&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张静'&gt;张静&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120007.05'&gt;MATH120007.05&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120007'&gt;高等数学D&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王珺'&gt;王珺&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120010.01'&gt;MATH120010.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120010'&gt;解析几何&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/莫景科'&gt;莫景科&lt;/a&gt;</td>
                    <td>青年研究员</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120010.02'&gt;MATH120010.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120010'&gt;解析几何&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/杨翎'&gt;杨翎&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120011.01'&gt;MATH120011.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120011'&gt;高等代数Ⅰ&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/朱胜林'&gt;朱胜林&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/齐子豪'&gt;齐子豪&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120011.02'&gt;MATH120011.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120011'&gt;高等代数Ⅰ&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/朱胜林'&gt;朱胜林&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/齐子豪'&gt;齐子豪&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120011.03'&gt;MATH120011.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120011'&gt;高等代数Ⅰ&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/谢启鸿'&gt;谢启鸿&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/冯鸽'&gt;冯鸽&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120011.04'&gt;MATH120011.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120011'&gt;高等代数Ⅰ&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/谢启鸿'&gt;谢启鸿&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/冯鸽'&gt;冯鸽&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120011.05'&gt;MATH120011.05&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120011'&gt;高等代数Ⅰ&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李骏'&gt;李骏&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/韩京俊'&gt;韩京俊&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/江辰'&gt;江辰&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/周杨'&gt;周杨&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年研究员&lt;br /&gt;青年研究员&lt;br /&gt;青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120011.06'&gt;MATH120011.06&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120011'&gt;高等代数Ⅰ&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李骏'&gt;李骏&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/韩京俊'&gt;韩京俊&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/江辰'&gt;江辰&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/周杨'&gt;周杨&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年研究员&lt;br /&gt;青年研究员&lt;br /&gt;青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120012.01'&gt;MATH120012.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120012'&gt;微积分（上）&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张建国'&gt;张建国&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>基础医学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120014.01'&gt;MATH120014.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120014'&gt;数学分析AI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/严金海'&gt;严金海&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/王丽丹'&gt;王丽丹&lt;/a&gt;</td>
                    <td>副教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120014.02'&gt;MATH120014.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120014'&gt;数学分析AI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/严金海'&gt;严金海&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/王丽丹'&gt;王丽丹&lt;/a&gt;</td>
                    <td>副教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120014.03'&gt;MATH120014.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120014'&gt;数学分析AI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/吴昊'&gt;吴昊&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/翟剑'&gt;翟剑&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120014.04'&gt;MATH120014.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120014'&gt;数学分析AI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/吴昊'&gt;吴昊&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/翟剑'&gt;翟剑&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.02'&gt;MATH120016.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张巍'&gt;张巍&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.03'&gt;MATH120016.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张守志'&gt;张守志&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.04'&gt;MATH120016.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/郭跃飞'&gt;郭跃飞&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.05'&gt;MATH120016.05&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王勇'&gt;王勇&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>计算机科学技术学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.06'&gt;MATH120016.06&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/应坚刚'&gt;应坚刚&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>经济学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.07'&gt;MATH120016.07&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/官辉琪'&gt;官辉琪&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.08'&gt;MATH120016.08&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/严金海'&gt;严金海&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.09'&gt;MATH120016.09&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/徐禛'&gt;徐禛&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>管理学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.10'&gt;MATH120016.10&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/谢锡麟'&gt;谢锡麟&lt;/a&gt;</td>
                    <td>正高级讲师</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.11'&gt;MATH120016.11&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/谢锡麟'&gt;谢锡麟&lt;/a&gt;</td>
                    <td>正高级讲师</td>
                    <td>航空航天系</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120016.12'&gt;MATH120016.12&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120016'&gt;数学分析BI&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/吴汉忠'&gt;吴汉忠&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120020.02'&gt;MATH120020.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120020'&gt;线性代数（理工类）&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/蔡志杰'&gt;蔡志杰&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120021.01'&gt;MATH120021.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120021'&gt;高等数学A(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/徐惠平'&gt;徐惠平&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120021.02'&gt;MATH120021.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120021'&gt;高等数学A(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/范恩贵'&gt;范恩贵&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120021.03'&gt;MATH120021.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120021'&gt;高等数学A(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/刘旭胜'&gt;刘旭胜&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120021.04'&gt;MATH120021.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120021'&gt;高等数学A(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/黄昭波'&gt;黄昭波&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120021.05'&gt;MATH120021.05&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120021'&gt;高等数学A(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张永前'&gt;张永前&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120021.08'&gt;MATH120021.08&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120021'&gt;高等数学A(上）&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/刘进'&gt;刘进&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120044.01'&gt;MATH120044.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120044'&gt;线性代数&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/杭国明'&gt;杭国明&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.01'&gt;MATH120045.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/杭国明'&gt;杭国明&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.02'&gt;MATH120045.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/肖晓'&gt;肖晓&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.03'&gt;MATH120045.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/秦振云'&gt;秦振云&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.04'&gt;MATH120045.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/贺丹青'&gt;贺丹青&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.05'&gt;MATH120045.05&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/黄耿耿'&gt;黄耿耿&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.06'&gt;MATH120045.06&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/曲鹏'&gt;曲鹏&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.07'&gt;MATH120045.07&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/朱慧敏'&gt;朱慧敏&lt;/a&gt;</td>
                    <td>高级讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH120045.08'&gt;MATH120045.08&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH120045'&gt;高等数学C I&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王剑波'&gt;王剑波&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130001.01'&gt;MATH130001.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130001'&gt;数学分析III&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李洪全'&gt;李洪全&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/杨志伟'&gt;杨志伟&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130001.02'&gt;MATH130001.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130001'&gt;数学分析III&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李洪全'&gt;李洪全&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/杨志伟'&gt;杨志伟&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130001.03'&gt;MATH130001.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130001'&gt;数学分析III&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/肖体俊'&gt;肖体俊&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/姚鹿鸣'&gt;姚鹿鸣&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130001.04'&gt;MATH130001.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130001'&gt;数学分析III&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/肖体俊'&gt;肖体俊&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/姚鹿鸣'&gt;姚鹿鸣&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130004.01'&gt;MATH130004.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130004'&gt;常微分方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/林伟'&gt;林伟&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130004.02'&gt;MATH130004.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130004'&gt;常微分方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张国华'&gt;张国华&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130004.03'&gt;MATH130004.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130004'&gt;常微分方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/严军'&gt;严军&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130004.04'&gt;MATH130004.04&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130004'&gt;常微分方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/林伟'&gt;林伟&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130005.01'&gt;MATH130005.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130005'&gt;抽象代数&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王庆雪'&gt;王庆雪&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130005.02'&gt;MATH130005.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130005'&gt;抽象代数&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李志远'&gt;李志远&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130005.03'&gt;MATH130005.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130005'&gt;抽象代数&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/陈猛'&gt;陈猛&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130006.01'&gt;MATH130006.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130006'&gt;复变函数&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/陈伯勇'&gt;陈伯勇&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130009.01'&gt;MATH130009.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130009'&gt;概率论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/许明宇'&gt;许明宇&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130009h.01'&gt;MATH130009h.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130009'&gt;概率论(H)&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/谢践生'&gt;谢践生&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130011.01'&gt;MATH130011.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130011'&gt;泛函分析&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/徐胜芝'&gt;徐胜芝&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130011.02'&gt;MATH130011.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130011'&gt;泛函分析&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王凯'&gt;王凯&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130011h.01'&gt;MATH130011h.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130011'&gt;泛函分析(H)&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/姚一隽'&gt;姚一隽&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/章嘉雯'&gt;章嘉雯&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/伊泽霖'&gt;伊泽霖&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年副研究员&lt;br /&gt;高等学校教师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130012.02'&gt;MATH130012.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130012'&gt;数理方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王志强'&gt;王志强&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130012h.01'&gt;MATH130012h.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130012'&gt;数理方程（H）&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/雷震'&gt;雷震&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130013.01'&gt;MATH130013.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130013'&gt;微分几何&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/嵇庆春'&gt;嵇庆春&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130013.02'&gt;MATH130013.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130013'&gt;微分几何&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/谢纳庆'&gt;谢纳庆&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130017h.01'&gt;MATH130017h.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130017'&gt;微分流形(H)&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/东瑜昕'&gt;东瑜昕&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130018.01'&gt;MATH130018.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130018'&gt;小波分析&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张德志'&gt;张德志&lt;/a&gt;</td>
                    <td>讲师</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130022.01'&gt;MATH130022.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130022'&gt;应用偏微分方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王利彬'&gt;王利彬&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130026.01'&gt;MATH130026.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130026'&gt;生物数学&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李春贺'&gt;李春贺&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130027.01'&gt;MATH130027.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130027'&gt;数学金融学&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张奇'&gt;张奇&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130030.01'&gt;MATH130030.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130030'&gt;专题讨论&lt;/a&gt;</td>
                    <td>2</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李春贺'&gt;李春贺&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130032.01'&gt;MATH130032.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130032'&gt;动力系统&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/梁振国'&gt;梁振国&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/张国华'&gt;张国华&lt;/a&gt;</td>
                    <td>副教授&lt;br /&gt;教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130033.01'&gt;MATH130033.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130033'&gt;利息理论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李荣敏'&gt;李荣敏&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130036.01'&gt;MATH130036.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130036'&gt;计算方法&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/高卫国'&gt;高卫国&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130043.01'&gt;MATH130043.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130043'&gt;数论基础&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/任汝飞'&gt;任汝飞&lt;/a&gt;</td>
                    <td>青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130052.01'&gt;MATH130052.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130052'&gt;Fourier分析&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李洪全'&gt;李洪全&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130055.01'&gt;MATH130055.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130055'&gt;非寿险精算数学&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李荣敏'&gt;李荣敏&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130056.01'&gt;MATH130056.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130056'&gt;复分析&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/邱维元'&gt;邱维元&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130057.01'&gt;MATH130057.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130057'&gt;控制理论基础&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/许亚善'&gt;许亚善&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130059.01'&gt;MATH130059.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130059'&gt;数据结构&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/朱松'&gt;朱松&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130067.01'&gt;MATH130067.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130067'&gt;时间序列分析&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/赵冬华'&gt;赵冬华&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130068.01'&gt;MATH130068.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130068'&gt;抽象代数续论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/吴泉水'&gt;吴泉水&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130072.01'&gt;MATH130072.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130072'&gt;数值逼近&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/苏仰锋'&gt;苏仰锋&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130073.01'&gt;MATH130073.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130073'&gt;数值代数&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/薛军工'&gt;薛军工&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130074.01'&gt;MATH130074.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130074'&gt;积分方程数值解法&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/张云新'&gt;张云新&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130080.01'&gt;MATH130080.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130080'&gt;科学计算&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/魏益民'&gt;魏益民&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130091.01'&gt;MATH130091.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130091'&gt;数学分析原理&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/周子翔'&gt;周子翔&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/邵杰'&gt;邵杰&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130091.02'&gt;MATH130091.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130091'&gt;数学分析原理&lt;/a&gt;</td>
                    <td>5</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/周子翔'&gt;周子翔&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/邵杰'&gt;邵杰&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;Null</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130108.01'&gt;MATH130108.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130108'&gt;反问题的正则化理论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/陆帅'&gt;陆帅&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130111.01'&gt;MATH130111.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130111'&gt;流形的拓扑学&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/马继明'&gt;马继明&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130112.01'&gt;MATH130112.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130112'&gt;拓扑学Ⅱ&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/马继明'&gt;马继明&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130112h.01'&gt;MATH130112h.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130112'&gt;代数拓扑(H)&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/吕志'&gt;吕志&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130113.01'&gt;MATH130113.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130113'&gt;几何拓扑选讲&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/李平'&gt;李平&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130114.01'&gt;MATH130114.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130114'&gt;泛函分析续论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/郭坤宇'&gt;郭坤宇&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130121.01'&gt;MATH130121.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130121'&gt;现代偏微分方程&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/周忆'&gt;周忆&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130126.01'&gt;MATH130126.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130126'&gt;遍历论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/田学廷'&gt;田学廷&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130130.01'&gt;MATH130130.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130130'&gt;代数几何初步&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/江智'&gt;江智&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130133.01'&gt;MATH130133.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130133'&gt;解析数论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/石荣刚'&gt;石荣刚&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130137.01'&gt;MATH130137.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130137'&gt;线性与非线性规划&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/杨卫红'&gt;杨卫红&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130139.01'&gt;MATH130139.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130139'&gt;几何测度论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/华波波'&gt;华波波&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130141.01'&gt;MATH130141.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130141'&gt;图论初步&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/吴河辉'&gt;吴河辉&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130143h.03'&gt;MATH130143h.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130143'&gt;现代代数学II(H)&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王庆雪'&gt;王庆雪&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130152.01'&gt;MATH130152.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130152'&gt;经典数学思想I&lt;/a&gt;</td>
                    <td>2</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/傅吉祥'&gt;傅吉祥&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/沈维孝'&gt;沈维孝&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/姚一隽'&gt;姚一隽&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;教授&lt;br /&gt;教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130154.01'&gt;MATH130154.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130154'&gt;数学分析I（英才班）&lt;/a&gt;</td>
                    <td>6</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/楼红卫'&gt;楼红卫&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/蔡圆'&gt;蔡圆&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130154.02'&gt;MATH130154.02&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130154'&gt;数学分析I（英才班）&lt;/a&gt;</td>
                    <td>6</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/楼红卫'&gt;楼红卫&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/蔡圆'&gt;蔡圆&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130154.03'&gt;MATH130154.03&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130154'&gt;数学分析I（英才班）&lt;/a&gt;</td>
                    <td>6</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/楼红卫'&gt;楼红卫&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/蔡圆'&gt;蔡圆&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;青年副研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130159.01'&gt;MATH130159.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130159'&gt;现代概率论基础I&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/Elie_Francis_AIDEKON'&gt;Elie Francis AIDEKON&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130162.01'&gt;MATH130162.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130162'&gt;独立学习I&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/姚一隽'&gt;姚一隽&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130163.01'&gt;MATH130163.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130163'&gt;独立学习Ⅱ&lt;/a&gt;</td>
                    <td>4</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/王志强'&gt;王志强&lt;/a&gt;</td>
                    <td>教授</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130166.01'&gt;MATH130166.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130166'&gt;经典物理选讲&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/周子翔'&gt;周子翔&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/梁振国'&gt;梁振国&lt;/a&gt;&lt;br /&gt;&lt;a href='https://fdu-math.github.io/teachers/陈曦'&gt;陈曦&lt;/a&gt;</td>
                    <td>教授&lt;br /&gt;副教授&lt;br /&gt;青年研究员</td>
                    <td>数学科学学院</td>
                </tr>
                <tr>
                    <td>&lt;a href='https://fdu-math.github.io/courses/course-id/MATH130167.01'&gt;MATH130167.01&lt;/a&gt;</td>
                    <td>&lt;a href='https://fdu-math.github.io/courses/MATH130167'&gt;Current理论&lt;/a&gt;</td>
                    <td>3</td>
                    <td>&lt;a href='https://fdu-math.github.io/teachers/丁琪'&gt;丁琪&lt;/a&gt;</td>
                    <td>副教授</td>
                    <td>数学科学学院</td>
                </tr>
            </tbody>
        </table>
    </small>
</div>
## 2022-2023学年第1学期（研究生）
