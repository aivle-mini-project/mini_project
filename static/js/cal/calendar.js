let date = new Date();
let mon,yea;
var arr=[];

const renderCalender = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    document.querySelector('.year').textContent = `${viewYear}`;
    document.querySelector('.month').textContent = `${viewMonth + 1}`;

    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();

    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];


    if (PLDay !== 6) {
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(" ");
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(" ");
    }

    const dates = prevDates.concat(thisDates, nextDates);
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);
    

    // 오늘 날짜 표시
    mon = viewMonth+1;
    yea = viewYear;

    dates.forEach((date, i) => {
        const today = new Date();
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 ?
            'this' :
            'other';
            
            if(viewMonth === today.getMonth() && viewYear === today.getFullYear()&&date == today.getDate()){
                dates[i] =
                `  
                    <div class="date ${condition}">
                        <div class="today">
                            ${show(mon,date)}
                        </div>
                    </div>
                `;
            }
            else{
                dates[i] =
                `  
                    <div class="date ${condition}">
                        <div class="date-itm">
                            ${show(mon,date)}
                        </div>
                    </div>
                `;
            }
    });

    document.querySelector('.dates').innerHTML = dates.join('');
};

//날짜를 받아서 달력에 날짜와 기분 표현
function show(mon,da){
    if(String(mon).length<2){ // 1~9월
        for(var i=0;i<s.length;i++){ // 저장된 날짜 찾아라!
            if(s[i].register_date.substr(0,4)==String(yea)){ //같은 년도니?
                if (s[i].register_date.substr(6,1) == String(mon)){ // 같은 월이니?
                    if(s[i].register_date.substr(9,1)==' '){ // 1 ~ 9일
                        if (String(da) == s[i].register_date.substr(10,1))
                            return emoji(s[i].feel)+ ' '+ da
                    }
                    else { // 10일~
                        if (String(da) == s[i].register_date.substr(9,2))
                            return emoji(s[i].feel)+ ' '+ da
                    }
                }
            }
        }
        if(da == " ") // 이전 달 날짜 표시하지 않는다
            return " "
        else // 저장된 값 없을 시 날짜만 표시
            return da
    }
    else { // 10~12월
        for(var i=0;i<s.length;i++){ // 저장된 날짜 찾아라!
            if(s[i].register_date.substr(0,4)==String(yea)){//같은 년도니?
                if (s[i].register_date.substr(5,2) == String(mon)){ // 같은 월이니?
                    if(s[i].register_date.substr(9,1)==' '){ // 1 ~ 9일
                        if (String(da) == s[i].register_date.substr(10,1))
                            return emoji(s[i].feel)+ ' '+ da
                    }
                    else { // 10일~
                        if (String(da) == s[i].register_date.substr(9,2))
                            return emoji(s[i].feel)+ ' '+ da
                    }
                }
            }
        }
        if(da == " ") // 이전 달 날짜 표시하지 않는다
            return " "
        else // 저장된 값 없을 시 날짜만 표시
            return da
    }
}

// 하단 문장 출력
const infoE = () => {
    const emotion=[];
    // 작성 날짜가 현재 년도, 달과 같다면 일기 목록 표시 아니라면 넘어간다
    if(String(mon).length<2){ // 1~9월
        for(var i=0;i<s.length;i++){
            if(s[i].register_date.substr(0,4)==String(yea)){
                if(s[i].register_date.substr(6,1) == String(mon)){
                    emotion[i] =
                    `
                    
                        <br>날짜 : ${s[i].register_date.substr(0,12)} | 기분 : ${emoji(s[i].feel)} | 일기 : ${s[i].write}<br>
                   
                    `;
                }
            }
            else{
                emotion[i] =
                `
                    <div><div>
                `;
            }
        }
    }
    else{ // 10~12월
        for(var i=0;i<s.length;i++){
            if(s[i].register_date.substr(0,4)==String(yea)){
                if(s[i].register_date.substr(5,2) == String(mon)){
                    emotion[i] =
                    `
                    <br>날짜 : ${s[i].register_date.substr(0,12)} | 기분 : ${emoji(s[i].feel)} | 일기 : ${s[i].write}<br>
                    `;
                }
            }
            else{
                emotion[i] =
                `
                    <div><div>
                `;
            }
            
        }
    }
    
    let te = document.querySelector('.emo').innerHTML = emotion.join('');
}

renderCalender();

function prevMonth(){
    date.setMonth(date.getMonth() - 1);
    renderCalender();
    infoE();
};

function nextMonth() {
    date.setMonth(date.getMonth() + 1);
    renderCalender();
    infoE();
};

function goToday() {
    date = new Date();
    renderCalender();
};

function emoji(a){
    if(a =='neutral')
        return '😐'
    else if(a=='positive')
        return '😀'
    else if(a=='negative')
        return '😥'
}