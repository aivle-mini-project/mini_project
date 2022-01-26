let date = new Date();
let mon;

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
    
    dates.forEach((date, i) => {
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 ?
            'this' :
            'other';
            
            dates[i] =
        `
            <div class="date ${condition}">
                <div class="date-itm">
                    ${show(mon,date)}
                </div>
            </div>
        `;
    });

    document.querySelector('.dates').innerHTML = dates.join('');

    // 오늘 날짜 표시
    mon = viewMonth+1;
    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.date-itm')) {
            if (+date.innerText === today.getDate()) {
                date.classList.add('today');
                break;
            }
            
        }
    }
};

renderCalender();

function prevMonth(){
    date.setMonth(date.getMonth() - 1);
    renderCalender();
};

function nextMonth() {
    date.setMonth(date.getMonth() + 1);
    renderCalender();
};

function goToday() {
    date = new Date();
    renderCalender();
};

// 현재 표시 달 가져오기
function send(){
    return mon;
}

//날짜를 받아서 달력에 날짜와 기분 표현
function show(mon,da){
    if(da == " ") // 이전 달 날짜 표시하지 않는다
        return " "
    else if (da == 1)
        return da+" 😀"
    else if (da == 2)
        return da+" 😐"
    else if (da == 3)
        return da+" 😥"
    else // 저장된 값 없을 시 날짜만 표시
        return da
}
